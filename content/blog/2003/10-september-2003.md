---
title: '10 September 2003'
slug: 10-september-2003
date: 2003-09-10T10:21:11+08:00
draft: false
---

**Cairo**

Started on some [Cairo](http://www.cairographics.org/) bindings for
[Python](http://www.python.org/). At the moment, they are fairly
immature, but shouldn\'t require too much more work before I can test
them.

Differing a bit from the C API, I\'ve made the `cairo_matrix_t` type
immutable from Python. That is, all the operations that modify a
cairo\_matrix\_t have been wrapped in such a way that they return a new
matrix rather than modifying the old one.

I also set things up so that `cairo_status()` calls are made
automatically after operations, and an exception rasied if appropriate.

The next thing to do is to set up some shim code to make the binding
usable in conjunction with PyGTK. This will probably just be a bit of
code in an extension that lets you create a `cairo.Surface` from a
`GdkDrawable` or `GdkPixbuf` (in 24-bit RGB format \-- since GdkPixbuf
uses RGBA and Cairo uses ARGB, it doesn\'t look trivial to render into
an RGBA pixbuf).

Talked with [keithp](http://www.keithp.com/) on IRC a bit about the
extension, and some changes to the Cairo API that would make the
extension\'s life a bit easier. Will follow it up on the list.

**Mail Viruses**

As predicted by the anti-virus firms, it looks like Sobig.F has stopped
propagating (based on the sudden drop in virus bounce messages I have
been receiving). About time.
