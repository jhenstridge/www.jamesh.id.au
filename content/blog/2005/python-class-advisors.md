---
title: 'Python class advisors'
slug: python-class-advisors
date: 2005-09-08T16:48:52+08:00
draft: false
tags: ['Python']
---

Anyone who has played with Zope 3 has probably seen the syntax used to
declare what interfaces a particular class implements. It looks
something like this:

    class Foo:
        implements(IFoo, IBar)
        ...

This leads to the following question: how can a function call inside a
class definition\'s scope affect the resulting class? To understand
how this works, a little knowledge of Python metaclasses is needed.

**Metaclasses**

In Python, classes are instances of metaclasses. For new-style
classes, the default metaclass is `type` (which happens to be its own
metaclass). When you create a new class or subclass, you are creating
a new instance of the metaclass. The constructor for a metaclass takes
three arguments: the class\'s name, a tuple of the base classes and a
dictionary attributes and methods. So the following two definitions of
the class `C` are equivalent:

    class C(object):
        a = 42

    C = type('C', (object,), {'a': 42})

The metaclass for a particular class can be picked in a number of
ways:

-   A `__metaclass__` variable at module or class scope.
-   Use the same metaclass as the base class.

If no metaclass is specified through either of these means, an \"old
style\" class is created. I won\'t cover old style classes here.

Now in Python calling a function and creating a new instance look
pretty similar. In fact the metaclass machinary doesn\'t really
care. The following two class definitions are also equivalent:

    class C:
        __metaclass__ = type

    def not_the_metaclass(name, bases, attrs):
        return type(name, bases, attrs)

    class C:
        __metaclass__ = not_the_metaclass

So using a function or other callable object as the metaclass
allows you to hook into the class creation without affecting the
type of the resulting class.

**Class Advisors**

The tricks performed by the Zope `implements()` function are
wrapped up in the `zope.interface.advice` module. It does so by
making use of the fact that Python programs can inspect their
execution stack at runtime.

1.  Walk up the stack to where the scope of the class being
    defined.
2.  Check to see if a \"`__metaclass__`\" variable has been set,
    which would indicate the that a metaclass has been specified
    for this particular class already.
3.  Check the module scope for a \"`__metaclass__`\" variable.
4.  Define a function `advise(name, bases, cdict)` that does the
    following:
    -   Deduce the metaclass (either what `__metaclass__` was set
        to in the class scope, the module scope, or check base
        classes).
    -   Call the metaclass to create the new class.
    -   Do something to the new class (in the case of Zope, it
        sets what interfaces the class implements).
5.  Set the \"`__metaclass__`\" variable in the class scope to
    this function.

The actual implementation is a little more complicated to handle
the case of registering multiple class advisors for a single
class. The actual interface provided is quite simple though:

    from zope.interface.advice import addClassAdvisor

    def setA():
        def advisor(cls):
            cls.a = 42
            return cls
        addClassAdvisor(advisor)

    class C:
        setA()

This simply sets the attribute \'a\' on the class after it has
been created. Also, since method decorators are implemented as a
single function call, they can add a class advisor as a way to
perform some extra work on the class or method after the class
has been constructed.
