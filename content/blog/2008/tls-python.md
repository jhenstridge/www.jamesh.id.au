---
title: 'How not to do thread local storage with Python'
slug: tls-python
date: 2008-06-11T18:00:21+08:00
tags: ['Python']
---

The [Python](http://www.python.org/) standard library contains a
function called `thread.get_ident()`.  It will return an integer that
uniquely identifies the current thread at that point in time.  On most
UNIX systems, this will be the `pthread_t` value returned by
`pthread_self()`. At first look, this might seem like a good value to
key a thread local storage dictionary with.  *Please* don\'t do that.

The value uniquely identifies the thread only as long as it is running. 
The value can be reused after the thread exits.  On my system, this
happens quite reliably with the following sample program printing the
same ID ten times:

    import thread, threading

    def foo():
        print 'Thread ID:', thread.get_ident()

    for i in range(10):
        t = threading.Thread(target=foo)
        t.start()
        t.join()

If the return value of `thread.get_ident()` was used to key thread local
storage, all ten threads would share the same storage. This is not
generally considered to be desirable behaviour.

Assuming that you can depend on Python 2.4 (released 3.5 years ago),
then just use a
[`threading.local`](http://www.python.org/doc/current/lib/module-threading.html)
object. It will result in simpler code, correctly handle serially
created threads, and you won\'t hold onto TLS data past the exit of a
thread.

You will save yourself (or another developer) a lot of time at some
point in the future. Debugging these problems is not fun when you
combine code doing proper TLS with other code doing broken TLS.

---
### Comments:
#### bash - <time datetime="2008-06-12 03:52:50">12 Jun, 2008</time>

get\_ident() is the threading equivalent to fileno in filelike objects.
None of them claim to be unique and both are implementation details
which may be out of the contract, but are very useful.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-06-12 08:30:05">12 Jun, 2008</time>

I don\'t dispute that the function has its uses -- just that this is not
one of them. I spent a while tracking down a problem caused by this
class of bug (<https://bugs.launchpad.net/zodb/+bug/239086>).

---
#### Pierre - <time datetime="2008-06-13 16:18:32">13 Jun, 2008</time>

Thanks for pointing this out.

---
