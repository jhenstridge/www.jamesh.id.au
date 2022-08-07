---
title: 'ZeroConf support for Bazaar'
slug: zeroconf-support-for-bazaar
date: 2007-03-25T18:05:58+08:00
draft: false
tags: ['Avahi', 'Bazaar', 'Gnome', 'Python']
---

When at conferences and sprints, I often want to see what someone else
is working on, or to let other people see what I am working on. Usually
we end up pushing up to a shared server and using that as a way to
exchange branches. However, this can be quite frustrating when competing
for outside bandwidth when at a conference.

It is possible to share the branch from a local web server, but that
still means you need to work out the addressing issues.

To make things easier, I wrote a simple [Bazaar/Avahi
plugin](https://launchpad.net/bzr-avahi). It provides a command
\"`bzr share`\", which does the following:

-   Scan the directory for any Bazaar branches it contains.
-   Start up the Bazaar server to listen on a TCP port and share the
    given directory.
-   Advertise each of the branches via mDNS using
    [Avahi](http://avahi.org/). They are shared using the branch
    nickname.

For the client side, the plugin implements a \"`bzr browse`\" command
that will list the Bazaar branches being advertised on the local network
(the name and the `bzr://` URL). Using the two commands together, it is
trivial to share branches locally or find what branches people are
sharing.

I am not completely satisfied with how things work, and have a few ideas
for how to improve things:

1.  Provide a dummy transport that lets people pull from branches by
    their advertised service name. This would essentially just redirect
    from `scheme://$SERVICE/` to `bzr://$HOST:$PORT/$PATH`.
2.  Maybe provide more control over the names the branches get
    advertised with. Perhaps this isn\'t so important though.
3.  Make \"`bzr share`\" start and stop advertising branches as they get
    added/removed, and handle branch nicknames changing (at this point,
    it is pretty much blue sky though).
4.  Perhaps some form of access control. I\'m not sure how easy this is
    within the smart server protocol, but it should be possible to query
    the user over whether to accept a connection or not.

It will be interesting to see how well this works at the next sprint or
conference.

---
### Comments:
#### [Pharao](http://blog.hopelesscom.de) - <time datetime="2007-03-26 03:38:28">1 Mar, 2007</time>

just great - thanks :)

---
#### Christopher - <time datetime="2007-03-26 04:42:50">1 Mar, 2007</time>

Excellent idea!

---
#### glatzor - <time datetime="2007-03-26 07:51:55">1 Mar, 2007</time>

I already love your plugin!

---
#### Michael Scherer - <time datetime="2007-03-26 17:57:58">1 Mar, 2007</time>

This seems like svl, a svk layer providing the same feature for svk. You
should take a look to see if there is some interesting concept to
implement. Too bad that svl developpement is stalled.

---
#### Michael Scherer - <time datetime="2007-03-26 17:58:22">1 Mar, 2007</time>

Oups, forgot the url to svl :
<http://search.cpan.org/~abergman/SVL-0.29/>

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-03-26 18:25:39">1 Mar, 2007</time>

Michael: I think a lot of the SVL features are already part of the
Bazaar core. My code basically just instantiates the existing Bazaar
server implementation and does the mDNS advertisement.

That said, there is definitely room for improvement on the client side
for bzr-avahi. I have a few ideas about how to improve things mentioned
in the main article.

One of the new features of Bazaar is the concept of a unique tree root
ID. All related branches share the same tree root ID. If this is
included in the advertised data, it would allow the plugin to show only
the branches that could be merged to a particular target.

---
