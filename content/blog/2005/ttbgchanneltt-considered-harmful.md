---
title: '&lt;tt&gt;bgchannel://&lt;/tt&gt; Considered Harmful?'
slug: ttbgchanneltt-considered-harmful
date: 2005-05-10T06:31:42+08:00
draft: false
tags: ['Gnome']
---

Recently [Bryan](http://www.gnome.org/~clarkbw/blog/) posted about
[background
channels](http://www.gnome.org/~clarkbw/blog/GNOME/background_channels)
\-- a system for automatic updating desktop wallpaper. One of the
features of the design is a new URI scheme based on the same ideas as
`webcal://`, which I think is a bad idea (as [dobey has also pointed
out](http://primates.ximian.com/~dobey/?date=2005-05-07-02)).

The usual reasoning for creating a URI scheme like this go something
like this:

1.  You want to be able to perform some action when a link in a web page
    is clicked.
2.  The action requires that you know the URI of the link (usually to
    allow contacting the original server again).
3.  When the web browser activates a helper application bound to a MIME
    type, you just get the path to a saved copy of the resource, which
    doesn\'t satisfy (2).
4.  Helper applications for URI types get passed the full URI.

So the solution taken with Apple\'s iCal and Bryan\'s background
channels is to strip the `http:` off the start of resource\'s URI, and
replace it with a custom scheme name. This works pretty well for the
general case, but causes problems for a few simple use cases that\'ll
probably turn out to be more common than you think:

-   Serving a background channel (or calendar, or whatever) via a
    protocol other than `http`. The first alternative protocol you\'ll
    probably run into is `https`, but there may be other protocols you
    want to support in the future.
-   Any links to a background channel will need to be fully qualified
    since they use a different scheme. If you move your site, you\'ll
    need to update every page that links to the background channel. If
    you could use relative URIs in the links, this wouldn\'t be the
    case.

One alternative to the \"new URI scheme\" solution, that doesn\'t suffer
from the above problems is to serve a \"locator file\" from the web
server that contains the information needed to request the real
information. Even though the helper application will only get the path
of a temporary file, the content of the file lets the app connect to the
server. This is the approach taken by BitTorrent, and various media
players like RealPlayer.

The separate \"locator file\" can even be omitted by placing the
background channel location inside the background channel itself. This
is the approach taken for
[Atom](http://www.ietf.org/html.charters/atompub-charter.html), via a
`<link rel="self"/>` link.
