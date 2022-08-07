---
title: 'HTTP resource watcher'
slug: http-resource-watcher
date: 2005-07-11T14:13:00+08:00
draft: false
tags: ['Gnome']
---

I\'ve got most of the features of my HTTP resource watching code I was
working on for GWeather done. The main benefits over the existing
gnome-vfs based code are:

-   Simpler API. Just connect to the `updated` signal on the resource
    object, and you get notified when the resource changes.
-   Supports `gzip` and `deflate` content encodings, to reduce bandwidth
    usage.
-   Keeps track of `Last-Modified` date and `Etag` value for the
    resource so that it can do conditional `GET`s of the resource for
    simple client side caching.
-   Supports the `Expires` header. If the update interval is set at 30
    minutes but the web server says that the it won\'t be updated for an
    hour, then use the longer timeout til the next check.
-   If a permanent redirect is received, then the new URI is used for
    future checks.
-   If a `410 Gone` response is received, then future checks are not
    queued (they can be restarted with a `refresh()` call).

I\'ve also got some code to watch the HTTP proxy settings in GConf, but
that seems to trigger a hang in libsoup ([bug
309867](http://bugzilla.gnome.org/show_bug.cgi?id=309867 "proxy_uri from a GConfClient notify callback")).

While I wrote the code for use in GWeather, it could be quite useful for
other tasks that require watching an HTTP resource such as:

-   HTTP calendar backend of `evolution-data-server`.
-   A stock ticker applet like `gtik`.
-   Possibly an RSS reader.

The code is available in my [Bazaar](http://bazaar.canonical.com/)
archive:

>     baz get http://www.gnome.org/~jamesh/arch/james@jamesh.id.au/http-resource--devel--0

---
### Comments:
#### [Grahame Bowland](http://grahame.angrygoats.net/) - <time datetime="2005-08-19 03:09:11">5 Aug, 2005</time>

Nice :-)

Will Davyd let you commit it? It sounds pretty neat. It\'s a bit of a
shame gnome-vfs is so gross :P\

---
