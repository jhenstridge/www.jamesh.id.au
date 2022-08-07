---
title: 'Building obex-method'
slug: building-obex-method
date: 2006-10-21T07:11:55+08:00
draft: false
tags: ['Gnome', 'Ubuntu']
---

I published a Bazaar branch of the Nautilus obex method here:

> `http://bazaar.launchpad.net/~jamesh/+junk/gnome-vfs-obexftp`

This version works with the `hcid` daemon included with Ubuntu Edgy,
rather than requiring the `btcond` daemon from
[Maemo](http://www.maemo.org).

Some simple instructions on building it:

1.  Download and build the `osso-gwobex` library:\

    > `svn checkout https://stage.maemo.org/svn/maemo/projects/connectivity/osso-gwobex/trunk osso-gwobex`

    The debian/ directory should work fine to build a package using
    `debuild`.

2.  Download and build the obex module:\

    > `bzr branch http://bazaar.launchpad.net/~jamesh/+junk/gnome-vfs-obexftp`

    There is no debian packaging for this --- just an `autogen.sh`
    script.

It should work on other distributions, but I haven\'t tried it. The main
requirement is `bluez-utils` 3.7, and that `-x` is passed to `hcid` to
enable the `org.bluez.RFCOMM` interface.

Still to do is cleaning up the `obex:///` listing of bonded devices, so
that it serves [desktop
entries](http://standards.freedesktop.org/desktop-entry-spec/latest/)
rather than symlinks, so that it is usable in Nautilus. This would also
make it easier to show the device names to the user and get nice icons.

---
### Comments:
#### pel - <time datetime="2006-10-21 21:41:03">6 Oct, 2006</time>

Wow.\
This is seriously wonderfull!

Now I\'ll have to install edgy on a machine this weekend :)

---
#### Johan Hedberg - <time datetime="2006-10-22 00:10:50">0 Oct, 2006</time>

I took a look at the code and it looks good. One thing however:

About the \"NFTP\" service identifier, that\'s actually something that
btcond supported but hcid doesn\'t. You\'ll have to give the exact
UUID-128 to hcid instead as\
\"00005005-0000-1000-8000-0002ee000001\" (I hope that\'s correct).

What it\'s about: some Nokia Symbian phones have two OBEX FTP services:
one identified with the normal UUID and another with a Nokia specific
128 bit UUID. The service found behind the normal identifier is very
limited in features on these phones while the other one supports full
OBEX FTP (don\'t ask me why).\

---
#### Wout - <time datetime="2006-10-23 23:17:11">1 Oct, 2006</time>

Thank you man. You\'re awsome\.... I\'ve installed the software
succesfully and everything works. Great\.....

B.t.w. mine gives me the full name after a while\... and it\'s fully
useable in nautilus. (Pretty stable\...)\
I\'f you wan\'t some testers just let me know\....(just say so on your
blog\.... )\
GReat great great\....

---
#### [Andrew Jorgensen](http://andrew.jorgensenfamily.us) - <time datetime="2006-10-24 07:53:10">2 Oct, 2006</time>

Thanks! This is awesome. I\'ve been thinking for some time now, though,
that OBEX != bluetooth.

There are at least four other media commonly (or less commonly) used for
OBEX: USB, IrDA, Serial, and TCP/IP. All of these are supported by
OpenOBEX.

I\'ve been told that IrDA is somewhat harder to deal with but USB should
be pretty easy. Serial might not be worth implementing. TCP/IP, if
supported at all, probably doesn\'t need to be discoverable (unless of
course it\'s advertised through mDNS).

---
#### [Alex Kanavin](http://www.sensi.org/~ak/openobex-usb/) - <time datetime="2006-10-24 21:46:08">2 Oct, 2006</time>

USB should use a different approach: mount it as a filesystem through
FUSE/obexfs. I\'ll check out how it all works

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-10-25 16:30:09">3 Oct, 2006</time>

Wout: yeah. I implemented that a bit after posting this article.

Andrew/Alex: Matthew Garrett has plans to add bluetooth device support
to HAL, which would help here. If I can look up IrDA OBEX and Bluetooth
OBEX devices in the HAL hardware database by some property, then it
should be possible to support both: the only bluetooth specific code is
for listing the paired devices and creating RFCOMM connections.

---
#### clp - <time datetime="2006-10-26 00:36:35">4 Oct, 2006</time>

I get this message in nautilus\...

obex:///\" is not a valid location.

\
what\'s wrong?

How do I enable the gnome-vfs-2.0 modules?

Salu2 clp ;)

---
#### [Andrew Jorgensen](http://andrew.jorgensenfamily.us/) - <time datetime="2006-10-26 02:30:01">4 Oct, 2006</time>

clp: I had the same problem at first. Trouble was that by default things
get installed in /usr/local. Try the following:

./configure \--sysconfdir=/etc \--prefix=/usr

---
#### clp - <time datetime="2006-10-26 17:24:59">4 Oct, 2006</time>

A lot of thanks, Andrew!

\> ./configure \--sysconfdir=/etc \--prefix=/usr

It\'s a great job!

---
#### clp - <time datetime="2006-10-30 05:47:50">1 Oct, 2006</time>

In amd64 architecture I get this problem in oss-gwobex compilation:

autoreconf2.50: running: /usr/bin/autoconf\
configure.ac:11: error: possibly undefined macro: AC\_PROG\_LIBTOOL\
If this token and others are legitimate, please use m4\_pattern\_allow.\
See the Autoconf documentation.\
autoreconf2.50: /usr/bin/autoconf failed with exit status: 1

Salu2 clp ;)

---
#### Onkar Shinde - <time datetime="2006-11-07 06:07:07">2 Nov, 2006</time>

Works really well. I could see name of my phone and a pretty icon. Did
file transfers in both directions without problem.

I have just one question. The autogen script in the vfs module code says
it requires automake1.9. Is this strict dependency?

Also is opebobex \> 1.2. a strict dependency.

Please note that I have not even looked into code. So pardon if my
questions are redundant.

---
#### Hans - <time datetime="2006-11-12 13:24:43">0 Nov, 2006</time>

I followed the instructions above. And obex method works fine until i
try to transfer a file to the bluetooth device (sony ericsson K750i).

The error messages tells me that theres not enough free space on the
receiver (I know theres about 1Gb free, Nautilus says 0byes free).

Someone know how to fix this?

---
#### Onkar Shinde - <time datetime="2006-11-18 10:55:12">6 Nov, 2006</time>

For those who are interested, packages are available for edgy, i386.
Check Edgy+1 section of <https://wiki.ubuntu.com/Bluetooth/TODO>

Hope this helps.

---
