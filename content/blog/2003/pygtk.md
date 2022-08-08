---
title: 'PyGTK'
slug: pygtk
date: 2003-08-25T07:06:06+08:00
---

Over the weekend, I did a set of releases for pygtk, pyorbit and
gnome-python. These releases are pretty much what I want for the 2.0
versions (which have been a long time coming). These releases should fix
up the last few remaining bugs related to running with [Python
2.3](http://www.python.org/2.3/), and bugs related to compiling on
[MacOS X](http://www.apple.com/macosx/). If no serious bugs are found,
I\'ll do 2.0 releases shortly.

Once 2.0 is done and I have branched, I can start looking at moving on
to the newer APIs. Some of the things I want to do include:

-   Delete the `gtk.gl` binding, or move it to the gtkglarea package.
    This library seems pretty much dead, and there is [another OpenGL
    binding for GTK](http://gtkglext.sourceforge.net/) which is being
    actively developed, and even has a Python binding.
-   Add all the new GTK 2.2 APIs to PyGTK. This shouldn\'t take too
    long, as all the infrastructure is there now.
-   Move gnome-python on to the GNOME 2.4 libraries. Given the timing of
    releases, its probably not worth targetting 2.2 separately.
-   Delete the `gnome.zvt` binding. The libzvt library is pretty much
    dead, and [VTE](http://cvs.gnome.org/lxr/source/vte) includes a
    Python binding itself.

There are a few other things I want to look at, such as Python 2.3\'s
new [`PyGILState`](http://www.python.org/peps/pep-0311.html) APIs, which
could potentially simplify PyGTK\'s threading support a lot, and make it
interact better with other threaded Python extension modules.
