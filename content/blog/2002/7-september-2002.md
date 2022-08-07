---
title: '7 September 2002'
slug: 7-september-2002
date: 2002-09-07T09:30:02+08:00
draft: false
---

**Egg**

Did a bit of work on
[EggToolbar](http://cvs.gnome.org/lxr/source/libegg/libegg/toolbar/) and
got it into a state where I could use it in
[EggMenu](http://cvs.gnome.org/lxr/source/libegg/libegg/menu/). Felt
good to work on these, as they had been neglected for a while. The
toolbar works quite well now, and I brought the merge code for toolbars
in EggMenu into parity with the menu merge code (now supports
placeholders, etc).

**[PyGIMP](http://www.daa.com.au/~james/pygimp/)**

[Yosh](/person/yosh/) added a little bit of magic to the autogen script
for [GIMP](http://www.gimp.org/) so that if you have automake-1.6, it
will optionally build PyGIMP. So it should be as simple as running
\"`./configure --enable-python`\" on the gimp-1.3.9 tarball to install
PyGIMP.
