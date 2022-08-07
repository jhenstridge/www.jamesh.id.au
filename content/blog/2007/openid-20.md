---
title: 'OpenID 2.0'
slug: openid-20
date: 2007-10-23T14:24:23+08:00
tags: ['OpenID']
---

Most people have probably seen or used [OpenID](http://openid.net/). If
you have used it, then it has most likely that it was with the 1.x
protocol. Now that OpenID 2.0 is [close to
release](http://openid.net/pipermail/specs/2007-October/002005.html)
(apparently they really mean it this time \...), it is worth looking at
the new features it enables. A few that have stood out to me include:

-   proper extension support
-   support for larger requests/responses
-   directed identity
-   attribute exchange extension
-   support for a new naming monopoly

I\'ll now discuss each of these in a bit more detail

**Extension Support**

OpenID 1.1 had one well known extension: the [Simple Registration
Extension](http://openid.net/specs/openid-simple-registration-extension-1_0.html "OpenID Simple Registration Extension 1.0").
An OpenID relying party (RP) would send a request with an
`openid.sreg.required` field, and get back user information in
`openid.sreg.*` fields from the OpenID Provider (OP). The RP and OP
would just need to know that \"`openid.sreg`\" fields means that the
simple registration extension is being used.

But what if I want to define my own extension? If my RP sends
`openid.foo.*` fields, how does the OP know that it refers to my
extension and not some other extension that happened to pick the same
prefix?

OpenID 2.0 solves this problem by borrowing the idea of name space URIs
from XML. If I am sending some `openid.foo.*` fields in an OpenID
message, then I also need to send an `openid.ns.foo` field set to a URI
that identifies the extension. This means that a message that sends the
same data as `openid.bar.*` fields should be treated the same provided
that `openid.ns.bar` is set to the extension\'s name space URI.

As with XML name spaces, this allows us to piggy back on top of DNS as a
way of avoiding conflicts.

**Large Requests and Responses**

OpenID 1.1 uses HTTP redirects as a way of transferring control between
the RP and OP (and vice versa). This means that the upper limit on a
message is effectively the same as the smallest upper limit on length of
URLs in common web browsers and servers. Internet Explorer seems to have
the lowest limit---[2,083
characters](http://support.microsoft.com/kb/208427 "Maximum URL length is 2,083 characters in Internet Explorer")---so
it sets the effective limit on message size.

For simple authentication checks (what OpenID was originally designed
for), this is not generally a problem. But once you start to introduce a
few extensions, this limit can easily be reached.

OpenID 2.0 allows messages to be sent as an HTTP POST body which
effectively removes the upper limit. The recommended way of achieving
this is by sending a page to the user\'s browser that contains a form
that posts to the appropriate endpoint and contains the data as hidden
form fields. The form would then get submitted by a JavaScript onload
handler.

**Directed Identity**

For OpenID 1.1, the authentication process goes something like this:

1.  the user enters their identity URL into a form on the RP
2.  the RP performs discovery on that URL to find the user\'s OP.
3.  the RP initiates an OpenID authentication request with that OP.

With OpenID 2.0, the discovery process may tell the RP that the URL
identifies the *OP* rather than the *user*. If this happens, the RP
proceeds with the authentication request using the special
\"http://specs.openid.net/auth/2.0/identifier\_select\" value as the
identity URL. The OP will then fill in the user\'s actual identity URL
in the subsequent authentication response. As an additional step, the RP
is then required to perform discovery on this URL to ensure that the OP
is entitled to authenticate it.

There are a number of cases where this feature can be useful:

1.  An OpenID provider can give their users a single URL that will work
    for everyone. For instance, if AOL sets things up correctly, you\'d
    be able to type \"aol.com\" into any OpenID 2.0 enabled site to [log
    in with an AIM screen
    name](http://dev.aol.com/aol-and-63-million-openids "AOL and 63 Million OpenIDs").
2.  A privacy concious user could configure their own OpenID provider
    that will hand out different identity URLs to different RPs, similar
    to how some people use single-purpose email addresses today.
3.  If an RP requires that users use a particular OP, they could use
    directed identity to begin the authentication request without
    requiring the user to enter an identity URL.

**Attribute Exchange Extension**

The [OpenID Attribute
Exchange](http://openid.net/specs/openid-attribute-exchange-1_0-07.html "OpenID Attribute Exchange 1.0 - Draft 07")
extension is like the simple registration extension on steroids. The
major differences are:

-   Unlike the simple registration extension, the attribute exchange
    extension does not have a fixed set of attributes that can be
    transmitted. Instead it uses URIs to identify the attribute types,
    making it easy to define new attributes without causing conflicts.
    Of course an attribute is not particularly useful if no one else
    supports it, so there is [a
    process](http://www.axschema.org/ "Schema for OpenID Attribute Exchange")
    set up to standardise common attribute types.
-   As well as receiving attribute values as part of an authentication
    response, an RP can request that an OP store certain attribute
    values. This is done as part of an authentication request, so the OP
    can verify that the user really wants to store the values.
-   The RP can request ongoing updates for the attributes it is
    interested in. As an example, if you stored your hackergotchi with
    your OP, changes to the image could be automatically pushed out to
    all sites you use that want to display that image.

**Prop Up A New Naming Monopoly**

With OpenID 2.0, a user is supposed to be able to enter an i-name in
place of an identity URL in an RP, and be authenticated against the
i-broker managing that name. So rather than entering an ugly URL, users
can enter an ugly string starting with \"=\" or \"@\".

All it costs to take advantage of this is US\$12 per year (or US\$55 for
an organisation name). They claim that it will be possible to use an
i-name in many contexts in the future, but for now it appears to be
limited to (1) a subset of OpenID RPs, (2) a web form that people can
use to send you emails and (3) an HTTP redirection to your website.

At this point, it seems that i-name support in OpenID is more important
to the i-name crowd than the OpenID crowd. That said, the complexity is
hidden by most of the existing OpenID libraries, so it\'ll most likely
get implemented by default on most RPs moving forward.

**Conclusion**

Overall OpenID 2.0 looks like a worthwhile upgrade, even if some parts
like i-names are questionable.

Assuming the attribute exchange extension takes off, it should provide a
much richer user experience. Imagine being able to update your shipping
address in one place when you move house and having all the online
retailers you use receive the updated address immediately. Or changing
your email address and having all the bugzilla instances you use pick up
the new address instantly (perhaps requiring you to verify the new
address first, of course).

The improved extension support should also make it easier for people to
experiment with new extensions without accidentally conflicting with
each other, which should accelerate development of new features.

---
### Comments:
#### [tenshu](http://www.tenshu.fr/) - <time datetime="2007-10-23 16:40:08">2 Oct, 2007</time>

Any news on openid support in and for launchpad?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-10-23 17:23:20">2 Oct, 2007</time>

Tenshu: we are working on supporting Launchpad as an OP. In fact,
http://shop.canonical.com/ is the first RP we set that makes use of it.
We don\'t have anything to announce about Launchpad as a general purpose
OP yet though.

When there is something to announce, it\'ll be through official channels
first though.

---
#### TG - <time datetime="2007-10-24 01:37:57">3 Oct, 2007</time>

Any word on when the inventors of openID (i.e. Livejournal) is actually
going to implement the protocol themselves? For the past years they\'ve
only had a half-assed implementation that doesn\'t even let you link
your openid to your journal. It just creates a new one with a weird
random name.

Isn\'t it bad advertisement that the creators won\'t even use their own
invention?

---
#### [J.B. Nicholson-Owens](http://digitalcitizen.info/) - <time datetime="2007-10-24 01:55:48">3 Oct, 2007</time>

I thought OpenID wasn\'t recommended to be used for sensitive
information like authenticating yourself to your bank. Wouldn\'t using
it for authentication with other commercial activities (like shops) come
under the same disrecommendation?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-10-24 09:51:17">3 Oct, 2007</time>

TG: Perhaps you should direct questions like that to Livejournal. It
doesn\'t seem accurate to say they don\'t implement the protocol though:
they provide an OP implementation for their users, and do make some
features available when acting as an RP.

J.B.: if the RP trusts that the OP will authenticate users properly and
has adequate security in place, there shouldn\'t be a problem with using
OpenID to authenticate. For the case of the Ubuntu shop, we are happy
with how Launchpad authenticates users.

---
#### Anonymous - <time datetime="2007-10-24 23:25:49">3 Oct, 2007</time>

I don\'t like the idea of i-names. Too centralized, and costs money.
Which are, quite frankly, against the principle of OpenID: The whole
idea of OpenID is that it\'s decentralized and easy to obtain.

---
#### [OpenID is not a provisioning engine](http://willnorris.com/2007/10/openid-is-not-a-provisioning-engine) - <time datetime="2007-10-30 16:11:56">2 Oct, 2007</time>

\[\...\] talking about the future possibilities of OpenID 2.0 and the
Attribute Exchange extension, James Henstridge \[\...\]

---
#### [Pushing String &raquo; Well-rounded identity for the whole person](http://www.xmlgrrl.com/blog/archives/2007/10/30/well-rounded-identity-for-the-whole-person/) - <time datetime="2007-10-30 22:52:36">2 Oct, 2007</time>

\[\...\] reading Will Norris's post OpenID is not a provisioning engine.
He riffs on a scenario from James Henstridge where you can propagate a
new shipping address to every service that needs to know it. (Actually,
I \[\...\]

---
#### John Bäckstrand - <time datetime="2007-11-06 23:13:06">2 Nov, 2007</time>

\"I don't like the idea of i-names. Too centralized, and costs money.
Which are, quite frankly, against the principle of OpenID: The whole
idea of OpenID is that it's decentralized and easy to obtain.\"

Ahemm, but doesn\'t OpenID depend on DNS? Which in turn is not free? :)

---
