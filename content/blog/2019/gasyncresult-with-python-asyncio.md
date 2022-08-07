---
title: 'Using GAsyncResult APIs with Python''s asyncio'
slug: gasyncresult-with-python-asyncio
date: 2019-10-07T23:08:17+08:00
tags: ['asyncio', 'glib', 'Python']
---

With a [GLib implementation of the Python asyncio event
loop](https://blogs.gnome.org/jamesh/2019/08/05/glib-integration-for-python-asyncio/),
I can easily mix asyncio code with GLib/GTK code in the same thread. The
next step is to see whether we can use this to make any APIs more
convenient to use. A good candidate is APIs that make use of
`GAsyncResult`.

These APIs generally consist of one function call that initiates the
asynchronous job and takes a callback. The callback will be invoked
sometime later with a `GAsyncResult` object, which can be passed to a
\"finish\" function to convert this to the result type relevant to the
original call. This sort of API is a good candidate to convert to an
asyncio coroutine.

We can do this by writing a ready callback that simply stores the result
in a future, and then have our coroutine await that future after
initiating the job. For example, the following will asynchronously
connect to the session bus:

\[code lang=\"python\"\]\
import asyncio\
from gi.repository import GLib, Gio

async def session\_bus():\
loop = asyncio.get\_running\_loop()\
bus\_ready = loop.create\_future()\
def ready\_callback(obj, result):\
try:\
bus = Gio.bus\_get\_finish(result)\
except GLib.Error as exc:\
loop.call\_soon\_threadsafe(bus\_ready.set\_exception, exc)\
return\
loop.call\_soon\_threadsafe(bus\_ready.set\_result, bus)

Gio.bus\_get(Gio.BusType.SESSION, None, ready\_callback)\
return await bus\_ready\
\[/code\]

We\'ve now got an API that is conceptually as simple to use as the
synchronous `Gio.bus_get_sync` call, but won\'t block other work the
application might be performing.

Most of the code is fairly straight forward: the main wart is the two
`loop.call_soon_threadsafe calls`. While everything is executing in the
same thread, my asyncio-glib library does not currently wake the asyncio
event loop when called from a GLib callback. The `call_soon_threadsafe`
method does the trick by generating some dummy IO to cause a wake up.

**Cancellation**

One feature we\'ve lost with this wrapper is the ability to cancel the
asynchronous job. On the GLib side, this is handled with the
`GCancellable` object. On the asyncio side, tasks are cancelled by
injecting an `asyncio.CancelledError` exception into the coroutine. We
can propagate this cancellation to the GLib side fairly seamlessly:

\[code language=\"python\"\]\
async def session\_bus():\
\...\
cancellable = Gio.Cancellable()\
Gio.bus\_get(Gio.BusType.SESSION, cancellable, ready\_callback)\
try:\
return await bus\_ready\
except asyncio.CancelledError:\
cancellable.cancel()\
raise\
\[/code\]

It\'s important to re-raise the `CancelledError` exception, so that it
will propagate up to any calling coroutines and let them perform their
own cleanup.

By following this pattern I was able to build enough wrappers to let me
connect to the D-Bus daemon and issue asynchronous method calls without
needing to chain together large sequences of callbacks. The wrappers
were all similar enough that it shouldn\'t be too difficult to factor
out the common code.
