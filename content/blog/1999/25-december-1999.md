---
title: '25 December 1999'
slug: 25-december-1999
date: 1999-12-26T03:56:19+08:00
---

I made another release of [Dia](http://www.lysator.liu.se/~alla/dia/).
This
one should fix the bugs people reported just after the 0.82
release. You can now copy/paste image and bezier objects
without dia crashing. I also added a new export dialog
modeled after gimp\'s save dialog. This also allows me to
separate off export filters to plugins, which is good.

I have included a partially complete CGM filter with the
new release. It does everything except beziers at the
moment. There is a polybezier element in CGM v3, but I have
not had much luck finding docs for it. I don\'t even know if
it is meant to be a closed, filled region or just a
line.

Some more work on gnorpm. It almost compiles again. I
just need to finish off converting the web find window to
the new API and then I can start testing it. After that I
should see what changes are necessary to get it compiling
with RH6.1 and make sure it doesn\'t crash in that setup.
Then I can go and start cleaning out all the bug reports.
Is there any record for the largest number of merged bug
reports closed in one go? It certainly feels like I shoulf
be in the running :)
