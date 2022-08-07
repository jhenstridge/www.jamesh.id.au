---
title: 'GraphViz'
slug: graphviz
date: 2005-01-18T06:39:27+08:00
tags: ['JHBuild']
---

On the `gtk-doc-list` mailing list, Matthias mentioned that the
[GraphViz](http://www.graphviz.org/) license has been changed to the
[CPL](http://www.opensource.org/licenses/cpl.php) (the same license as
used for Eclipse), which is considered Free by both the FSF and OSI
(although still GPL incompatible). This should remove the barriers that
prevented it getting packaged by Linux distributions.

Due to the previous licensing, RMS urged developers of GNU software to
not even produce output in the form that the GraphViz tools use as
input. Maybe that can change now. While the license is GPL incompatible,
the GraphViz tools can easily be invoked from the command line, passing
a `.dot` file in, and getting output in PNG, PS, SVG, etc format (or
even another `.dot` file with the layout information added), which is
enough for pretty much all uses of the tools.

One of the features I added to JHBuild fairly early on was the ability
to dump the dependency tree for a set of modules in the `.dot` format.
So to visualise the dependencies for Gnome, you could run a command like
this:

    jhbuild dot meta-gnome-desktop | dot -Tps > gnome-2.10.eps

(of course, given the number of modules that are needed to build the
entire Gnome desktop, you might get a better picture by picking a
smaller number of modules).
