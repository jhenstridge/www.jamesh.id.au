---
title: 'Re: Python factory-like type instances'
slug: python-metaclasses
date: 2008-02-12T14:54:44+09:00
draft: false
tags: ['Python']
---

[Nicolas](http://eikke.com/python-factory-like-type-instances/ "Python factory-like type instances"):
Your metaclass example is a good example of when not to use metaclasses.
I wouldn\'t be surprised if it is executed slightly different to how you
expect. Let\'s look at how `Foo` is evaluated, starting with what\'s
written:

    class Foo:
        __metaclass__ = FooMeta

This is equivalent to the following assignment:

    Foo = FooMeta('Foo', (), {...})

As `FooMeta` has an `__new__()` method, the attempt to instantiate
`FooMeta` will result in it being called. As the return value of
`__new__()` is not a `FooMeta` instance, there is no attempt to call
`FooMeta.__init__()`. So we could further simplify the code to:

    Foo = {
        'linux2': LinuxFoo,
        'win32': WindowsFoo,
    }.get(PLATFORM, None)
    if not Foo:
        # XXX: this should _really_ raise something other than Exception
        raise Exception, 'Platform not supported'

So the factory function is gone completely here, and it is clear that
the decision about which class to use is being made at module import
time rather than class instantiation time.

Now this isn\'t to say that metaclasses are useless. In both
implementations, the code responsible for selecting the class has
knowledge of all implementations. To add a new implementation (e.g. for
Solaris or MacOS X), the factory function needs to be updated. A better
solution would be to provide a way for new implementations to register
themselves with the factory. A metaclass could be used to make the
registration automatic:

    class FooMeta(type):
        def __init__(self, name, bases, attrs):
            cls = super(FooMeta, self).__init__(name, bases, attrs)
            if cls.platform is not None:
                register_foo_implementation(klass.platform, cls)
            return cls

    class Foo:
        __metaclass__ = FooMeta
        platform = None
        ...

    class LinuxFoo(Foo):
        platform = 'linux2'

Now the simple act of defining a `SolarisFoo` class would be enough to
have it registered and ready to use.

---
### Comments:
#### [John Stowers](http://www.johnstowers.co.nz) - <time datetime="2008-02-12 14:42:42">2 Feb, 2008</time>

Nice post. You may have seen this, but FWIW, the following site expands
on the idea of \'\...a metaclass could be used to make the registration
automatic\...\' to build a plugin system.

http://gulopine.gamemusic.org/2008/jan/10/simple-plugin-framework/

John

---
#### Snark - <time datetime="2008-02-12 15:50:06">2 Feb, 2008</time>

Nice post!

I thought python was saner than C++ \-- you prove me wrong!

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-02-12 21:13:58">2 Feb, 2008</time>

John: that guy really should read up on Zope interfaces a bit more \--
they handle a lot of the things he is doing.

Snark: if you think metaclasses are obscure, you should see what people
do with sys.\_getframe().

---
#### [john Stowers](http://www.johnstowers.co.nz) - <time datetime="2008-02-13 08:47:48">3 Feb, 2008</time>

\@James,

Yeah his first paragraph says as much. Still, I applaud his
determination for going to the effort. A lesser capable plugin system
that doesnt bring in zope.interface might be useful for those people who
care about such things

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-02-13 10:39:14">3 Feb, 2008</time>

There isn\'t much point in reinventing zope.interface. With the effort
the Zope 3 developers have put in to modularise everything, using
zope.interface does not imply pulling in the rest of Zope. There
doesn\'t seem to be much reason not to use it where appropriate.

---
#### [Python if/else in lambda &raquo; Ikke&#8217;s blog](http://eikke.com/python-ifelse-in-lambda/) - <time datetime="2008-02-17 05:47:24">0 Feb, 2008</time>

\[\...\] James, obviously you're right... Stupid me didn't think about
that. Your version won't work when a discriminator isn't known at import
time. But even then a function taking \*args and \*\*kwargs with a
class-like name, returning a correct class instance, would cut the job.
\[\...\]

---
