---
title: 'jhbuild'
slug: jhbuild-2
date: 2004-03-23T10:26:57+08:00
tags: ['JHBuild']
---

Made some changes to the way \"`jhbuild bootstrap`\" works. Whereas
previously `bootstrap` would check to see if each required build tool
was installed by the distro and only build the tools that were missing,
it now builds all the tools.

If you wish to use the build tools supplied by your distro, it is now
recommended that you *don\'t* run `bootstrap`. To perform the \"check
that required tools are installed\" job that `bootstrap` used to do, you
can instead run the \"`jhbuild sanitycheck`\" command, which will do
these checks and report any errors. The `sanitycheck` command also
checks for other configuration problems as well, such as whether the all
the different automake versions will be able to find the libtool macros.

The upside for me is that there are now only 2 combinations of distro
packages vs. packages installed by jhbuild, as opposed to the 2*n*
combinations previously (where *n* is the number of bootstrap packages).
This greatly reduces the number of ways someone can screw up their
system.

Since `bootstrap` is a lot simpler now, I also changed how it was
implemented. Rather than using a separate code path, it now uses the
same build framework as the main build. The `bootstrap` command is now
functionally equivalent to building `meta-bootstrap` from the
`bootstrap` module set. Changing the list of bootstrap packages can now
be done as easily as modifying any other module set.

Removing the redundant code path should make things a little more
robust, since it reduces the amount of infrequently used and/or untested
code.
