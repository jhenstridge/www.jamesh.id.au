---
title: '23 November 1999'
slug: 23-november-1999
date: 1999-11-23T13:48:02+08:00
---

-   Working on gnorpm again. I am converting the rpmfind
    code over to a non blocking architecture using the glibwww
    code I wrote (a thin wrapper around the W3C\'s libwww that
    uses the glib mainloop for transfers). It is not currently
    finished, but it is getting there.
-   Apparently the gtkhtml guys are using glibwww as well.
    Maybe it would be a good idea to split the code into a
    separate package at some point. For now, it means there are
    other people to help find and fix bugs in the code
    `:)` Libwww is a bit of a beast if you try to do
    something non trivial in a way that the authors did not
    expect. I know all libraries are like this, but libwww
    seems to be more so.
-   Once I have these changes finished, I should install
    that copy of Red Hat 6.1 to see what the problems were with
    it. Probably merge in some of the Red Hat patches in the
    RH6.1 RPM of gnorpm and release 0.11 (if I call it 0.10,
    there will be people calling it 0.1, which is quite old
    now).
-   I should do some more hacking on dia. I am looking at
    adding a python scripting interface. With a few
    modifications, it should be possible to add extra menu items
    that trigger python functions. Alexander has made Dia nice
    and modular, so this should be pretty easy. This interface
    should be powerful enough to do full manipulation of
    diagrams, and also extract information from a diagram for
    writing export filters. I want to be able to use the
    interface to export UML diagrams to UXF format and circuit
    diagrams to SPICE net files for instance. One thing that
    will be needed is a general way of reading and modifying the
    properties on objects. There was some talk on the list of
    adding this, which will be good.
