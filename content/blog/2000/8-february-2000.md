---
title: '8 February 2000'
slug: 8-february-2000
date: 2000-02-09T02:38:19+08:00
---

I hate the heat at this time of year. I got up to around
40 degrees celcius yesterday.

The properties code in dia is working a bit. I switched
the flowchart box object over to using properties, and it
seems to be working fine. I also added properties code to
the group object. You can select two flowchart boxes, group
them and set both their properties at once. There is still
a bit of work to be done w.r.t. undo with the group object
\-- I think I will have to implement a composite ObjectChange
to handle that. It will also be necessary to add change
notification to the group properties dialog so that we only
set the properties the user changes (this might be a good
thing in any case).

I will probably add code to make saving an object a one
line operation with the properties code. Loading should be
just/almost as easy. This should make it easier to write
new objects in C. Cyrille is looking at writing some
convenience routines for writing the property set/get
methods.
