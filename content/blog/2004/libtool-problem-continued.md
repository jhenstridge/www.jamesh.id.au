---
title: 'Libtool Problem (continued)'
slug: libtool-problem-continued
date: 2004-10-27T05:32:35+08:00
---

Shortly after posting the last entry about the libtool problem I sent a
message to the [bug-libtool
list](http://news.gmane.org/gmane.comp.gnu.libtool.bugs),
[Scott](http://www.netsplit.com/blog) helped to track down the problem.

With the help of the test script I wrote, he managed to track down the
change on the libtool-2.0 branch that fixed the problem. Applying this
same change to a 1.5.x release fixed the problem. He has uploaded a new
Debian package with the change, and I\'ve altered the
`jhbuild bootstrap` module set to include the patch too. The copy of the
patch included with JHBuild can be found
[here](http://cvs.gnome.org/viewcvs/jhbuild/patches/libtool-1.5.10-deplibs-in-conv.patch?view=markup).
Hopefully it will also be in a future 1.5.x release (assuming that there
are any more).

Scott pointed out another case where people might run into the problem
is when building binary packages for software. A packager usually builds
the new version of the software into a temporary prefix (often by
setting the `$DESTDIR` environment variable when calling
`make install`). If the package includes a library with some
applications that link to the library and there is an old version of the
package installed on the system, libtool could end up linking with the
library in `/usr/lib`, which could result in a build failure if some new
APIs were added. The patch should fix this particular case too.

So if you release tarballs that make use of libtool, applying this patch
may help out the people maintaining binary packages of the software for
a distro too (assuming that they haven\'t gone the scorched earth route
and deleted all the `.la` files \...).
