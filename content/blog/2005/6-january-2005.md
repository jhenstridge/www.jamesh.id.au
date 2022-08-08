---
title: '6 January 2005'
slug: 6-january-2005
date: 2005-01-07T05:13:32+08:00
tags: ['Bazaar', 'Gnome']
---

**Travels**

I\'ve put some of the photos from my [trip to
Mataró](/photos/2004-12-mataro.md), and the [short stop over in Japan
on the way back](/photos/2004-12-narita.md). The Mataró set includes a
fair number taken around La Sagrida Familia, and the Japan set is
mostly of things around the Naritasan temple (I didn\'t have enough
time to get into Tokyo).

**Multi-head**

A few months back, I got a second monitor for my computer and configured
it in a Xinerama-style setup (I\'m actually using the `MergedFB` feature
of the radeon driver, but it looks like Xinerama to X clients). Overall
it has been pretty nice, but there are a few things that Gnome could do
a bit nicer in the setup:

-   Backgrounds get stretched over both screens. The
    [Ubuntu](http://www.ubuntulinux.org/) backgrounds already looked a
    bit weird at a 5:4 aspect ratio. They look even worse at a 5:2 ratio
    `:-)`. Ideally the background image would be repeated on each
    monitor of the virtual screen. Some details are available as [bug
    147808](http://bugzilla.gnome.org/show_bug.cgi?id=147808), but it
    looks like the fix would be in `EelBackground` code.
-   Most parts of the desktop treat the monitors as independent (which
    is good, since most people pick Xinerama over classic X multi-screen
    so that dragging windows between monitors works, rather than to
    build video walls), but there is a few bits that don\'t. One of the
    more obvious ones is in Metacity: the alt+tab dialog pops up centred
    on the monitor where mouse currently resides, but it cycles through
    all the windows visible on the virtual screen. This is a bit
    confusing, since it looks like it will be a monitor-local operation
    based on the position of the dialog (however, if it was
    monitor-local I\'m not sure how you\'d switch focus to a window on
    the other monitor with only the keyboard \...).

**Bazaar**

The new merge command in `baz` is quite nice. This provides support for
merging in ways that `tla` can\'t. One of the limitations of
`star-merge` is that it can get confused if you don\'t strictly follow
the star topology when merging. That is, you should only merge to/from
the person you branched from, and people who branched from you. If
siblings merge for instance, it can cause problems with subsequent
merges.

The new `merge` command doesn\'t suffer from that problem, and allows
you to merge from anyone. Of course, if you break the star topology,
people wanting to merge from you will either need to be using Bazaar, or
ask for you to merge from them first (so that the `star-merge` algorithm
merges the right changes).
