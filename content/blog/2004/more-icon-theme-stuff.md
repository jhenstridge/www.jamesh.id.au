---
title: 'More Icon Theme stuff'
slug: more-icon-theme-stuff
date: 2004-10-05T12:09:41+08:00
---

In an email, [Jonathan](http://jrb.webwynk.net/) pointed out that simply
using `gtk_icon_theme_load_icon()` by itself is not optimal either. If
the user changes their icon theme, you should reload the icon in case it
has changed in the new theme.

This is quite easy to handle correctly though, using the `"changed"`
signal of `GtkIconTheme`:

> `GtkIconTheme *icon_theme = gtk_icon_theme_get_default (); g_signal_connect (icon_theme, "changed", G_CALLBACK (callback), NULL);`

Now `callback()` will be called when the icon theme changes, at which
point you can reload the icon.

What would be nice would be a `GtkImage` constructor that let you pass
in an icon name plus desired size, and handled theme changes for you.
Maybe I\'ll do a patch for this \...
