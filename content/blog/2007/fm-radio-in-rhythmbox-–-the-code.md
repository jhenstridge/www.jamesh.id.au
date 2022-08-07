---
title: 'FM Radio in Rhythmbox – The Code'
slug: fm-radio-in-rhythmbox-–-the-code
date: 2007-05-21T21:08:41+08:00
draft: false
tags: ['Bazaar', 'Gnome', 'Ubuntu']
---

[Previously](http://blogs.gnome.org/view/jamesh/2007/05/04/0), I posted
about the FM radio plugin I was working on. I just posted the code to
[bug
168735](http://bugzilla.gnome.org/show_bug.cgi?id=168735#c13 "Support for v4l radio in rhythmbox").
A few notes about the implementation:

-   The code only supports [Video4Linux
    2](http://www.linuxtv.org/downloads/video4linux/API/V4L2_API/) radio
    tuners (since that's the interface my device supports, and the V4L1
    compatibility layer doesn't work for it). It should be possible to
    port it support both protocols if someone is interested.
-   It does not pass the audio through the GStreamer pipeline. Instead,
    you need to configure your mixer settings to pass the audio through
    (e.g. unmute the Line-in source and set the volume appropriately).
    It plugs in a GStreamer source that generates silence to work with
    the rest of the Rhythmbox infrastructure. This does mean that the
    volume control and visualisations won't work
-   No properties dialog yet. If you want to set titles on the stations,
    you'll need to edit `rhythmdb.xml` directly at the moment.
-   The code assumes that the radio device is `/dev/radio0`.

Other than that, it all works quite well (I\'ve been using it for the
last few weeks).

**Development**

I developed this plugin in [Bazaar](http://bazaar-vcs.org/) using
[Jelmer](http://jelmer.vernstok.nl/blog/)\'s
[bzr-svn](http://bazaar-vcs.org/BzrForeignBranches/Subversion) plugin.
It produces a repeatable import, so I should be able to cross merge with
anyone else producing branches with it.

It is also possible to use bzr-svn to merge Bazaar branches back into
the original Subversion repository through the use of a lightweight
checkout.

For anyone wanting to play with my Bazaar branch, it is [published in
Launchpad](https://code.launchpad.net/~jamesh/rhythmbox/fmradio) and can
be grabbed with the following command:

    bzr branch lp:~jamesh/rhythmbox/fmradio rhythmbox

---
### Comments:
#### dave - <time datetime="2007-05-21 22:58:33">1 May, 2007</time>

Does this (and the other projects based on v4l) give you access to the
radio stations broadcast alongside television channels via DVB-T or
DVB-S (Freeview and Freesat in the UK)?

---
#### bronxoni - <time datetime="2007-05-21 23:34:18">1 May, 2007</time>

Please \*DO NOT\* develop the V4L1 support. The reason is simple: V4L1
is deprecated and getting seriously outdated. The problem is that some
people are still developing new drivers using V4L1, which is harder and
worse to work with. They will never stop that idiocy before V4L1 support
starts seriously get dropped from all the applications.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-05-22 01:05:16">2 May, 2007</time>

dave: I have no idea. I don\'t have a DVB-T tuner card in my desktop
(the DSB-R100 only does FM radio).

bronxoni: I have no immediate plans to implement V4L1 support \-- I am
merely pointing out that it wouldn\'t be too difficult to support both
APIs transparently. I wrote my plugin to the V4L2 API because that\'s
the interface my hardware supports on Ubuntu Feisty.

---
