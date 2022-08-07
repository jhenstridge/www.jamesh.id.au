---
title: '20 October 2004'
slug: 20-october-2004
date: 2004-10-20T08:28:17+08:00
draft: false
tags: ['Gnome', 'JHBuild']
---

**Even More Icon Theme Stuff**

To make it a bit easier to correctly display themed icons, I added
support to `GtkImage`, so that it is as easy as calling
`gtk_image_new_from_icon_name()` or `gtk_image_set_from_icon_name()`.
The patch is attached to [bug
\#155688](http://bugzilla.gnome.org/show_bug.cgi?id=155688).

This code takes care of theme changes so the application developer
doesn\'t need to. Once this is in, it should be trivial to add themed
icon support to various other widgets that use GtkImage (such as
GtkAbout and GtkToolItem).

**JHBuild**

I started work on some [extended documentation for
JHBuild](http://cvs.gnome.org/viewcvs/jhbuild/doc/jhbuild.xml?view=markup).
At the moment, this just includes some information on setting it up and
basic use. I\'ll extend it to hold a reference to all JHBuild commands,
some documentation on the module set file format and some frequently
asked questions.

It would be good to include some information on setting up JHBuild\'s
tinderbox mode ([like Luis
has](http://gnome-build.ximian.com/tinderbox/LATEST/)). Getting a few
more tinderboxes running for Gnome on other platforms such Solaris/SPARC
would be really useful \-- Luis\'s build logs have already helped track
down a few build failures, so having build information for a few more
platforms would be very useful.

**New Computer**

I just got the last components for my new computer (an Athlon 64
system). It is a fair bit faster than the laptop I\'ve been doing most
of the development on, so should be quite nice once it is all set up.

It is amazing how much hardware has improved and gone down in price. The
[motherboard](http://www.asus.com.au/products/mb/socket939/a8v-d/overview.htm)
alone is packed with features I wouldn\'t have expected for something
costing AU\$220:

-   Gigabit ethernet
-   An 802.11g wireless card (PCI)
-   An extra Promise SATA chip, bringing the number of SATA connectors
    up to 4, and the IDE connectors to 3.
-   Firewire
-   SPDIF output (both electrical and optical).
-   6 headphone-style jacks on the back, so you can get 6 channel audio
    output without losing your line in and microphone jacks.

I also got a
[Raptor](http://www.westerndigital.com/en/products/Products.asp?DriveID=65)
hard drive for the system. These drives seem to have up to twice the
performance of most 7200rpm desktop drives, and make a big difference to
the overall performance of the system.

It should be a nice system once I finish building it. Also, since it is
an x86-64 system, it effectively provides two architectures to test
stuff on.
