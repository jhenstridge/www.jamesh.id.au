---
title: 'New stuff in gnome-vfs-obexftp'
slug: obexftp-changes
date: 2007-06-11T16:03:49+08:00
---

Recently, [Bastien](http://www.hadess.net/) has been doing [a bit of
hacking on
gnome-vfs-obexftp](http://hadessuk.blogspot.com/2007/06/mo-bluetooth.html "Mo' Bluetooth").
The changes remove the use of the `org.bluez.RFCOMM` interface to
`hcid`, instead doing SDP and createing RFCOMM sockets directly. This
removes the need to run `hcid` with its experimental interfaces enabled.
This is also good because the `org.bluez.RFCOMM` interface has been
removed in newer releases (replaced by `org.bluez.serial.Manager`).

I\'ve now integrated that patch and made a number of further clean ups
so that we don\'t need any D-Bus requests to establish the connection to
the remote device. Now the only D-Bus requests being made are for device
enumeration used for the \"`obex:///`\" virtual folder. Should make it
easier to switch over to
[HAL](http://www.freedesktop.org/wiki/Software/hal) if/when it supports
scanning for Bluetooth devices.

I also had a go at fixing [bug
\#116912](https://bugs.launchpad.net/bugs/116912 "Free Space on Phone's SD Card Incorrect in Nautilus").
Using the memory type information provided in folder listings on Nokia
phones, I\'ve now got the `get_volume_free_space()` routine to return
the free space of the appropriate memory type for the folder. While this
works fine in the GNOME-VFS API, unfortunately it hasn\'t improved
matters in Nautilus. It seems to always request the free space for the
root directory, so I still see an incorrect free space value for e.g.
`obex://[...]/Memory%20card/` on my phone. I\'m not sure how I\'ll go
about fixing that.

There does appear to be some problems with some Sony phones, but I
don\'t have any hardware to test this. Perhaps this is something to work
on in the next release if I can get some help debugging the problem.

**Update:** looks like I spoke too soon about Nautilus not getting the
correct free space value.  After restarting Nautilus again, it started
showing the free space correctly, and I can copy large files to my
memory card.

---
### Comments:
#### [Stefano Costa](http://blog.linux.it/steko) - <time datetime="2007-06-11 18:23:51">1 Jun, 2007</time>

Is cable support going into gnome-vfs-obexftp anytime soon? It would be
really great to switch from tedious and repetitive CLI to Nautilus for
handling files on my N70 (the cable came for free in the package, I\'m
not going to buy a BT adapter for my quite-old laptop). Thanks.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-06-11 19:25:26">1 Jun, 2007</time>

Stefano: I\'ve [filed a bug](https://bugs.launchpad.net/bugs/119801) to
track this feature, but don\'t have any immediate plans to implement it.

I didn\'t have much luck establishing an OBEX connection to my phone (a
Nokia 6230) over USB, so I am not sure how I\'d test it. You are welcome
to submit patches though.

---
#### Frequent Traveller - <time datetime="2007-06-11 19:36:48">1 Jun, 2007</time>

Great work! Any reason why it\'s not maintained in the GNOME SVN? Also,
is there going to be a new release?

Keep up!

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-06-11 19:55:02">1 Jun, 2007</time>

It isn\'t in Subversion because I prefer to use Bazaar for source code
management. Launchpad is a convenient place to host said branches (GNOME
is not providing Bazaar branch hosting other than in people\'s home
directories on www.gnome.org).

There will probably be a new release in a few days. Most of the
functionality is in place, so there is just some testing and other
administrative stuff to finish off.

---
#### [James Henstridge &raquo; gnome-vfs-obexftp 0.3](gnome-vfs-obexftp-03.md) - <time datetime="2007-06-13 11:37:25">3 Jun, 2007</time>

\[\...\] James Henstridge Random stuff Skip to content « New stuff in
gnome-vfs-obexftp \[\...\]

---
