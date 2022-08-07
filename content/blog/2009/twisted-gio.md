---
title: 'Using Twisted Deferred objects with gio'
slug: twisted-gio
date: 2009-01-06T10:18:53+09:00
tags: ['Gnome', 'Python', 'Twisted']
---

The gio library provides both synchronous and asynchronous interfaces
for performing IO.  Unfortunately, the two APIs require quite different
programming styles, making it difficult to convert code written to the
simpler synchronous API to the asynchronous one.

For C programs this is unavoidable, but for Python we should be able to
do better.  And if you\'re doing asynchronous event driven code in
Python, it makes sense to look at [Twisted](http://twistedmatrix.com/). 
In particular, Twisted\'s Deferred objects can be quite helpful.

**Deferred**

The [Twisted
documentation](http://twistedmatrix.com/documents/8.2.0/api/twisted.internet.defer.Deferred.html)
describes deferred objects as \"a callback which will be put off until
later\".  The deferred will eventually be passed the result of some
operation, or information about how it failed.

From the consumer side, you can register one or more callbacks that will
be run:

    def callback(result):
        # do stuff
        return result

    deferred.addCallback(callback)

The first callback will be called with the original result, while
subsequent callbacks will be passed the return value of the previous
callback (this is why the above example returns its argument). If the
operation fails, one or more errbacks (error callbacks) will be called:

    def errback(failure):
        # do stuff
        return failure

    deferred.addErrback(errback)

If the operation associated with the deferred has already been completed
(or already failed) when the callback/errback is added, then it will be
called immediately. So there is no need to check if the operation is
complete before hand.

**Using Deferred objects with gio**

We can easily use gio\'s asynchronous API to implement a new API based
on deferred objects.  For example:

    import gio
    from twisted.internet import defer

    def file_read_deferred(file, io_priority=0, cancellable=None):
        d = defer.Deferred()
        def callback(file, async_result):
            try:
                in_stream = file.read_finish(async_result)
            except gio.Error:
                d.errback()
            else:
                d.callback(in_stream)
        file.read_async(callback, io_priority, cancellable)
        return d

    def input_stream_read_deferred(in_stream, count, io_priority=0,
                                   cancellable=None):
        d = defer.Deferred()
        def callback(in_stream, async_result):
            try:
                bytes = in_stream.read_finish(async_result)
            except gio.Error:
                d.errback()
            else:
                d.callback(bytes)
        # the argument order seems a bit weird here ...
        in_stream.read_async(count, callback, io_priority, cancellable)
        return d

This is a fairly simple transformation, so you might ask what this buys
us. We\'ve gone from an interface where you pass a callback to the
method to one where you pass a callback to the result of the method. The
answer is in the tools that Twisted provides for working with deferred
objects.

**The inlineCallbacks decorator**

You\'ve probably seen code examples that use Python\'s generators to
implement simple co-routines. Twisted\'s `inlineCallbacks` decorator
basically implements this for generators that yield deferred objects. It
uses the enhanced generators feature from Python 2.5 ([PEP
342](http://www.python.org/dev/peps/pep-0342/)) to pass the deferred
result or failure back to the generator. Using it, we can write code
like this:

    @defer.inlineCallbacks
    def print_contents(file, cancellable=None):
        in_stream = yield file_read_deferred(file, cancellable=cancellable)
        bytes = yield input_stream_read_deferred(
            in_stream, 4096, cancellable=cancellable)
        while bytes:
            # Do something with the data.  For this example, just print to stdout.
            sys.stdout.write(bytes)
            bytes = yield input_stream_read_deferred(
                in_stream, 4096, cancellable=cancellable)

Other than the use of the yield keyword, the above code looks quite
similar to the equivalent synchronous implementation.  The only thing
that would improve matters would be if these were real methods rather
than helper functions.

Furthermore, the `inlineCallbacks` decorator causes the function to
return a deferred that will fire when the function body finally
completes or fails. This makes it possible to use the function from
within other asynchronous code in a similar fashion. And once you\'re
using deferred results, you can mix in the gio calls with other Twisted
asynchronous calls where it makes sense.

---
### Comments:
#### [davidz](http://blog.fubar.dk) - <time datetime="2009-01-06 09:57:47">2 Jan, 2009</time>

Note that for C, there\'s the GFiber proposal

http://bugzilla.gnome.org/show\_bug.cgi?id=565501

---
