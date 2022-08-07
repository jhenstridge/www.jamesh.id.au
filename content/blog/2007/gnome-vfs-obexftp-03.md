---
title: 'gnome-vfs-obexftp 0.3'
slug: gnome-vfs-obexftp-03
date: 2007-06-13T11:37:21+08:00
tags: ['Gnome', 'Launchpad', 'Ubuntu']
---

I\'ve just released a new version of gnome-vfs-obexftp, which includes
the features [discussed
previously](http://blogs.gnome.org/jamesh/2007/06/11/obexftp-changes/).
It can be downloaded from:

> <http://download.gnome.org/sources/gnome-vfs-obexftp/0.3/>

The highlights of the release include:

-   Sync osso-gwobex and osso-gnome-vfs-extras changes from Maemo
    Subversion.
-   Instead of asking hcid to set up the RFCOMM device for
    communication, use an RFCOMM socket directly. This is both faster
    and doesn\'t require enabling experimental hcid interfaces. Based on
    work from Bastien Nocera.
-   Improve free space calculation for Nokia phones with multiple memory
    types (e.g. phone memory and a memory card). Now the free space for
    the correct memory type for a given directory should be returned.
    This fixes various free-space dependent operations in Nautilus such
    as copying files.

Any bug reports should be filed in Launchpad at:

> <https://bugs.launchpad.net/gnome-vfs-obexftp/>

---
### Comments:
#### cruiseoveride - <time datetime="2007-06-16 10:59:49">6 Jun, 2007</time>

I needed a really quick and simple solution to obexftp, so in 3hrs i
wrote my own bash like program that simply parses the xml output from
obexftp commands using libxml and lets me, so far, \"ls\",\"cd\".\"cp\"
haha, what a silly stupid program.

I wish i knew how to use gnome-vfs, i really need usb support, can i
help you?\
I dont know much about gnome-vfs or obex, but i can write any boiler
plate code you need.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-06-16 19:15:27">6 Jun, 2007</time>

cruiseoveride: I\'ve filed a bug to track the USB feature as [bug
119801](https://bugs.launchpad.net/bugs/119801). I haven\'t managed to
connect to do OBEX over USB with my phone (a Nokia 6230), so haven\'t
really had any motivation or opportunity to work on it.

If you can work out how to identify OBEX over USB devices (maybe via the
data HAL discovers?), and how to establish the connection, that could be
useful.

---
#### cruiseoveride - <time datetime="2007-06-17 00:18:30">0 Jun, 2007</time>

OK, i just downloaded the obexftp source, let me see the \"happy path\"
it takes when i connect over usb, and i\'ll give you what i find.

I\'m also thinking of intergrating my prompt into obexftp itself, so to
make it a proper \"ftp\" client :)

---
#### cruiseoveride - <time datetime="2007-06-17 00:52:29">0 Jun, 2007</time>

Stepping through a \"sudo ./obexftp -u 1 -c \'/C:/Data\' -l\" with ddd,
reveals a few interesting things

I can give you a shell on my machine, there is a nokia E50 connected to
it and it is working beautifully with obexftp. Send me confirmation to
my email, and ill give you credentials.

---
