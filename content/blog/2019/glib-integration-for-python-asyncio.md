---
title: 'GLib integration for the Python asyncio event loop'
slug: glib-integration-for-python-asyncio
date: 2019-08-05T12:33:51+08:00
tags: ['asyncio', 'glib', 'GStreamer', 'Python']
---

As an evening project, I\'ve been working on a small library that
integrates the GLib main loop with [Python\'s
asyncio](https://docs.python.org/3/library/asyncio.html). I think I\'ve
gotten to the point where it might be useful to other people, so have
pushed it up here:

<https://github.com/jhenstridge/asyncio-glib>

This isn\'t the only attempt to integrate the two event loops, but the
other I found ([Gbulb](https://github.com/nhoad/gbulb)) is unmaintained
and seems to reimplement a fair bit of the asyncio (e.g. it has its own
transport classes). So I thought I\'d see if I could write something
smaller and more maintainable, reusing as much code from the standard
library as possible.

My first step was writing an implementation of the
[`selectors.BaseSelector`](https://docs.python.org/3/library/selectors.html)
interface in terms of the GLib main loop. The `select()` method just
runs a `GMainLoop` with a custom source that will quit the loop if any
of the file descriptors are ready, or the timeout is reached.

For the asyncio event loop, I was able to reuse the standard library
`asyncio.SelectorEventLoop` with my new selector. In action, it looks
something like this:

1.  Let the GMainLoop spin until any asyncio events come in.
2.  Return control to the asyncio event loop to process those events.
3.  Repeat

As far as testing goes, the Python standard library comes with a suite
of tests parameterised on an event loop implementation. So I\'ve just
reused that as the bulk of my test suite, and done the same with the
selector tests. There are a handful of test failures I still need to
diagnose, but for the most part things just work.

Making an asyncio application use this event loop is simple:

    import asyncio
    import asyncio_glib
    asyncio.set_event_loop_policy(asyncio_glib.GLibEventLoopPolicy())

The main limitation of this code is that it relies on asyncio running
the GLib main loop. If some other piece of code runs the main loop,
asyncio callbacks will not be triggered and will probably lead to busy
looping. This isn\'t a problem my project (an asyncio server making use
of GStreamer), but would be a problem for e.g. a graphical application
calling `gtk_dialog_run()`.

---
### Comments:
#### [Manuel Quiñones](http://aereo.manuq.com.ar) - <time datetime="2019-08-12 04:39:38">12 Aug, 2019</time>

Nice! The one I\'m using in a project is glibcoro:
https://github.com/ldo/glibcoro

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2019-08-23 22:10:20">23 Aug, 2019</time>

I hadn\'t discovered glibcoro when looking for other implementations.
From a quick look at the code, it only implements a subset of the
AbstractEventLoop API. In particular it omits all of the networking
related methods, which would rule it out for the project I\'ve been
working on.

---
