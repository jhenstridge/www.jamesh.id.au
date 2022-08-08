---
title: 'Extracting BIOS images and tools from ThinkPad update ISOs'
slug: extracting-thinkpad-bios-image
date: 2012-11-13T16:58:00+08:00
tags: ['Python']
---

With my old ThinkPad, Lenovo provided BIOS updates in the form of
Windows executables or ISO images for a bootable CD.  Since I had wiped
Windows partition, the first option wasn\'t an option.  The second
option didn\'t work either, since it expected me to be using the drive
in the base I hadn\'t bought.  Luckily I was able to just copy the
needed files out of the ISO image to a USB stick that had been set up to
boot DOS.

When I got my new ThinkPad, I had hoped to do the same thing but found
that the update ISO images appeared to be empty when mounted.  It seems
that the update is handled entirely from an [El
Torito](http://en.wikipedia.org/wiki/El_Torito_%28CD-ROM_standard%29 "El Torito (CD-ROM standard)")
emulated hard disk image (as opposed to using the image only to
bootstrap the drivers needed to access the CD).

So I needed some way to extract that boot image from the ISO.  After a
little reading of the spec, I put together the following Python script
that does the trick:

    import struct
    import sys

    SECTOR_SIZE = 2048

    def find_image(fp):
        # el-torito boot record descriptor
        fp.seek(0x11 * SECTOR_SIZE)
        data = fp.read(SECTOR_SIZE)
        assert data[:0x47] == b'\x00CD001\x01EL TORITO SPECIFICATION' + b'\x0' * 41
        boot_catalog_sector = struct.unpack('<L', data[0x47:0x4B])[0]

        # check the validation entry in the catalog
        fp.seek(boot_catalog_sector * SECTOR_SIZE)
        data = fp.read(0x20)
        assert data[0:1] == b'\x01'
        assert data[0x1e:0x20] == b'\x55\xAA'
        assert sum(struct.unpack('<16H', data)) % 0x10000 == 0

        # Read the initial/default entry
        data = fp.read(0x20)
        (bootable, image_type, load_segment, system_type, sector_count,
         image_sector) = struct.unpack('<BBHBxHL', data[:12])
        image_offset = image_sector * SECTOR_SIZE
        if image_type == 1:
            # 1.2MB floppy
            image_size = 1200 * 1024
        elif image_type == 2:
            # 1.44MB floppy
            image_size = 1440 * 1024
        elif image_type == 3:
            # 2.88MB floppy
            image_size = 2880 * 1024
        elif image_type == 4:
            # Hard disk image.  Read the MBR partition table to locate file system
            fp.seek(image_offset)
            data = fp.read(512)
            # Read the first partition entry
            (bootable, part_type, part_start, part_size) = struct.unpack_from(
                '<BxxxBxxxLL', data, 0x1BE)
            assert bootable == 0x80 # is partition bootable?
            image_offset += part_start * 512
            image_size = part_size * 512
        else:
            raise AssertionError('unhandled image format: %d' % image_type)

        fp.seek(image_offset)
        return fp.read(image_size)

    if __name__ == '__main__':
        with open(sys.argv[1], 'rb') as iso, open(sys.argv[2], 'wb') as img:
            img.write(find_image(iso))

It isn\'t particularly pretty, but does the job and spits out a 32MB
FAT disk image when run on the ThinkPad X230 update ISOs. It is then a
pretty easy task of copying those files onto the USB stick to run the
update as before. Hopefully owners of similar laptops find this
useful.

There appears to be an EFI executable in there too, so it is possible
that the firmware update could be run from the EFI system partition
!!too.  I haven\'t had the courage to try that though.

---
### Comments:
#### Kim - <time datetime="2012-11-13 18:08:34">13 Nov, 2012</time>

Hi James,

there is a much much simpler solution to boot this ISO image without a
windows partition. I was in the same situation, since\
I bought a lenovo x121 which only has an SSD and no optical drive. Space
on the SSD being scarce, I promptly wiped the windows\
partition. To boot on a bootable iso without optical drive:

\(1\) install grub-imageboot\
(2) copy your iso file in /boot/images/\
(3) run update-grub2\
(4) profit! (that is reboot and you will get a grub entry to boot your
iso as-if it had been loaded from a CD).

I updated my bios this way, worked flawlessly.\
You can put all sorts of images in that directory (e.g. bootable floppy
images with the .img suffix are also recognized).

HTH,\
\--\
Kim

---
#### [Marius Gedminas](http://gedmin.as) - <time datetime="2012-11-13 21:13:36">13 Nov, 2012</time>

The genisoimage package in Ubuntu ships a /usr/bin/geteltorito, which
can be used to achieve the same ends:

geteltorito -o firmware.img firmware.iso

For some ISO images even that\'s not necessary: you can boot the ISO
directly with grub and syslinux\'s memdisk, as described here:
http://www.donarmstrong.com/posts/x200\_bios\_update/

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2012-11-14 10:42:23">14 Nov, 2012</time>

\@Marius Gedminas: that geteltorito script looks like it would have done
what I wanted. It was still fun working out how to pull the image apart
though.

I\'m still somewhat interested in whether it would be possible to run
the BIOS updates from the pre-OS EFI shell though. If it is, it probably
isn\'t well tested though, since the installed copy of Windows was set
to boot in legacy BIOS mode despite the machine having a UEFI BIOS.

---
#### AirMaxVI - <time datetime="2012-12-20 00:10:21">20 Dec, 2012</time>

hi James,

Can you give me some hints of how to execute this script on Linux.\
I am complete newbie in programming, scripting and linux.\
Can I copy the content in a file with extension .py and run it in
terminal typing python script.py for instance.\
Thanks

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2013-01-23 11:05:22">23 Jan, 2013</time>

\@AirMaxVI: that should work. Alternatively, you can use the existing
geteltorito script Marius mentioned in an earlier comment.

---
