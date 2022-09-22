---
title: 'OBEX in Nautilus'
slug: obex-in-nautilus
date: 2006-10-05T09:22:22+08:00
tags: ['Gnome', 'Ubuntu']
---

When I got my new laptop, one of the features it had that my previous
one didn\'t was Bluetooth support. There are a few Bluetooth related
utilities for Gnome that let you send and receive SMS messages and a few
other things, but a big missing feature is the ability to transfer files
to and from the phone easily.

Ideally, I\'d be able to browse the phone\'s file system using Nautilus.
Luckily, the [Maemo](http://www.maemo.org/) guys have already done the
hard work of writing a gnome-vfs module that speaks the OBEX FTP
protocol. I had a go at compiling it on my laptop (running Ubuntu Edgy),
and you can see the result below:

{{< figure src="obex-nautilus.jpg"
        caption="Browsing files and viewing images stored on my phone" >}}

There are a few rough edges:

-   While I can get a list of discovered devices at the location
    `obex:///`, it displays the raw bluetooth addresses rather than
    device names. Furthermore, the files displayed here are symlinks to
    the appropriate `obex://[$ADDRESS]/` URLs, which aren\'t that useful
    given that gnome-vfs does not support symlinks pointing to other
    schemes or authorities. This could be fixed by generating `.desktop`
    files instead, which would make it possible to provide nice icons
    too.
-   Can\'t rename files. This might be a limitation of the OBEX FTP
    protocol though: the man page for the command line `obexftp` client
    says moves only work with Siemens phones.
-   Doesn\'t seem to handle devices disappearing very well --- when I
    tried turning off Bluetooth on my phone and told Nautilus to reload
    the window, Nautilus hung and stopped redrawing til I turned
    Bluetooth on again.

I don\'t have any ready made binaries for others to try at this point.
Below are some notes for anyone else who wants to try building it:

-   You\'ll need the `osso-gwconnect`, `osso-gwobex` and
    `osso-gnomevfs-extra` modules. I grabbed them from Maemo Subversion.
-   When trying to build a debian package for `osso-gwconnect`, I
    removed the `libosso-dev` and `mce-dev` build dependencies, and made
    an equivalent change to the configure arguments in `debian/rules`.
    The configure script also asks for BlueZ 3.2, while Edgy only has
    3.1. The package built fine when I decreased the minimum version
    requirement.
-   You\'ll need to build `osso-gwconnect` and `osso-gwobex` before
    `osso-gnomevfs-extra`. There are a few build problems with this last
    module:
    1.  The `autogen.sh` script asks for automake 1.8.x specifically,
        but works fine with the current 1.9.x releases.
    2.  I had to change a `dbus_connection_disconnect()` call to
        `dbus_connection_close()` in `obex-module/src/om-dbus.c`.
    3.  You only need to build the `obex-utils` and `obex-module`
        directories. There are other bits in this module that you
        probably don\'t want, and some bits like the replacement GTK
        filesystem backend didn\'t build for me.

With a little bit of work, this would fit into the main Gnome desktop
quite well. When talking to [Bastien](http://hadess.net/) a while back,
he said that the extra dbus daemons shouldn\'t really be necessary, so
it might be worth trying to bypass them.

---
### Comments:
#### Johan Hedberg - <time datetime="2006-10-05 16:53:46">5 Oct, 2006</time>

Hi,

The osso-gwconnect dependency should be easily removable if you use
bluez-utils-3.7 or newer. Starting with that version hcid provides a
functionally equivalent RFCOMM D-Bus interface as btcond from
osso-gwconnect does (which is what the OBEX module uses). However, this
interface is currently categorized as experimental which means you need
to give hcid the -x option for it to be enabled.

The osso-gwobex dependency can hopefully also be removed in the future.
Work has started on glib bindings for openobex which would be
functionally equivalent to the async API the gwobex provides. You can
see the current work in the glib subdirectory of the openobex CVS on
sourceforge. Hopefully we can release a first version during the autumn
(within a month or so).

---
#### [Davyd](http://www.davyd.id.au/) - <time datetime="2006-10-05 20:12:09">5 Oct, 2006</time>

It\'s great that this has been done (not that my phone has bluetooth). I
once tried to do something like this using Gammu (when it forked from
Gnokii), but ended up trying to cut myself instead.

---
#### [Jonh Wendell](http://www.bani.com.br) - <time datetime="2006-10-05 21:52:53">5 Oct, 2006</time>

This is great. KDE already has a kind of that, hasn\'t it?

Once i managed to transfer files to/from phone via obex with fuse and
obexfs, just frontend to obexftp. (<http://www.bani.com.br/?p=10> -
Brazilian Portuguese)

Seeing that feature in nautilus/gnomevfs is very cool!

Will it in 2.16?

---
#### James Henstridge - <time datetime="2006-10-05 22:24:12">5 Oct, 2006</time>

Johan: great news!

Davyd: looking at the code, the VFS method should handle infrared too.
So if your phone can do OBEX FTP over IR, you could still use it.

John: The screenshot is from an Ubuntu Edgy system, which has Gnome
2.16. You won\'t find it in the default install though \-- I compiled
the code from the Maemo Subversion repository (with the few
modifications listed in the main text).

---
#### Ross - <time datetime="2006-10-05 22:28:01">5 Oct, 2006</time>

Matthew Garrett was doing some very interesting work that would replace
bits of this, by integrating BlueZ into HAL. There are HAL objects for
every phone detected, which can be probed and so on.

---
#### [Marius Gedminas](http://mg.b4net.lt/) - <time datetime="2006-10-06 01:29:41">6 Oct, 2006</time>

I was very disappointed recently when I did an apt-cache search in
Ubuntu and didn\'t find any graphical OBEX FTP client. (Googling for a
FUSE module also gave me no results, so it is very interesting to see
that link to obexfs.)

Is there any chance for the OBEX FTP gnomevfs module to make it into
Edgy+1?

---
#### [AdamW](http://www.happyassassin.net/) - <time datetime="2006-10-06 06:04:50">6 Oct, 2006</time>

I may be missing something obvious here, but why does everyone want to
use OBEX FTP directly? What\'s wrong with nautilus-sendto-bluetooth? I
use it regularly for sending files to my phone - right click file, Send
to\..., pick the phone - and it works very well and seems brain-dead
simple to me. Sending files from the phone to the PC I do from, well,
the phone, which also seems to make sense. What am I missing? :)

