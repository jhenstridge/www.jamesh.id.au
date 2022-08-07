---
title: 'Overriding Class Methods in Python'
slug: overriding-class-methods-in-python
date: 2005-06-23T13:28:38+08:00
tags: ['Python']
---

One of the features added back in Python 2.2 was class methods. These
differ from traditional methods in the following ways:

1.  They can be called on both the class itself and instances of the
    class.
2.  Rather than binding to an instance, they bind to the class. This
    means that the first argument passed to the method is a class object
    rather than an instance.

For most intents and purposes, class methods are written the same way as
normal instance methods. One place that things differ is overriding a
class method in a subclass. The following simple example demonstrates
the problem:

    class SubClass(ParentClass):
        @classmethod
        def create(cls, arg):
            ret = ParentClass.create(cls, arg)
            ret.dosomethingelse()
            return ret

This code is broken because the `ParentClass.create()` call is calling
the version of `create()` method in the context of `ParentClass`,
rather than calling an unbound method like it would with a normal
instance method. The most likely outcome will be a `TypeError` due to
the method receiving too many arguments.

So how do you chain up to the parent class implementation? You use the
`super()` object, which was also added in Python 2.2 as an alternative
way to chain to the parent implementation of a method. The above code
rewritten as follows:

    class SubClass(ParentClass):
        @classmethod
        def create(cls, arg):
            ret = super(SubClass, cls).create(arg)
            ret.dosomethingelse()
            return ret

If you haven\'t ever used the `super()` object, this is what it is
doing in the above example:

1.  `SubClass` is looked up in the list `cls.__mro__` (a linearised
    list of ancestor classes in the order used for method
    resolution).
2.  The class dict for each ancestor class coming after `SubClass`
    in `cls.__mro__` is checked to see if it contains \"`create`\".
3.  The `super()` object returns a version of \"`create`\" in the
    context of `cls` using the `__get__(cls)` \"descriptor get\"
    method.
4.  When this bound method gets called, `cls` will be passed in
    instead of the parent class.

Previously I\'d ignored `super()` for the most part, since I could
use the old chaining syntax. This shows a place where the old-style
syntax can\'t be applied.

---
### Comments:
#### cs - <time datetime="2005-06-23 20:17:14">4 Jun, 2005</time>

Looks a lot like Ruby.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-06-24 00:43:34">5 Jun, 2005</time>

From my quick reading of some Ruby documentation, it says that \"super\"
is a keyword.

In Python, it is just another object. In fact, it could easily be
rewritten in Python as seen here:\
<http://www.python.org/2.2/descrintro.html#superexample>

It is just an application of the descriptor features added back then.

---
#### Geoff Gerrietts - <time datetime="2005-06-24 07:05:58">5 Jun, 2005</time>

SubClass and Subclass are mixed throughout the code examples. That\'s
not intentional is it?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-06-24 10:47:04">5 Jun, 2005</time>

Thanks for pointing that out. I was adapting a real example, and made
some mistakes when transcribing it.

---
