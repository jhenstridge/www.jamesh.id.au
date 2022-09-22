---
title: '8 December 2000'
slug: 8-december-2000
date: 2000-12-09T05:50:56+08:00
---

Have been hacking on pygtk recently, and a small amount on glib HEAD
and framebuffer gtk (which is looking really promising). I did up the
first cut at allowing arbitrary GtkTreeModels to be defined in python
code. It leaks badly, and it will probably be near impossible to fix
correctly `:(`.

The glib patch was to add some convenience functions for the GSignal
code, as it is so difficult to use the existing functions people are
still creating GtkObjects because of the gtksignal compatibility
wrappers. Still waiting on feedback from Tim about it

Yesterday night [alex](http://www.advogato.org/person/alex/) asked me
to try compiling pygtk with the framebuffer port of GTK, which he is
working on. After adding a single missing function to the framebuffer
gdk backend, pygtk compiled with no source modifications, which was
good. I was having trouble with the "ms" serial mouse driver in GtkFB
and my mouse. I put together a patch to make finding the start of
mouse packets a little smarter, and to fix up the mouse button
handling for that driver. The level of functionality in GtkFB is quite
impressive.

Last Sunday, I went to the reconciliation walk in the city, which went
quite well. Lots of people turned up.  Also, on the way there I
noticed a big banner on the old Swan Brewery (which has been a sore
point, because it was an Aboriginal sacred site) saying "sorry". I
don't know if anything different will happen with the development at
that site though.
