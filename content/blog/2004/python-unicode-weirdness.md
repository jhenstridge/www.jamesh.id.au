---
title: 'Python Unicode Weirdness'
slug: python-unicode-weirdness
date: 2004-08-17T22:34:34+08:00
draft: false
tags: ['Python']
---

While discussing unicode on IRC with owen, we ran into a peculiarity in
Python\'s unicode handling. It can be tested with the following code:

> `>>> s = u'\U00010001\U00010002' >>> len(s) >>> s[0]`

Python can be compiled to use either 16-bit or 32-bit widths for
characters in its unicode strings (16-bit being the default). When
compiled in 32-bit mode, the results of the last two statements are `2`
and `u'\U00010001'` respectively. When compiled in 16-bit mode, the
results are `4` and `u'\ud800'`.

So rather than just being an implementation detail, the unicode string
width chosen at compile time can alter the result of Python programs
that manipulate characters outside of the basic multilingual plane. It
would be nice if Python programs didn\'t have to care about this sort of
detail \...
