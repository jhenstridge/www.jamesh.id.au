---
title: '29 July 2002'
slug: 29-july-2002
date: 2002-07-30T06:06:46+08:00
---

**linux.conf.au**

The call for papers is almost over. If you want to speak, please send in
your abstracts soon.

**GNOME**

I started writing up some code to add [RPM](http://www.rpm.org/)
support to Nautilus. At the moment, I just have a simple [GNOME
VFS](http://www.advogato.org/proj/GNOME%20VFS/) module that allows you
to see what packages are on the system. You can see a sample of what
it looks like [here](rpmdb-vfs-1.png).  The package sizes represent
the installed size of the package (as reported in the RPM database),
and the modification times are the installation times of the packages.

I still need to write some code so that you can view information about
the package (probably as a nautilus view), and some utilities for
installing and removing packages (these will probably be separate
applications, which should cut down on the problems I ran into when
writing [GnoRPM](http://www.advogato.org/proj/GnoRPM/). When it is
finished, it should be pretty useful.
