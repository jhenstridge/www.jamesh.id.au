---
title: '30 September 2002'
slug: 30-september-2002
date: 2002-10-01T06:38:00+08:00
---

[**PyORBit**](http://cvs.gnome.org/lxr/source/gnome-python/pyorbit/)

Started working on a new binding for ORBit2 about a week ago. The
existing orbit-python port to ORBit2 is a little crufty, and doesn\'t
take advantage of the new features in ORBit2. So far things have looked
fairly promising, but I have turned up a number of ORBit2 bugs related
to the use of typelibs. Some of them are pretty weird (such as [bug
93928](http://bugzilla.gnome.org/show_bug.cgi?id=93928) and [bug
94513](http://bugzilla.gnome.org/show_bug.cgi?id=94513)), while others
indicate defficiencies in the current typelib implementation itself
([bug 93725](http://bugzilla.gnome.org/show_bug.cgi?id=93725)). I don\'t
know if I will be able to get it to a usable state when compiled with
ORBit2 2.4.x, so I might have to wait til GNOME 2.2 before using these
in the GNOME Python bindings.

Other than the bugs, I have a mostly working client side binding that
generates stubs at runtime from typelibs, and have a little code for the
server side. I am looking at doing a custom object adaptor at the
moment, rather than getting it to work with the POA (it won\'t prevent
using POA in the future). The API would probably be as simple as
\"`objref = create_servant(repo_id, instance)`\", which would create and
activate a new servant that delegated all method calls to `instance`
(which could be of any class \-- the only constraint being that it
implement the required methods), and returned an object reference. This
should be enough for most cases.

**Weird Bug Reports**

Some people send in very weird bug reports. This morning, I received
[bug 94576](http://bugzilla.gnome.org/show_bug.cgi?id=94567) which seems
to have nothing to do with the package it was filed against, has a stack
trace from some weird custom app (I guess), and talks about Anna
Kournikova a bit. I don\'t know why people send in bug reports that are
obviously useless \-- it is a waste of their time and mine.
