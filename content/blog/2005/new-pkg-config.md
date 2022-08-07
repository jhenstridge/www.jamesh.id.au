---
title: 'New pkg-config'
slug: new-pkg-config
date: 2005-04-14T07:43:09+08:00
draft: false
---

I recently pointed jhbuild\'s bootstrap module-set at the new releases
of [pkg-config](http://pkgconfig.freedesktop.org/wiki/), which seems to
have triggered some problems for some people.

In some ways, it isn\'t too surprising that some problems appeared,
since there were two years between the 0.15 and 0.16 releases. When you
go that long without testing from packages that depend on you, some
incompatibilities are bound to turn up. However, Tollef has been doing a
good job fixing the bugs and 0.17.1 fixes most of the problems I\'ve
found.

So far, I\'ve run into the following problems (some reported to me as
jhbuild bug reports):

-   `PKG_CHECK_MODULES()` stopped evaluating its second argument in
    0.16.0. This caused problems for modules like `gtk+`
    \[[\#300232](http://bugzilla.gnome.org/show_bug.cgi?id=300232),
    [fd.o bug \#2987](https://bugs.freedesktop.org/show_bug.cgi?id=2987)
    \-- fixed in pkg-config-0.17\].
-   The `pkg.m4` autoconf macros now blacklist words matching `PKG_*` or
    `_PKG_*` in the resulting configure script (with the exception of
    `PKG_CONFIG` and `PKG_CONFIG_PATH`). This is to try and detect
    unexpanded macros, but managed to trip up ORBit2 (ORBit2 has since
    been fixed in CVS though).
    \[[\#300151](http://bugzilla.gnome.org/show_bug.cgi?id=300151)\]
-   The `PKG_CHECK_MODULES()` macro now uses the autoconf result caching
    mechanism, based on the variable prefix passed as the first
    argument. This means that multiple `PKG_CHECK_MODULES()` calls using
    the same variable prefix will give the same result, even if they
    specifiy a different list of modules
    \[[\#300435](http://bugzilla.gnome.org/show_bug.cgi?id=300435),
    [\#300436](http://bugzilla.gnome.org/show_bug.cgi?id=300436),
    [\#300449](http://bugzilla.gnome.org/show_bug.cgi?id=300449)\]
-   The `pkg-config` script can go into an infinite loop when expanding
    the link flags if a package name is repeated \[[fd.o bug
    \#3006](https://bugs.freedesktop.org/show_bug.cgi?id=3006),
    workarounds for some Gnome modules:
    [\#300450](http://bugzilla.gnome.org/show_bug.cgi?id=300450),
    [\#300452](http://bugzilla.gnome.org/show_bug.cgi?id=300452)\]

(note that only the last problem is likely to affect people building
existing packages from tarballs)

Appart from these problems, there are some new features that people
might find useful:

Unknown headers are ignored in `.pc` files. This will make future
extensions possible. Previously, if you wanted to make use of a feature
in a newer version of `pkg-config` in your `.pc`, you\'d probably end up
making the file incompatible with older versions. This essentially meant
that a new feature could not be used until the entire userbase upgraded,
even if the feature was non-critical.

A new `Url` header can be used in a `.pc` file. If `pkg-config` finds a
version of a required package, but it is too old, then the old `.pc`
file can print a URL telling people where to find a newer version.
Unfortunately, if you use this feature your `.pc` file won\'t work with
`pkg-config` \<= 0.15.

<div>

A virtual \"`pkg-config`\" package is provided by `pkg-config`. It
doesn\'t provide any `cflags` or `libs`, but does include the version
number. So the following are equivalent:

</div>

>     pkg-config --atleast-pkgconfig-version=0.17.1
>     pkg-config --exists pkg-config '>=' 0.17.1
>
> <div>
>
> This may not sound useful at first, but you can also list the module
> in the `Requires` line of another `.pc` file. As an example, if you
> used some weird link flags that `pkg-config` used to mangle but has
> since been fixed, you can encode that requirement in the `.pc` file.
> Of course, this is only useful for checking for `pkg-config` versions
> greater than 0.16.
>
> </div>
