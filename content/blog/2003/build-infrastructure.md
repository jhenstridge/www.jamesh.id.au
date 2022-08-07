---
title: 'Build Infrastructure'
slug: build-infrastructure
date: 2003-03-01T15:08:27+08:00
draft: false
---

For the past few weeks, I have been working on improving the
[Gnome](http://www.gnome.org/) build infrastructure. It is something
that we have needed to do for a long time. Most of Gnome is still using
automake-1.4 because they rely on bugs that have since been fixed, and
don\'t handle the readonly sourcdir builds that \"make distcheck\" does
with newer automakes.

So far I have been working on updating the various build tools that
Gnome uses to reduce the amount of work needed to update a package\'s
build infrastructure. So far, I have updated the gnome-common package,
removing most of the macros it contained and doing significant updates
to the shared `autogen.sh` script, and gtk-doc (adding code to separate
out the common section of the docs makefiles everyone is using).

To test things out, I recently ported glib over to using Automake 1.7.
The patch is currently in its second revision, and waiting for another
review. Afterwards, I might look at doing a bit of documentation on how
to update a package \-- I don\'t intend to do the conversion for every
package in CVS \...
