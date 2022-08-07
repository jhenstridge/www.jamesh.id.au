---
title: 'HTTP code in GWeather'
slug: http-code-in-gweather
date: 2005-06-30T09:19:18+08:00
draft: false
tags: ['Gnome']
---

One of the things that pisses me off about `gweather` is that it
occasionally hangs and stops updating. It is a bit easier to tell when
this has occurred these days, since it is quite obvious something\'s
wrong if gweather thinks it is night time when it clearly isn\'t.

The current code uses `gnome-vfs`, which isn\'t the best choice for this
sort of thing. The code is the usual mess you get when turning an
algoithm inside out to work through callbacks in C:

1.  One function opens the URL with `gnome_vfs_async_open()`.
2.  The callback that gets triggered on completion of the open calls
    `gnome_vfs_async_read()`.
3.  The callback that gets triggered on the end of the read checks the
    status. If it is at the end of the stream, then process the data and
    close the stream. Otherwise, perform another read (which will loop
    back to this step).

This logic is repeated 5 times for the different weather data sources.
To clean this up, I started looking at `libsoup` which doesn\'t try to
be a full file system abstraction, but provides a better API for the
kind of things gweather does.

I put together a simple `HttpResource` class that wraps the relevant
parts of `libsoup` for apps like gweather. It can be used like so:

1.  Create an `HttpResource` instance for the given URI.
2.  Connect a handler to the resource\'s `updated` signal.
3.  Call the `_set_update_interval()` method to say how often the
    resource should be checked.
4.  Call the `_refresh()` method to kick off periodic freshness checks.
5.  When new data arrives, the `updated` signal is emitted.

Since the code is designed for periodic updates, I added some simple
caching behaviour. If the server reports that the resource hasn\'t been
modified, we don\'t need to emit the `updated` signal.

There are a few things that still need doing:

-   Some code to keep a `SoupSession` instance up to date with the proxy
    configuration settings in GConf.
-   Correct handling of the `Expires:` response header. If we are
    checking for updates every 30 minutes, but the server says the
    current weather report is current for the next hour, then we
    shouldn\'t check again til then.
-   Support `gzip` and/or `deflate` content transfer encoding to reduce
    bandwidth.

This code should be pretty trivial to integrate into gweather when it is
done, and should simplify the logic. I guess it would be useful for
other applets too, such as `gtik`. The current code is available in my
[Bazaar](http://bazaar.canonical.com/) archive:

>     baz get http://www.gnome.org/~jamesh/arch/james@jamesh.id.au/http-resource--devel--0
