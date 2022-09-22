---
title: 'pkg-config patches'
slug: pkg-config-patches
date: 2005-06-21T19:56:18+08:00
tags: ['Gnome']
---

I uploaded a few patches to the pkg-config bugzilla recently, which will
hopefully make their way into the next release.

The first is related to [bug
3097](https://bugs.freedesktop.org/show_bug.cgi?id=3097 "dependent
library elimination causing link problems with -zdefs"), which has to
do with the [broken dependent library elimination code](pkg-config.md)
added to 0.17.

The patch adds a `Requires.private` field to `.pc` files that contains a
list of required packages like `Requires` currently does, which has the
following properties:

-   When verifying that a particular package name is available with
    \"`pkg-config --exists`\", dependencies in both `Requires` and
    `Requires.private` are checked.
-   When running \"`pkg-config --cflags`\", flags from dependencies in
    `Requires` are included.
-   When running \"`pkg-config --libs`\", flags from dependencies in
    `Requires` are included.
-   When running \"`pkg-config --static --libs`\", flags from
    dependencies in both `Requires` and `Requires.private` are included.

The purpose of this is to list dependencies that are not exposed in the
API of the library in question while not making users of the library
link directly to those dependencies. This means that private
dependencies can be upgraded to new incompatible versions without
breaking applications that only depend on them indirectly.

This is intended for cases like [Cairo](http://www.cairographics.org/),
which links to `libpng`, but doesn\'t expose any of the `libpng` API
itself. It is not intended for dependencies like `gtk+` depending on
`pango`. Of course, this header will cause the `.pc` file to be
incompatible with `pkg-config` versions prior to 0.16, because those
versions don\'t tolerate unknown fields.

The other changes are related to the associated autoconf macros:

-   Add a `PKG_CHECK_EXISTS()` macro. This would be similar to
    `PKG_CHECK_MODULES()`, except that no variables would be set or
    substitutes \-- it would simply run the `ACTION-IF-FOUND` or
    `ACTION-IF-NOT-FOUND` arguments. It is basically a less heavy weight
    macro for cases where you just want to see if a set of modules is
    available ([bug
    3530](https://bugs.freedesktop.org/show_bug.cgi?id=3530 "add a PKG_CHECK_EXISTS() autoconf macro")).
-   Get rid of the caching behaviour in `PKG_CHECK_MODULES()`. Since
    0.16, this macro has cached the result of the check based on the
    variable prefix passed as the first argument. Since pkg-config is
    quite fast and `configure` doesn\'t store its cache between runs by
    default, this doesn\'t result in any noticable speed improvement and
    causes build problems for `configure` scripts that call
    `PKG_CHECK_MODULES` multiple times with the same variable name
    prefix but different package lists (e.g. [Eye of
    Gnome](http://mail.gnome.org/archives/desktop-devel-list/2005-June/msg00131.html)).
    It seems simplest to just remove the caching, resulting in a simpler
    and more reliable macro ([bug
    3550](https://bugs.freedesktop.org/show_bug.cgi?id=3550 "Result caching in PKG_CHECK_MODULES() is broken / causes breakage"),
    patch not yet uploaded).

With these changes, hopefully 0.18 will fix up the last few small
incompatibilities in the recent releases.

---
### Comments:
#### Alastair McKinstry - <time datetime="2005-06-23 05:55:34">23 Jun, 2005</time>

Hi, these changes look interesting and useful: I\'m fixing up packages
in Debian at the moment that have unnecessary dependencies. Any idea
when pkg-config 0.18 might be
released?

Regards
Alastair McKinstry

---
#### James Henstridge - <time datetime="2005-06-23 15:09:19">23 Jun, 2005</time>

I\'m not sure. I haven\'t spoken with Tollef much recently (I\'d guess
he\'s hard at work on breezy).

---
