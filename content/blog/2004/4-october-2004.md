---
title: '4 October 2004'
slug: 4-october-2004
date: 2004-10-04T14:37:00+08:00
draft: false
tags: ['Gnome', 'JHBuild']
---

**Icon Theme APIs (continued)**

Of course, after recommending that people use
`gtk_icon_theme_load_icon()` to perform the icon load and scale the icon
for you, [Ross](http://www.burtonini.com/) manages to [find a
bug](http://bugzilla.gnome.org/show_bug.cgi?id=154142) in that function.

If the icon is not found in the icon theme, but instead in the legacy
`$prefix/share/pixmaps` directory, then `gtk_icon_theme_load_icon()`
will not scale the image down (it will scale them up if necessary
though).

**jhbuild**

Jhbuild now includes a notification icon when running in the default
terminal mode. The code is loosely based on
[Davyd\'s](http://www.livejournal.com/users/davyd/114890.html) patch,
but instead uses Zenity\'s notification icon support. If you have the
HEAD branch of Zenity installed, it should display without any further
configuration. Some of the icons are a little difficult to tell apart at
notification icon sizes, so it would be good to update some of them.

**DVDs**

The [Double the Fist](http://www.abc.net.au/doublethefist/)
[DVD](http://shop.abc.net.au/browse/product.asp?productid=727036&promoid=141)
is great. I hope they do another season, and release the second half of
the first season on DVD. It is a satire on extreme sports and reality TV
shows among other things, and is worth watching. Apparently it was
originally shown on ABC digital, so not many people saw it during its
original screening (digital television is fairly new in Australia, and
equipment is still fairly expensive).
