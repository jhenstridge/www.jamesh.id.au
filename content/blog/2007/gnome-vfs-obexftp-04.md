---
title: 'gnome-vfs-obexftp 0.4'
slug: gnome-vfs-obexftp-04
date: 2007-06-19T13:16:39+08:00
tags: ['Gnome', 'Ubuntu']
---

It hasn\'t been long since the last gnome-vfs-obexftp release, but I
thought it\'d be good to get these fixes out before undertaking more
invasive development. The new version is available from:

> <http://download.gnome.org/sources/gnome-vfs-obexftp/0.4/>

The highlights of this release are:

-   If the phone does not provide free space values in the OBEX
    capability object, do not report this as zero free space. This fixes
    Nautilus file copy behaviour on a number of Sony Ericsson phones.
-   Fix date parsing when the phone returns UTC timestamps in the folder
    listings.
-   Add some tests for the capability object and folder listing XML
    parsers. Currently has sample data for Nokia 6230, Motorola KRZR K1,
    and Sony K800i, Z530i and Z710i phones.

These fixes should improve the user experience for owners of some Sony
Ericsson phones by letting them copy files to the phone, rather than
Nautilus just telling them that there is no free space. Unfortunately,
if there isn\'t enough free space you\'ll get an error part way through
the copy. This is the best that can be done with the information
provided by the phone.

**Test Suite**

As noted in the third point, I\'ve started to build up a collection of
capability and folder listing XML documents produced by various phone
models. This serves a dual purpose:

1.  Ensure that the capability object and folder listing XML parsers
    don\'t regress between releases. It is impractical for me to test
    gnome-vfs-obexftp against all these phone models since I don\'t have
    the hardware or time.
2.  Give an idea of what information the different phone models provide,
    which should be useful when planning new features.

If you have an OBEX FTP capable phone that is not already in the test
suite, it\'d be useful if you could collect the data and [file a
bug](https://bugs.launchpad.net/gnome-vfs-obexftp/+filebug). The
information can be collected using the command line \"obexftp\" program
(part of the \"obexftp\" package on Ubuntu). The following commands will
give the capability object and root folder listing:

    obexftp --bluetooth $BDADDR --capability
    obexftp --bluetooth $BDADDR --list

It\'d also be useful to get a listing for one or two other directories.
If there is a memory card, it\'d be useful to get that folder. For
example:

    obexftp --bluetooth $BDADDR --list "Memory card/"

It\'d be most useful if the transcript of the various commands were
included as an attachment. Feel free to censor personal information if
you want (e.g. the phone serial number in the capability object, some
non-default file names).

In particular, I wouldn\'t mind getting information on phones with
brands other than than Nokia or Sony to see what info they provide.

---
### Comments:
#### [Lasse Bigum](http://www.zenith.dk) - <time datetime="2007-06-19 16:13:36">2 Jun, 2007</time>

I have a Motorola RAZR V3 that I will try to remember to get the data
from when I get the time.

---
#### [Mikko Ohtamaa](http://www.redinnovation.com) - <time datetime="2007-06-20 23:26:17">3 Jun, 2007</time>

Obexftp does not work with my Nokia E70 phone very well. Version 0.2 was
able to open the phone in Nautilus, but looks like version 0.4 doesn\'t
do anything when I click my phone icon in obex://.

1\. How do I enable debug output for obexftp?

2\. How do I enable debug output for Bluetooth connection?

I think I can trace down the issue if you can provide me some hints how
to start.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-06-21 09:26:45">4 Jun, 2007</time>

Mikko: please file a bug, and I\'ll walk you through a few things you
could do to help identify the problem.

---
#### Joel - <time datetime="2007-06-24 20:09:21">0 Jun, 2007</time>

Hello,

I have a nokia 6111, and I\'m running ubuntu gutsy, and I can\'t work
out how to make the two pair. Any advice?

Thanks.

---
