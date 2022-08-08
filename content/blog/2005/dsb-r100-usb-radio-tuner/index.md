---
title: 'DSB-R100 USB Radio Tuner'
slug: dsb-r100-usb-radio-tuner
date: 2005-10-18T09:26:54+08:00
tags: ['Gnome', 'Ubuntu']
---

Picked up a
[DSB-R100](http://www.dlink.com.au/tech/faq/usb/dsbr100-faq.htm) USB
Radio tuner off EBay recently. I did this partly because I have better
speakers on my computer than on the radio in that room, and partly
because I wanted to play around with timed recordings.

Setting it up was trivial \-- the `dsbr100` driver got loaded
automatically, and a program to tune the radio
([gnomeradio](http://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/)) was
available in the Ubuntu universe repository. I did need to change the
radio device from `/dev/radio` to `/dev/radio0` though.

{{< figure src="gnomeradio.png" width="332" height="155" >}}

One of the issues with the gnomeradio is the UI for tuning the radio.
The following controls in the main window are used for this purpose:

1.  The slider on the left hand side of the window.
2.  The rewind and fast forward buttons (which are actually scan forward
    and backward).
3.  The track backward and forward buttons (which actually move back or
    forward by 0.05MHz).
4.  The presets option menu (which is initially empty).

What you can\'t do from the main window is type in a frequency with the
keyboard. You can type in frequencies directly when entering presets
though, which is nice. These controls could probably be reduced to just
an entry field for the frequency (possibly a spin button), and the
presets option menu. The scanning feature seems most useful in setting
up the presets: create a preset for each radio station that can be tuned
and be done with it.

There are a few other small complaints:

-   The button for turning the radio on or off (the button with a
    speaker on it) doesn\'t change appearance like most other mute
    controls.
-   The recording feature doesn\'t use GStreamer. It\'d be nice if it
    offered the same audio profiles for recording as Sound Juicer and
    other apps.
-   The input selection and volume control should probably also use
    GStreamer, so that they can work with the ALSA mixer.

I haven\'t yet looked into software for doing timed recordings. [Other
people](http://burd.info/gary/2003/07/time-shifting-fm-radio.html) have
though, so I could probably use those scripts as a base.

---
### Comments:
#### [Marcus](http://www.modmeup.net) - <time datetime="2005-10-18 18:39:15">18 Oct, 2005</time>

Very cool.. I remember having one of those years ago, I set it up with a
shoutcast server so that the whole site (a mining operation in
Australia) could get radio.. even underground.I may have to buy another
one I think.. thanks for the reminder :-)

---
#### nate - <time datetime="2005-10-19 00:55:09">19 Oct, 2005</time>

Did you get the recording feature to work? I have used gnomeradio for
years, different hw platforms & different distros, and so far have never
gotten it to function at all.

---
#### Tobias - <time datetime="2005-10-19 05:17:41">19 Oct, 2005</time>

Perhaps you can help with HAL Support for v4l hardware:\
<https://bugs.freedesktop.org/show_bug.cgi?id=3527>

Or Support for v4l radio in rhythmbox:\
<http://bugzilla.gnome.org/show_bug.cgi?id=314160>

Anyway, have a lot of fun.

---
#### James Henstridge - <time datetime="2005-10-19 11:00:38">19 Oct, 2005</time>

nate: I just tried the recording function, and got a silent, mono
44.1KHz wave file. I\'m not sure what the problem is.

---
