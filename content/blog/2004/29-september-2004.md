---
title: '29 September 2004'
slug: 29-september-2004
date: 2004-09-29T13:25:58+08:00
tags: ['Gnome']
---

[**Ubuntu**](http://www.ubuntulinux.org/)

Ubuntu seems to have taken off very quickly since the preview release
came out a few weeks ago. In general, people seem to like the small
tweaks we\'ve made to the default Gnome install. Of course, after the
preview came out people found bugs in some of my Gnome patches \...

One of the things we added was the [trash
applet](http://luon.net/~michiels/trashapplet/) on the panel. I made a
fair number of fixes that make the applet fit in with the desktop a bit
better and handle error conditions a bit better.

Probably the biggest fix was adding support for multiple trash
directories. Originally the applet would move files to `~/.Trash` and
didn\'t monitor any other trash directories, which meant that moving to
the trash took longer than necessary on slow volumes and the applet
didn\'t correctly reflect the trash\'s empty state if you used the
\"move to trash\" context menu item in Nautilus.

One of the problems implementing this was that the trash handling in
Gnome is pretty much entirely private to Nautilus. I managed to adapt
the Nautilus code into a small class (about 500 lines) that could
provide an item count for the trash, notification of changes to the item
count, and the ability to empty the trash. A lot of the complexity in
this code is to handle plugging and and unplugging of removable volumes.
It\'d be nice if this kind of code was available in gnome-vfs or
something though.

**Icon Theme APIs**

While working on various Ubuntu fixes, I found an error that seems to be
quite common in various bits of the desktop. It goes something like
this:

1.  Find the image file for an icon at size *n* using
    `gnome_icon_theme_lookup_icon()` or `gtk_icon_theme_lookup_icon()`.
2.  Create a `GdkPixbuf` from the image file using
    `gdk_pixbuf_new_from_file()`.
3.  Use the pixbuf as an *n*x*n* icon.

The first problem with this is that `gtk_icon_theme_lookup_icon()` is
not guaranteed to return an image at the desired size. This is quite
obvious when you consider that you can pass in an arbitrary size to the
lookup function, but the icon theme will only contain a finite number of
sizes. However, if you ask for a common sized icon and the icon theme
contains that size image, it might appear that the function will always
return an image file of the requested size. The fix is to check the size
of the loaded pixbuf and scale it if it is of the wrong dimensions.

The second problem is to do with SVG image files. They can be rendered
at arbitrary sizes, but `gdk_pixbuf_new_from_file()` doesn\'t tell the
loader backend what size is actually wanted. This means that the SVG
will be rendered at whatever size is listed in the file itself, which
could be very large or very small. To avoid having to resize the SVG
image after rendering it (which could be slow), you can use the
`gdk_pixbuf_new_from_file_at_size()` routine (new in GTK 2.4) which
passes the desired size to the backend so that ones like the SVG backend
can render at an appropriate size. This function will return a pixbuf
that fits into the bounding height/width you pass to it, and will
perform scaling if the backend can\'t load the image at the requested
size.

If this sounds complicated, there is an easier way. You can just use
`gtk_icon_theme_load_icon()`, which will lookup the image, and load it
at the desired size all in one go. I guess there aren\'t many people
using it because there wasn\'t an equivalent in the older
`GnomeIconTheme` API.
