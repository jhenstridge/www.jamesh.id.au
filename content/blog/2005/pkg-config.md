---
title: 'pkg-config'
slug: pkg-config
date: 2005-04-26T07:04:17+08:00
---

One of the changes in the recent
[pkg-config](http://pkgconfig.freedesktop.org/) releases is that the\
`--libs` output no longer prints out the entire list of\
libraries expanded from the requested set of packages. As an example,\
here is the output of `pkg-config --libs gtk+-2.0` with version\
0.15:

    -lgtk-x11-2.0 -lgdk-x11-2.0 -latk-1.0 -lgdk_pixbuf-2.0 -lm -lpangoxft-1.0 -lpangox-1.0 -lpango-1.0 -lgobject-2.0 -lgmodule-2.0 -ldl -lglib-2.0

And with 0.17.1:

    -lgtk-x11-2.0

If an application is compiled with the first set of `-l`\
flags, it will include `DT_NEEDED` tag for each of those\
libraries. With the second set, it will only have a\
`DT_NEEDED` tag for `libgtk-x11-2.0.so.0`. When run,\
the application will still pull in all the other libraries via shared\
library dependencies.

The rationale for this change seems to boil down to:

-   Some programs link to more libraries than they need to.
-   Sometimes programs link to libraries that they don\'t use directly\
    \-- they\'re encapsulated by some other library they use.
-   The application will need to be recompiled if one of the libraries\
    it is linked against breaks ABI, even if the library is not used\
    directly.

At first this seems sensible. However, in a lot of cases\
applications actually use libraries that are only pulled in through\
dependencies. For instance, almost every GTK application is going to\
be using some glib APIs as well.

With the new pkg-config output, the fact that the application\
depends on the ABI of \"`libglib-2.0.so.0`\" is no longer\
recorded. The application is making use of those APIs, so it declare\
that. Without the glib `DT_NEEDED` tag, the application is\
relying on the fact that GTK isn\'t likely to stop depending on glib\
\...

Furthermore, this causes breakage if you link your application with\
the [libtool](http://www.gnu.org/software/libtool/)\
`-no-undefined` flag. On platforms that support it, this\
generates an error if you don\'t list all the libraries the application\
depends on. This allows for some optimisations on some platforms\
(e.g. Solaris), and is required on others (e.g. Win32).

*(interestingly, this problem doesn\'t exhibit itself on Linux.\
The `-no-undefined` flag expands to nothing, even though the\
linker supports the feature through the `-zdefs` flag)*

For these reasons, I\'ve disabled the feature in jhbuild\'s\
bootstrap, using the `--enable-indirect-deps` configure flag.\
If the aim is just to get rid of unnecessary library dependencies, the\
GNU linker\'s `--as-needed` flag seems to be a better choice.\
It will omit a `DT_NEEDED` tag if none of the symbols from the\
library are used by the application.
