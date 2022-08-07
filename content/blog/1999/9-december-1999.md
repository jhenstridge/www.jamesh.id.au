---
title: '9 December 1999'
slug: 9-december-1999
date: 1999-12-10T02:57:45+08:00
---

I got my uni results yesterday. I got good marks in both\
my computing and pure maths majors. I got invitation for\
honours year letters from both the maths and computer\
science departments. I will have to decide where I want to\
do honours. Apparently I got the highest score in the\
computer networks unit, which means I will be getting a\
prize from a company called AlphaWest.

I converted the page setup widget I wrote for dia to use\
GnomePaper and GnomeUnit. After doing a bit more cleanup,\
and implementing the old GnomePaperSelector interface, I\
will commit it to gnome-libs HEAD branch.

Dia now has a bezier connection line. It is a mixture of\
work by Lars Clausen and me. It works fairly well. There\
is a patch for it from Lars to better handle the initial\
drag when placing the object, but I haven\'t got round to\
applying it. Cyrille has a few patches to start doing the\
properties interface. I haven\'t read them yet, and I think\
I will wait till 0.82 is out before applying them\
anyway.

I should really do a bit more work on gnome-python and\
gnorpm. I should probably spend a while bringing\
gnome-python back up to scratch and release a new version.\
As for gnorpm, I have got a bit stuck implementing the\
dependencies code in terms of glibwww. It is quite\
difficult handling the state between callbacks.
