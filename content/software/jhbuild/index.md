---
title: "JHBuild"
date: 2006-07-07T00:00:00+08:00
---

JHBuild is a build script for building [GNOME](https://www.gnome.org/)
from CVS.  Unlike some build scripts, jhbuild makes use of dependency
information, so it will only build what is needed to build the
packages you want.

<!--more-->

JHBuild is available from [GNOME CVS](http://cvs.gnome.org/).  To get
started, you will need to check it out:

    $ mkdir -p ~/cvs/gnome2
    $ cd ~/cvs/gnome2
    $ cvs -d :pserver:anonymous@anoncvs.gnome.org:/cvs/gnome login
    Logging in to :pserver:anonymous@anoncvs.gnome.org:/cvs/gnome
    CVS password:
    $ cvs -d :pserver:anonymous@anoncvs.gnome.org:/cvs/gnome get jhbuild
    ...

If you have a Gnome CVS account, use the appropriate cvs root.  From
that point, you can follow the instructions in the
[README](https://gitlab.gnome.org/GNOME/jhbuild/blob/master/README)
file.
