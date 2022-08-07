---
title: 'pkg-config vs. Cross Compile and Multi-arch'
slug: pkg-config-vs-cross-compile-and-multi-arch
date: 2005-07-05T04:27:05+08:00
---

One of the areas where [`pkg-config`](http://pkgconfig.freedesktop.org/)
can cause some problems is when trying to cross compile some code, or
when working with multi-arch systems (such as bi-arch AMD64 Linux
distros). While it is possible to use `pkg-config` in such systems by
manipulating `$PKG_CONFIG_PATH` and/or `$PKG_CONFIG_LIBDIR`, users
can\'t just follow the instructions given for the single-arch case.

After some discussion with Wolfgang Wieser, we came up with [a proposal
for better supporting cross-compile and
multi-arch](http://pkgconfig.freedesktop.org/wiki/CrossCompileProposal)
uses. The main changes would be:

-   Add a new `--host` option `pkg-config`. This would allow
    `pkg-config` to use different default search paths based on the host
    type, and search for `.pc` files in host type specific subdirs on
    the search path.
-   If an unknown host type is given, then no default search path is
    disabled altogether.
-   The autoconf macro would pass this argument whenever it detected
    that `pkg-config` supported it.

For the common case, this should allow most packages to be built for the
non default architecture on a bi-arch system, or cross compiled, by just
passing `--host=foo` to `configure` and (you might still need to set
`$CC` or `$CFLAGS`, depending on the compiler setup).

For packages that install `.pc` files, they should continue to work.
However it will be worth updating them to install their `.pc` file into
a host type specific sub directory (the autoconf macros will make this
easy to do).

If this code is likely to affect you, send comments to the `pkg-config`
mailing list (or leave comments here).

---
### Comments:
#### Ian Campbell - <time datetime="2005-07-05 17:20:32">2 Jul, 2005</time>

I like the look of what you are doing, but thought you might be
interested in how we have solved this problem for cross compiling.

We have a cross tool chain (e.g. arm-linux-gcc) which is installed into
prefix /opt/arcom/. We then build pkg-config with
\--libdir=/opt/arcom/arm-linux/lib \--program-prefix=arm-linux-

Now when we cross compile libraries we put their .pc into the arm-linux
pkgconfig directory and when we build something using pkg-config we pass
in \$PKGCONFIG (or whatever it is called) as arm-linux-pkgconfig \--
which has nice symmetry with overriding \$CC etc. If \--host=arm-linux
would cause configure to search for arm-linux-pkgconfig automatically
like it does with gcc then that would be even cooler.

This scheme probably doesn\'t help at all with bi-arch though.

Ian.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-07-05 23:02:41">2 Jul, 2005</time>

Ian: with these changes, you should be able to use the system\'s default
pkg-config binary. It will just skip the system configured search paths,
and only look in the directories you set in \$PKG\_CONFIG\_PATH (which
is the instructions most packages give you if installed packages can\'t
be found).

Having multiple pkg-config binaries would be another option, but the
only difference between them would be about 3 strings inside the
binaries, which seems a bit wasteful. It also removes the need to
recompile pkg-config when you want to target a new host type.

---
