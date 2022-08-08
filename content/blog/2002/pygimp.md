---
title: 'PyGIMP'
slug: pygimp
date: 2002-08-31T05:47:14+08:00
---

Started working on the python bindings for gimp 1.3. It has been a long
time since I had done much with that code (a lot of the code hadn\'t
been changed in 3 years), and it was a bit embarassing to see how bad
some of it was \...

I now have it mostly working, and updated to take advantage of new
Python 2.2 features (given that pygtk for gtk 2.0 uses Python 2.2, there
was no point in artificially limiting what constructs to use). Now I am
using new style classes for all the various gimp objects (which means
that issubclass(gimp.Layer, gimp.Drawable) is now true). It is almost at
a stage where it could be added to the main tarball builds of gimp.
