---
title: '1 November 2004'
slug: 1-november-2004
date: 2004-11-01T10:43:57+08:00
tags: ['Bazaar']
---

**Libtool**

When looking into the libtool problem I mentioned earlier, I decided to
take a look at the libtool-2.0 betas. Overall, it looks pretty good.
I\'ve updated the
[gnome-common](http://cvs.gnome.org/viewcvs/gnome-common/) `autogen.sh`
script to support it. So if a package uses the `LT_INIT` macro, it will
call `libtoolize` for you.

One of the new features in these versions of libtool is that if you have
a `AC_CONFIG_MACRO_DIR(directory)` call in your `configure.ac` file, it
will copy the libtool M4 macros to that directory. If you then call
`aclocal` with the correct `-I` flag, autoconf will use that version of
the macro.

This means that you will get consistent versions of `ltmain.sh` and
`libtool.m4`, which is a lot more reliable. With the old setup, the
version of `ltmain.sh` you got would depend on `$PATH` while the version
of `libtool.m4` would depend on the `aclocal` search path. With the new
setup, it just depends on `$PATH`.

The only problem is that `aclocal` doesn\'t automatically check the
macro dir for macros. This is pretty easy to work around. Just pass the
appropriate `-I` flag to `aclocal` in `autogen.sh`, and make sure
`ACLOCAL_AMFLAGS` gets set appropriately in your `Makefile.am`\'s. This
second part can be done from the `configure.in` file like so:

    AC_CONFIG_MACRO_DIR([m4])
    ...
    # make sure $ACLOCAL_FLAGS are used during a rebuild.
    AC_SUBST([ACLOCAL_AMFLAGS], ["-I $ac_macro_dir \${ACLOCAL_FLAGS}"])

(the above will also pass `$ACLOCAL_FLAGS` to `aclocal` on a rebuild,
which is expected when building most Gnome packages).

I also updated the gnome-common `autogen.sh` script to check for
`AC_CONFIG_MACRO_DIR`, and call `aclocal` correctly, so a package
maintainer doesn\'t need to do anything special.

This system could benefit some of the other Gnome related build tools
like intltool and gtk-doc --- I recently got CC\'d on an intltool bug
that seemed to be caused by mismatched macros and support files, so
people are tripping over the problem. It should be pretty trivial to
modify `intltoolize` to check for `AC_CONFIG_MACRO_DIR`, and copy over
the macro file if it finds it. This wouldn\'t affect its behaviour on
existing packages, but would be more reliable on packages that have been
updated to use the macro.

[**Bazaar**](http://bazaar.canonical.com/)

I did some initial [Fedora Core 2 packages for
Bazaar](http://bazaar.canonical.com/packages/rpms/fc2/) (a new GNU Arch
command line tool sponsored by Canonical). It is only an i386 build, but
I\'ll add an x86-64 build once I have FC2 or FC3 set up on my desktop
(so far I\'ve only got round to installing Ubuntu/AMD64 on it).

At the moment `baz` is quite similar to `tla`, but there are some
promising [interface
ideas](http://wiki.gnuarch.org/moin.cgi/BazaarMockupUI) that should make
it a lot nicer to use. If you\'ve avoided Arch due to `tla`\'s
complexity, `baz` might be worth trying when it develops further.
