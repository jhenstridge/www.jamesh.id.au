---
title: 'FM Radio Tuners in Feisty'
slug: fm-radio-tuners-in-feisty
date: 2007-04-17T15:32:44+08:00
tags: ['Gnome', 'Ubuntu']
---

I upgraded to Feisty about a month or so ago, and it has been a nice
improvement so far. One regression I noticed though was that my USB FM
radio tuner had stopped working (or at least,
[Gnomeradio](http://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/) could no
longer tune it).

It turns out that some time between the kernel release found in Edgy and
the one found in Feisty, the `dsbr100` driver had been upgraded from the
[Video4Linux 1
API](http://www.linuxtv.org/downloads/video4linux/API/V4L1_API.html) to
[Video4Linux
2](http://www.linuxtv.org/downloads/video4linux/API/V4L2_API). Now the
driver nominally supports the V4L1 ioctls through the `v4l1_compat`, but
it doesn\'t seem to implement enough V4L2 ioctls to make it usable (the
`VIDIOCGAUDIO` ioctl fails).

To work around this, I ported the tuner code in Gnomeradio over to V4L2.
The patch can be found attached to [bug
429005](http://bugzilla.gnome.org/show_bug.cgi?id=429005 "Port radio tuner code over to the Video4Linux 2 API").
I don\'t know if this patch will go in as is though, since it only works
for drivers supporting V4L2. Perhaps it\'d be worth supporting both
APIs, using V4L2 if both are supported.

---
### Comments:
#### Max - <time datetime="2007-04-17 18:33:00">17 Apr, 2007</time>

Argg, we need V4L and V4L2 Support in Gstreamer\...

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-04-17 19:21:17">17 Apr, 2007</time>

Max: there are v4lsrc and v4l2src elements in Gstreamer already.
However, they don\'t really handle V4L/V4l2 radio devices, where you\'ve
only got a tuner and no audio/video inputs.

---
#### Xav - <time datetime="2007-04-17 23:33:22">17 Apr, 2007</time>

I think v4l device are automatically handled as v4l2 by the kernel (but
I may be mistaken).

---
#### n8 - <time datetime="2007-04-18 06:13:28">18 Apr, 2007</time>

Out of raw, unabashed curiosity \-- which USB FM radio tuner do you use?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-04-18 10:35:13">18 Apr, 2007</time>

n8: it is a D-Link DSB-R100 USB tuner. It does all the basic things, but
doesn\'t report signal strength (which means that apps can\'t scan
forward for stations).

---
#### gizmo - <time datetime="2007-04-22 06:41:21">22 Apr, 2007</time>

I use avermedia GO 007 tv tuner card\
I could use gnomeradio on dapper, but I cant use it on Fiesty\...

can anyone suggest me anything?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-04-24 23:59:56">24 Apr, 2007</time>

gizmo: have you tried the patch attached to the bug report I mentioned
in the main article? The gnomeradio in feisty is incapable of tuning my
radio hardware, so may be incapable of tuning yours too.

---
