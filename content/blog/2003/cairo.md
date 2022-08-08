---
title: 'Cairo'
slug: cairo
date: 2003-09-24T07:35:39+08:00
---

Did some more hacking on my [Python bindings for
Cairo](http://cvs.freedesktop.org/cgi-bin/cvsweb/cairo/python-cairo/).
They are now in the new [freedesktop.org](http://www.freedesktop.org/)
CVS server.

I added a `cairo.gtk.set_target_drawable()` function that sets a Cairo
context to draw on an arbitrary GdkDrawable, taking into account the
temporary pixmaps used by GTK for its double buffering and the expanded
virtual 32-bit coordinate space (based on some of Carl\'s code in
grrobots).

I ported a few of the Cairo demos to Python/GTK for testing purposes,
and they all seem to be working fairly well. The exception is the
knockout demo, which doesn\'t seem to be redrawing properly (a bad
interaction between Cairo and GTK\'s double buffering, I guess).
