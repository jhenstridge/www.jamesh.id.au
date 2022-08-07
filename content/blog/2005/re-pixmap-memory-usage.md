---
title: 'Re: Pixmap Memory Usage'
slug: re-pixmap-memory-usage
date: 2005-12-08T06:38:53+08:00
draft: false
tags: ['Gnome']
---

[Glynn](http://www.gnome.org/~gman/blog/07122005-1): I suspect that the
Pixmap memory usage has something to do with image rendering rather than
applets in particular doing something stupid. Notice that most other GTK
programs seem to be using similar amounts of pixmap memory.

To help test this hypothesis, I used the following Python program:

    import gobject, gtk
    win = gtk.Window()
    win.set_title('Test')
    win.connect('destroy', lambda w: gtk.main_quit())
    def add_image():
        img = gtk.image_new_from_stock(gtk.STOCK_CLOSE,
                                       gtk.ICON_SIZE_BUTTON)
        win.add(img)
        img.show()
    gobject.timeout_add(30000, add_image)
    win.show()
    gtk.main()

According to `xrestop`, this program has low pixmap memory usage when
it starts, but jumps up to similar levels to the other apps after 30
seconds.

**Update:** of course, this issue [has already been
debugged](http://mail.gnome.org/archives/desktop-devel-list/2005-May/msg00052.html)
by [markmc](http://blogs.gnome.org/markmc). It is the SHM segment
allocated for drawing pixbufs.
