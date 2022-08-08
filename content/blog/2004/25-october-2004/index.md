---
title: '25 October 2004'
slug: 25-october-2004
date: 2004-10-26T04:04:06+08:00
tags: ['Gnome']
---

**Drive Mount Applet**

The new drive mount applet is now checked into the HEAD branch of
gnome-applets, so will be in Gnome 2.10. There are a few things left to
do, such as making it possible to open the file manager as well as
unmounting/ejecting it. I did up a
[screenshot](drive-mount-applet.png)
showing what it looks like as an applet.

{{< figure src="drive-mount-applet.png" width="200" height="240" >}}

**Libtool**

Finally managed to reproduce a particular libtool bug that people have
reported on and off. It does show why some people decide that `.la`
files are evil, since it doesn\'t occur when people delete those files
\...

A reduced test case can be found
[here](http://bugzilla.gnome.org/attachment.cgi?id=33052&action=view).
The problem occurs when you have multiple copies of a library in your
linker library search path with associated `.la` files. In the test
case, there are the following libraries:

-   `libfoo.so` and `libfoo.la` in the directory `/A`. This is the
    library we want to link to.
-   `libfoo.so` and `libfoo.la` in the directory `/B`. We don\'t want to
    link to this one, because it is old.
-   `libbar.so` and `libbar.la` in the directory `/B`.

Let\'s say I then try to link an app that needs `libbar` and the new
version of `libfoo`, and happen to use the following link line:

    libtool --mode=link gcc -o main main.c -lbar -L/A -L/B -lfoo

In the absense of libtool, this would result in us linking against
`/B/libbar.so` and `/A/libfoo.so` (since `/A` comes before `/B` in the
search path).

However, libtool ends up doing something quite different. When it sees
`-lbar`, it notices that there is a `libbar.la` in `/B`, expands that
argument to the full path name of the actual library (`/B/libbar.so`),
*and prepends `/B` to the library search path*. This means that when
it gets round to processing `-lfoo`, it finds `/B/libfoo.la` instead
of `/A/libfoo.la`, and links to the wrong library.

If this sounds like an obscure bug, note that it also happens if we
replace `/B` with `/usr/lib`. In this case, we don\'t even need the
`-L/usr/lib` argument. So the following command results in linking
with `/usr/lib/libfoo.so` instead of `/A/libfoo.so`:

    libtool --mode=link gcc -o main main.c -lbar -L/A -lfoo

This sort of situation is quite common when trying to build some
software into a separate prefix that is also provided by the OS, when
you are relying on a few libraries installed in `/usr/lib` with .la
files.

After putting together the test case I tested it out in the latest
development release (1.9f), and it appears that the problem has been
fixed. Given that the libtool developers are so close to a 2.0
release, I don\'t know whether they would bother putting out another
1.5.x release to fix the problem.

So if you do run into the problem, some possible solutions are:

1.  Upgrade to libtool-1.9f. I\'m not sure how good an idea this is
    if you are producing tarballs, since they will be packaged with
    the development release too.
2.  Remove all the `.la` files in `/usr/lib`. Some distributors seem
    to take this route (eg. Ximian/Novell and Red Hat).
