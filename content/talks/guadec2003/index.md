---
title: "GUADEC 2003: Libegg and PyORBit"
date: 2003-06-16T00:00:00+08:00
resources:
 - src: libegg-slides.pdf
 - src: pyorbit-slides.pdf
 - src: metadata-demo.py
keywords: ["guadec", "libegg", "pyorbit"]
aliases: ["/talks/guadec2003/libegg/", "/talks/guadec2003/pyorbit/"]
---

At GUADEC 2003 in Dublin, I gave talks about Libegg and PyORBit.

<!--more-->

Libegg was a library used to prototype new features for GTK.  My talk
focused on the EggToolbar class and EggMenu system, which were both
merged into GTK 2.4 as the new GtkToolbar API and GtkUIManager.

PyORBit is a Python binding for the ORBit2 CORBA implementation.  It
was designed to follow the standard CORBA Python Language Mapping,
while using ORBit2's type libraries to generate stubs and skeletons at
runtime.

* [EggToolbar and EggMenu (slides)](libegg-slides.pdf)
* [PyORBit (slides)](pyorbit-slides.pdf)

## Example Code

The PyORBit slides reference the following example program:

[`metadata-demo.py`](metadata-demo.py)
: monitor Nautilus metadata via CORBA
