---
title: '27 January 2002'
slug: 27-january-2002
date: 2002-01-28T04:00:39+08:00
---

**Skyshow**

Went to the Australia Day fireworks on Saturday night. I\
cycled into the city to see them, which was worth it (didn\'t\
get stuck in a traffic jam \-- just had to dodge pedestrians\
on the way home). The fireworks looked so much better in\
the city (I went just a little past the narrows bridge).\
There were fireworks being let off the tops of the buildings\
in the city, off the narrows bridge, and off the barges in\
the middle of the river. At one stage, some small\
tough-ducks were driving past about 50 metres away and\
letting off some smaller fireworks. One of the embers from\
these smaller fireworks landed about 2 metres away from me!\
(on the esky belonging to someone sitting nearby).

**Sony NEWS**

I have been looking at reviving an old Sony NEWS NWS-1580\
workstation. This is from a line of 68030 based unix\
workstations made by sony in the early 90\'s. It had been\
left off for about 5 years, so wouldn\'t boot at all.\
Apparently the problem was with the battery on the NVRAM\
chip, so I will try and get a replacement for it (its an\
MK48T02B-25 chip, which was also used in a number of Sun\
boxes). While I had the system open, I decided to take a\
few photos of its insides:

> <http://www.jamesh.id.au/images/nws-1580/>

While searching for information, I ran accross the [NetBSD/news68k\
FAQ](http://www.netbsd.org/Ports/news68k/faq.html), which gave a button
combo to press to boot a system\
with a discharged NVRAM battery, or new NVRAM chip. Using\
that combo, I was able to get the system to boot NEWS-OS 3.3\
(a BSD-4.3 derivative).

Once the system is running nicely, I might look at\
transfering the OS off the 180MB disk onto a spare 2GB SCSI\
disk I have (provided I can find the installation tape). I\
could probably fit two 3.5\" disks into the space the current\
5.25\" disk takes up, which would mean I could put NetBSD on\
it too. I can also fit in another 8MB of RAM, which should\
be helpful (it takes standard 8 or 9 chip 30pin SIMMs). I\
will also look for a AUI -\> 10Base-T tranceiver, so I can\
hook the machine up to the network (6 COMM ports can only\
get you so far \...).

**Python**

On the PyGTK development side, we now have bonobo\
bindings in CVS, using
[jdahlin](http://www.advogato.org/person/zilch)\'s\
orbit-python bindings for ORBit2. We now have support for\
libbonobo, libbonoboui, bonobo-activation, nautilus views\
and panel applets (most of this work is thanks to jdahlin).

I have also been looking at doing some automatic\
signal/property documentation for GObject wrappers. Rather\
than calculating all this documentation up front, I decided\
to use the cool new descriptor support in Python 2.2. This\
is essentially a generalisation of the rule that maps\
functions in a class dictionary to methods on instances.\
Rather than this being a special case in 2.2, functions\
implement a tp\_descr\_get() function, which gets called\
asking the function object to return itself in the context\
of the instance. This generalisation has made it trivial\
for support for static methods, class methods and properties\
(objects with setter/getter functions) to be added to the\
language. I used this for my automatic documentation hack.\
I set \_\_doc\_\_ in the class dictionary to a special object,\
which implements the tp\_descr\_get() slot. The\
tp\_descr\_get() slot looks up the information when\
instance.\_\_doc\_\_ or class.\_\_doc\_\_ is requested and returns\
it.

This worked great for the instance.\_\_doc\_\_ case, but\
class.\_\_doc\_\_ was always returning None. On further\
investigation, I found out that this was caused by the\
type.\_\_doc\_\_ property descriptor (\"type\" is now a new style\
class, rather than just a function for getting the type of\
an object. It serves as the standard metaclass), which took\
precedence. I have a patch for python now that gets rid of\
the property and makes \_\_doc\_\_ on new style classes work\
more like old style classes (and lets you have unicode doc\
strings as well).

The upshoot of this is that typing help(\'gtk.Widget\')\
lists all the signals and properties of gtk.Widget (provided\
my patch is applied).

**linux.conf.au**

I am going to [l.c.a](http://linux.conf.au/)\
next week, which should be a lot of fun. Looking forward to\
meeting everyone there (including
[gman](http://www.advogato.org/person/gman/) and\
[malcolm](http://www.advogato.org/person/malcolm/)). Looks like I will
be fixing up\
my grandmother\'s Windows XP box while I am over there as\
well.

**GUAD3C**

I submitted a talk proposal for [GUADEC 3](http://www.guadec.org), so it
looks like\
I will have to write up the paper. The talk will be on\
writing GTK 2.0 and GNOME 2.0 applications with Python.\
Looking forward to a free trip to Spain `:)`.
