---
title: 'intltool and po/LINGUAS'
slug: intltool-and-polinguas
date: 2006-04-15T08:41:52+08:00
draft: false
tags: ['Gnome']
---

[Rodney](http://primates.ximian.com/~dobey/?date=2006-04-12): my
suggestions for intltool were not intended as an attack. I just don\'t
really see much benefit in intltool providing its own
`po/Makefile.in.in` file.

The primary difference between the intltool `po/Makefile.in.in` and the
version provided by gettext or glib is that it calls `intltool-update`
rather than `xgettext` to update the PO template, so that strings get
correctly extracted from files types like desktop entries, Bonobo
component registration files, or various other XML files.

The current method intltool uses to get `intltool-update` called
(providing its own `po/Makefile.in.in`) is a lot better than the
previous method (maintaining patches for the `po/Makefile.in.in` files
from various versions of gettext and then deciding which one to apply),
however it can make it difficult to take advantage of new gettext
features (the `po/LINGUAS` file being the most recent example). If it
was possible for `intltool-update` to be called without any modification
to the `po/Makefile.in.in` file that gettext installs then this sort of
problem wouldn\'t occur.

The standard `po/Makefile.in.in` uses the makefile variable
`$(XGETTEXT)` as the program to extract translations for the PO
template. If intltool had a program (or a mode for one of the existing
programs) that was command line argument compatible with xgettext, then
all that would be necessary would be to redefine `$(XGETTEXT)` to the
appropriate value. Since `$(XGETTEXT)` is set through a simple autoconf
substitution, this should be very easy to do from intltool\'s M4
autoconf macro.
