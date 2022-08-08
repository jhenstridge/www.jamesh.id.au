---
title: '4 October 2002'
slug: 4-october-2002
date: 2002-10-05T07:53:23+08:00
---

**[linux.conf.au](http://linux.conf.au/)**

[Registrations](http://linux.conf.au/register/) are now open!

**PyORBit**

Fixed up handling of return values for all types. Now I need to look at
the handling of arguments. The semantics of ORBit\_small\_invoke\_stub
are non trivial. Also fixed a bug in the marshalling of sequences to
python types.

Tracked down and fixed one of the typelib bugs. Turned out to be a
subtle bug in the IDL compiler.
