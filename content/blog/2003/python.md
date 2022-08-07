---
title: 'Python'
slug: python
date: 2003-10-21T02:20:46+08:00
draft: false
---

Been reading over Ulrich Drepper\'s [paper on how to write shared
libraries](http://people.redhat.com/drepper/dsohowto.pdf), and it struck
me that use of the `PyArg_ParseTupleAndKeywords()` function will result
in a lot of relocations that can\'t be avoided.

I did a few tests using some dummy extension modules that contained a
number of functions. I tried varying the number of functions, number of
arguments for each function, and whether keyword arguments were
supported.

I found that in the `PyArg_ParseTuple()` case, the number of relocations
was proportional to the number of functions (as expected \-- a few
relocations for each entry in the `PyMethodDef`array. For the
`PyArg_ParseTupleAndKeywords()` case, there was also one relocation for
each argument listed in the keyword list array, which dominated as the
number of arguments went up.

I haven\'t checked how much influence this has on the startup speed, but
it would make a difference to the amount of code shareable between
processes for larger modules.
