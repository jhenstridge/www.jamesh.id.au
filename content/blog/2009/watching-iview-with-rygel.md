---
title: 'Watching iView with Rygel'
slug: watching-iview-with-rygel
date: 2009-07-06T16:50:45+08:00
tags: ['Gnome', 'Python', 'UPnP']
---

One of the features of [Rygel](http://live.gnome.org/Rygel) that I found
most interesting was the [external media server
support](http://live.gnome.org/Rygel/MediaServerSpec). It looked like
an easy way to publish information on the network without implementing a
full UPnP/DLNA media server (i.e. handling the UPnP multicast traffic,
transcoding to a format that the remote system can handle, etc).

As a small test, I put together a server that exposes the
[ABC](http://www.abc.net.au/)\'s [iView](http://www.abc.net.au/iview/)
service to UPnP media renderers. The result is a bit rough around the
edges, but the basic functionality works. The source can be grabbed
using Bazaar:

    bzr branch lp:~jamesh/+junk/rygel-iview

It needs Python, [Twisted](http://twistedmatrix.com/), the [Python
bindings for
D-Bus](http://www.freedesktop.org/wiki/Software/DBusBindings) and
[rtmpdump](http://lkcl.net/rtmp/) to run. The program exports the guide
via D-Bus, and uses rtmpdump to stream the shows via HTTP. Rygel then
publishes the guide via the UPnP media server protocol and provides
MPEG2 versions of the streams if clients need them.

There are still a few rough edges though. The video from iView comes as
640x480 with a 16:9 aspect ratio so has a 4:3 pixel aspect ratio, but
there is nothing in the video file to indicate this (I am not sure if
flash video supports this metadata).

**Getting Twisted and D-Bus to cooperate**

Since I\'d decided to use Twisted, I needed to get it to cooperate with
the D-Bus bindings for Python. The first step here was to get both
libraries using the same event loop. This can be achieved by setting
Twisted to use the glib2 reactor, and enabling the glib mainloop
integration in the D-Bus bindings.

Next was enabling asynchronous D-Bus method implementations. There is
support for this in the D-Bus bindings, but has quite a different (and
less convenient) API compared to Twisted. A small decorator was enough
to overcome this impedence:

    from functools import wraps

    import dbus.service
    from twisted.internet import defer

    def dbus_deferred_method(*args, **kwargs):
        def decorator(function):
            function = dbus.service.method(*args, **kwargs)(function)
            @wraps(function)
            def wrapper(*args, **kwargs):
                dbus_callback = kwargs.pop('_dbus_callback')
                dbus_errback = kwargs.pop('_dbus_errback')
                d = defer.maybeDeferred(function, *args, **kwargs)
                d.addCallbacks(
                    dbus_callback, lambda failure: dbus_errback(failure.value))
            wrapper._dbus_async_callbacks = ('_dbus_callback', '_dbus_errback')
            return wrapper
        return decorator

This decorator could then be applied to methods in the same way as the
`@dbus.service.method` method, but it would correctly handle the case
where the method returns a Deferred. Unfortunately it can\'t be used in
conjunction with `@defer.inlineCallbacks`, since the D-Bus bindings
don\'t handle varargs functions properly. You can of course call another
function or method that uses `@defer.inlineCallbacks` though.

**The iView Guide**

After coding this, it became pretty obvious why it takes so long to load
up the iView flash player: it splits the guide data over almost 300 XML
files. This might make sense if it relied on most of these files
remaining unchanged and stored in cache, however it also uses a
cache-busting technique when requesting them (adding a random query
component to the URL).

Most of these files are series description files (some for finished
series with no published programs). These files contain a title, a
short description, the URL for a thumbnail image and the IDs for the
programs belonging to the series. To find out about those programs, you
need to load all the channel guide XML files until you find which one
contains the program. Going in the other direction, if you\'ve got a
program description from the channel guide and want to know about the
series it belongs to (e.g. to get the thumbnail), you need to load each
series description XML file until you find the one that contains the
program. So there aren\'t many opportunities to delay loading of parts
of the guide.

The startup time would be a lot easier if this information was collapsed
down to a smaller number of larger XML files.

---
### Comments:
#### [Jeremy](http://jeremy.visser.name/) - <time datetime="2009-07-06 18:18:48">6 Jul, 2009</time>

Totally agree with you about the XML files. I myself did a similar thing
\-- found out about the whole XML file hierarchy, demixing the RTMP
streams, and the glorious 640x480 16:9 aspect ratio.

Wrote a simple PyGTK app to scrape and parse these (I used
BeautifulSoup), but your implementation is way better, so I\'d be
ashamed to share my code. ;)

---
