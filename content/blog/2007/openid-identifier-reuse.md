---
title: 'Identifier Reuse in OpenID 2.0'
slug: openid-identifier-reuse
date: 2007-11-11T23:15:41+09:00
tags: ['OpenID']
---

One of the issues that the OpenID 1.1 specification did not cover is the
fact that an identity URL may not remain the property of a user over
time. For large OpenID providers there are two cases they may run into:

1.  A user with a popular user name stops using the service, and they
    want to make that name available to new users.
2.  A user changes their user name. This may be followed by someone
    taking over the old name.

In both cases, RPs would like some way to tell the difference between
two different users who present the same ID at different points in time.

The traditional method of solving this problem is to assign two
identifiers to a user: a human friendly identifier and a persistent
identifier (e.g. a UNIX user ID, a database row ID, etc). At any point
in time, the human friendly identifier will point to a particular
persistent identifier, but over time the relationship may not hold.
Whenever a human-friendly identifier is presented, it is transformed to
its persistent counterpart before storage.

With OpenID 1.1, Relying Parties are expected to use the canonicalised
form of what the user enters to identify them. It is possible to
redirect the human friendly identifier to a persistent one, but that is
not particularly nice if you are trying to co-locate the user\'s home
page and OpenID.

**OpenID 2.0: XRIs**

The only solution to this problem in earlier drafts of OpenID 2.0 was to
use XRIs. When resolving an XRI, the resulting XRDS document includes a
persistent identifier in the `` element.

For example, resolving \"=foo\" gives us a canonical ID of
\"=!4EFC.841C.8012.E2F8\". If a user logs in to an RP with the former,
the RP will record the latter. This means the following:

1.  If the user stops paying their \$12/year and someone else registers
    \"=foo\", that new user will have a different persistent ID so
    won\'t be able to assume the identity.
2.  If the user registers another XRI pointing at the same persistent
    identifier, it will be considered equivalent.

**OpenID 2.0: URL identifiers**

But if you want to use URLs as identifiers, how do you solve the
problem?

One solution that was shot down was to allow the `<CanonicalID>` element
in the XRDS document for a URL OpenID. Apparently this was rejected
because it would result in another round trip during the discovery
process to find the endpoint for the persistent ID.

Instead, a feature was added to help detect the case where an identifier
was recycled. As part of the positive authentication response, an OP is
allowed to modify the claimed ID to include a fragment URI component. If
the identifier gets reassigned, the OP is expected to return a different
fragment.

This solves problem (1) but not problem (2). As it stands, the OpenID
2.0 specification doesn\'t provide much guidance in letting a user
change their human friendly URL identifier while maintaining the same
identity.

**A Solution**

One solution to this problem is to make use of the directed identity
feature of OpenID 2.0. Rather than making the user\'s homepage their
identifier, make it an OP identifier URL. This lets the OP decide on the
final claimed identifier.

This allows the user to enter their home page (e.g.
http://example.com/james), and have the RP record a persistent
identifier (e.g. http://example.com/id/42). If the user changes their
human friendly identifier, they\'ll still be able to use existing
services.

This solution does have a few downsides though:

-   Users can log in with any other user\'s homepage URL since they all
    point at the same OP.
-   Supporting both OpenID 1.1 and 2.0 on the same URL will likely cause
    confusion, since 1.1 requests would record the human friendly
    identifier and 2.0 requests record the persistent identifier. If an
    RP upgraded to the 2.0 protocol, the user would appear to be a
    different person (which is one of the problems we are trying to
    avoid).

So it seems that there isn\'t a good solution if you need to support
OpenID 1.1. If anyone else has ideas, I\'d be glad to hear them.

---
### Comments:
#### [Tassos Bassoukos](http://tassos.blogentis.net) - <time datetime="2007-11-12 13:55:19">12 Nov, 2007</time>

Wouldn\'t your solution invalidate one of the major use-cases of OpenID,
the \'you need only one identifier\' one?

---
#### James Henstridge - <time datetime="2007-11-13 06:15:55">13 Nov, 2007</time>

Tassos: I don\'t think anything I\'ve suggested breaks the \"single
digital identity\" idea of OpenID.

As I said above, the main questions are (1) how to avoid someone else
assuming an identity on OPs that allow identifier reuse and (2) on
systems that allow a user to change their human-friendly identifier, can
the user maintain their identity?

---
#### [Gary Krall](http://pip.verisignlabs.com) - <time datetime="2007-11-13 08:17:18">13 Nov, 2007</time>

James: By way of introduction I am the technical director for the
PiP/SeatBelt products here at Verisign. I read with interest your
article and I thought I would share with you what Verisign does. On the
PiP we do not allow identifers to ever be re-used. Once an identifier
has been claimed by a user we never allow for that to be re-issued in
the system.

Just thought you\'d be interested.

---
#### [atom](http://www.allentom.com) - <time datetime="2007-11-13 08:41:39">13 Nov, 2007</time>

Identifier Recycling is an issue that all large identity providers face,
and freeing up desirable usernames that aren\'t being actively used is
always a high priority.

Section 11.5.1 of Draft 12 of the OpenID 2.0 spec recommends that OPs
assign a unique url fragment to an OpenID url that changes when the
OpenID changes ownership.

I believe that if the OP of http://example.com/james responded with
http://example.com/id/42, the RP would be required to preform discovery
on http://example.com/id/42 to verify that the OP is authorized to make
claims about http://example.com/id/42. This will add an extra round
trip, adding more latency to the signin process. See section 11.2 for
more info. I don\'t believe that using url fragments as generation
identifiers will require an extra round trip.

---
#### James Henstridge - <time datetime="2007-11-13 21:14:32">13 Nov, 2007</time>

Garry: thanks for the info. That gets rid of the reuse problem, but does
not address the renaming issue.

Atom: I do realise that processing would require an additional round
trip \-- I said as much in the article. Given that it wouldn\'t affect
things in the general case where is not used, I don\'t really agree that
this is reason enough to reject it.

For instance, it requires no more round trips than the directed identity
mode, and that is included in the specification.

---
#### Roman Beslik - <time datetime="2007-11-15 09:45:26">15 Nov, 2007</time>

\>If the user registers another XRI pointing at the same persistent
identifier, it will be considered equivalent.

Does it mean that I can write under someone's name? Assuming that I've
registered an XRI pointing to someone's persistent identifier.

---
#### James Henstridge - <time datetime="2007-11-15 09:57:36">15 Nov, 2007</time>

Roman: my understanding is that there are a few things preventing this:

1\. the XRI registry probably won\'t let you do that.

2\. if you could do that, you probably wouldn\'t be able to authenticate
using the XRI. This is roughly equivalent to copying the openid.\* meta
tags from someone else\'s web page \-- you would be creating a new
OpenID for the other user, not creating a way to impersonate them.

You\'d be better off asking an XRI expert about this though. I have not
read much about the implementation details.

---
#### [James Henstridge &raquo; OpenID 2.0 Specification Approved](openid-20-specification-approved.md) - <time datetime="2007-12-10 12:38:57">10 Dec, 2007</time>

\[\...\] stated previously that I think the support for identifier reuse
with respect to URL identifiers is a bit lacking. \[\...\]

---
