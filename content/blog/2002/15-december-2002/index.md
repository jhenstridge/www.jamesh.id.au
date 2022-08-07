---
title: '15 December 2002'
slug: 15-december-2002
date: 2002-12-15T13:41:33+08:00
---

Haven\'t posed here for a while \...

**PyORBit**

Put out a few releases of PyORBit. Seems to work quite well, although it
still needs some more work. CVS gnome-python is already using it, but I
haven\'t put out any tarballs yet (which I should do \-- it has been too
long since the last releases).

**fontilus**

I started working on another small GNOME package a few weeks ago: a set
of tools to help manage fonts on
[fontconfig](http://www.fontconfig.org/) based GNOME systems (such as
GNOME 2.1.x and Red Hat 8.0). Here are a few screenshots of what it can
do:

-   [List of fonts in icon view](fontilus-thumb-icons.png)
-   [List of fonts in list view](fontilus-thumb-list.png)
-   [Font viewer](fontilus-font-viewer.png)

The thumbnailing only works if you have Nautilus 2.1, but the rest works
on vanila RH8. What the screenshots don\'t show is that the `fonts:///`
folder can also be used to install fonts via drag and drop (it puts the
files in `~/.fonts`, which is in the default fontconfig search path).

Even though I have only been hacking on it for a while, fontilus has
already become fairly popular. There are packages in Mandrake Cooker, RH
Rawhide and Debian Unstable.
