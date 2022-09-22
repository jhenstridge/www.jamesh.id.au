---
title: '16 February 2000'
slug: 16-february-2000
date: 2000-02-17T05:10:59+08:00
---

I finished integrating Lars\'s properties patch into dia
(after modifying it so that it uses the offsets code). Now
you can group a number of lines and set their dash pattern
(before, you would have to ungroup the lines and go to each
individual properties dialog.

There are a few missing features though. Undo on changes
to a group does not work correctly. I will have to
implement a \"compound ObjectChange\" for this to work
correctly. I should also make it so you can modify the
properties of multiple objects without having to group them
(just selecting them).

Once more of the objects are changed over to using
properties maybe we will put out another release. There are
a few changes I want to make to the properties code though
(eg. giving bounds for number properties, giving enumeration
values for enum properties, etc).

I made a new release of gnome-python yesterday. Most of
the fixes in this one were applied by Matt Wilson. I am
looking at changing gnome-python/pygtk over to using
ExtensionClass. This will hopefully remove a lot of the
hand written python code, increase the amount of code that
can be generated, reduce memory usage and give a one to one
PyObject \<\--\> GtkObject mapping and remove the need
for python class wrappers. With Havoc\'s new defs file
format, doing the code generation should be even easier.