---
#### James Henstridge - <time datetime="2006-10-06 16:52:25">6 Oct, 2006</time>

AdamW: one simple reason is that this provides the same interface for
copying files to/from my phone as I have for accessing my camera, PSP,
USB sticks, etc.

Initiating the send from my phone feels clunky, and is pretty
inconvenient if I want to transfer multiple files.

---
#### [felipe](http://pollycoke.wordpress.com) - <time datetime="2006-10-06 19:43:34">6 Oct, 2006</time>

Wow, do you know if there\'s any plan to support OBEX via USB? It\'s
much faster than bluetooth and in many cases your phone comes with a
free USB cable.

Openobex already supoprts USB

Thanks

---
#### matt - <time datetime="2006-10-17 07:49:39">17 Oct, 2006</time>

You just can mount the phone filesystem into any directory.
<http://openobex.triq.net/obexfs>

But only the user who mounts it can access the mount directory, even
root isn\'t allowed to do that! :-/

here\'s my script:

\#!/bin/bash
obexfs -b 00:12:EE:9A:19:39 -B 6 /mnt/k750i/
nautilus \--no-desktop \--browser /mnt/k750i

---
#### Wout - <time datetime="2006-10-17 23:07:47">17 Oct, 2006</time>

Can you post some (checkinstall) deb files??? You would be a hero if you
did ;-)

---
#### [Alex Kanavin](http://www.sensi.org/~ak/openobex-usb/) - <time datetime="2006-10-21 01:08:16">21 Oct, 2006</time>

The author of USB support in openobex here :) I plan to see what I can
do with obexfs in Fedora and perhaps nicely integrate it into their
removable media infrastructure (which may be shared with other distros -
I dunno yet). So that when you plug your phone in, you get a nice icon
on your desktop, just like your flash drive or digicam.

---
#### [Olivier Berger](http://www.olivierberger.com/weblog/) - <time datetime="2006-11-04 00:30:37">4 Nov, 2006</time>

Hmmm\... I\'m not sure this hasn\'t been addressed in the comments
indirectly, but I used to check gnome-bluetooth-manager, and it looked
quite promising : <http://usefulinc.com/software/gnome-bluetooth>

My 2 cents,

---
