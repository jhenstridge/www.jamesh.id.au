---
title: '13 February 2003'
slug: 13-february-2003
date: 2003-02-13T14:56:30+08:00
draft: false
---

[lmjohns3](http://www.advogato.org/person/lmjohns3/): if you use a
locale with right to left text direction, GTK+ will automatically flip
the direction of standard widgets.

This means that if you have a GtkHBox, items added with `pack_start()`
will end up on the right hand side of the box, and ones added with
`pack_end()` on the left (after all, they aren\'t called `pack_left` and
`pack_right`).

To see what happens, try out the \"flipping\" test in the `testgtk`
program included with GTK.
