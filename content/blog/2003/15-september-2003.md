---
title: '15 September 2003'
slug: 15-september-2003
date: 2003-09-15T15:59:22+08:00
draft: false
---

**PyCairo**

Been discussing the bindings on the Cairo mailing list. I\'ll probably
be merging my bindings with Maarten\'s ones.

I also brought up a few changes that would make it easier to write
robust language bindings. Since the API is fairly new, the changes will
probably go in.

**PyGTK**

LWN covered [the pygtk 2.0.0 release](http://lwn.net/Articles/48114/).
2.0.0 is also in
[RawHide](http://www.rpmfind.net//linux/RPM/rawhide/1.0/i386/RedHat/RPMS/pygtk2-2.0.0-1.i386.html)
too, so it looks like it should be a usable baseline in the near future.

In CVS, the move on to GTK 2.2 APIs is under way. It is still necessary
to test them, and add a few custom overrides, but things are looking
fairly good. The wait for 2.2.0 shouldn\'t be anywhere near as long as
the 2.0.0 dev cycle `:)`
