---
title: 'PyORBit'
slug: pyorbit
date: 2002-10-13T02:52:18+08:00
draft: false
---

The client side of PyORBit should be pretty usable now. Marshalling and
demarshalling of pretty much all types is working well. I ported most of
`test/everything/client.c` to Python using PyORBit, which helped test
the a lot of the code.

I support pretty much all of the complex types pretty well (structures,
unions, sequences, arrays, exceptions, anys).

I fixed the weird typelib bug ([bug
94513](http://bugzilla.gnome.org/show_bug.cgi?id=94513)), and checked
the fix into both `HEAD` and `gnome-2-0` branches of ORBit2 (haven\'t
had a release yet though). I need to look at porting the fix for [bug
93928](http://bugzilla.gnome.org/show_bug.cgi?id=93928) back to the
`gnome-2-0` branch. I ran into some other bugs while working on the
union support: [bug
95581](http://bugzilla.gnome.org/show_bug.cgi?id=95581) and [bug
95591](http://bugzilla.gnome.org/show_bug.cgi?id=95591). Hopefully I can
get both of these resolved and a new ORBit2-2.4.x release put out.

As the client side of things is mostly working, I am tossing up on
whether to port gnome-python over to using it. I should probably wait
for a tarball release of ORBit2 though \...
