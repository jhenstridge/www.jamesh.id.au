---
title: "Linux.conf.au 2004: Scripting with PyORBit"
date: 2004-01-16T00:00:00+08:00
draft: false
keywords: ["linux.conf.au", "pyorbit"]
resources:
 - src: slides.pdf
 - src: list-apps.py
 - src: dump-tree.py
 - src: follow-focus.py
 - src: spell-check.py
 - src: aspell.py
 - src: open-nautilus.py
---

At Linux.conf.au 2004 in Adelaide, I gave a talk about controlling
GNOME applications from Python via the accessibility framework.

<!--more-->

At the time, GNOME's accessibility framework (AT-SPI) was built on top
of CORBA.  I had been working on a Python binding for the ORBit2 CORBA
implementation, so this talk demonstrated how it could be used to
script the accessibility API.

* [Remote Control and Scripting of Gnome Applications with Python (slides)](slides.pdf)

## Example Code

The slides reference a number of example programs provided here:

[`list-apps.py`](list-apps.py)
: lists all the accessible apps currently running.

[`dump-tree.py`](dump-tree.py)
: dumps the accessible tree for a particular app.

[`follow-focus.py`](follow-focus.py)
: prints information about the currently focused application.

[`spell-check.py`](spell-check.py)
: suggests corrections for mis-spellings found in text accessibles.

[`aspell.py`](aspell.py)
: support module for `spell-check.py`.

[`open-nautilus.py`](open-nautilus.py`)
: performs the "open" aciton on the first icon found.
