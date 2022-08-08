---
title: 'PyGTK'
slug: pygtk
date: 2003-09-03T11:12:21+08:00
---

Finally got version 2.0 of PyGTK, PyORBit and Gnome-Python out. I sent
the announcements a bit further than usual this time
(gnome-announce-list, python-announce, etc). Already, it is in
[Debian](http://packages.debian.org/unstable/python/python-gtk2.html),
Mandrake Cooker and there is a [Win32
installer](http://www.pcpm.ucl.ac.be/~gustin/win32_ports/). PyGTK is
also buildable/runnable on MacOS X, provided that you have an X server
installed (such as [Apple\'s one](http://www.apple.com/macosx/x11/)). If
you have been holding off from looking at PyGTK 1.99.x, you should
definitely take a look now.

This release has been a long time in the making:

-   595 revisions to the ChangeLog (out of 670 revisions on the main
    branch in CVS) since branching the 1.2 bindings.
-   Over 5000 lines in the ChangeLog.
-   Over 3 years since branching.

The result is a binding that is a lot nicer to use, and will be much
easier to maintain. It does demonstrate that you lose a lot of time when
you decide to do a rewrite. At the same time, I don\'t know if it would
have been feasible to get from the old 1.2 bindings to where we are now
in small incremental steps. I am very happy with what we have now
though.

Updating the binding for GTK 2.2 (and GTK 2.4 after that) is going to be
a lot easier and quicker. All the infrastructure is in place, so it is a
simple matter of adding the new APIs. The 2.0 to 2.2 delta is much
smaller than the 1.2 to 2.0 delta.

It is a similar story for the Gnome bindings, although we will probably
skip to Gnome 2.4, since it is almost out and contains some new APIs
that are interesting from a language bindings perspective. I won\'t need
to rewrite the CORBA bindings this time either `:)`.
