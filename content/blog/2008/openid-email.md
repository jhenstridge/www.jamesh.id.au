---
title: 'Using email addresses as OpenID identities (almost)'
slug: openid-email
date: 2008-04-02T16:25:46+08:00
tags: ['OpenID']
---

On the [OpenID](http://openid.net/) specs mailing list, there was
another discussion about using email addresses as OpenID identifiers. So
far it has mostly covered existing ground, but there was one comment
that interested me: a report that [you can log in to many OpenID RPs by
entering a Yahoo email
address](http://openid.net/pipermail/specs/2008-April/002274.html).

Now there certainly isn\'t any Yahoo-specific code in the standard
OpenID libraries, so you might wonder what is going on here. We can get
some idea by using the python-openid library:

    >>> from openid.consumer.discover import discover
    >>> claimed_id, services = discover('example@yahoo.com')
    >>> claimed_id
    'http://www.yahoo.com/'
    >>> services[0].type_uris
    ['http://specs.openid.net/auth/2.0/server',
     'http://specs.openid.net/extensions/pape/1.0']
    >>> services[0].server_url
    'https://open.login.yahooapis.com/openid/op/auth'
    >>> services[0].isOPIdentifier()
    True

So we can see that running the discovery algorithm on the email address
has resulted in Yahoo\'s standard identifier select endpoint. What
we\'ve actually seen here is the effect of [Section
7.2](http://openid.net/specs/openid-authentication-2_0.html#normalization)
at work:

> 3\. Otherwise, the input SHOULD be treated as an http URL; if it does
> not include a \"http\" or \"https\" scheme, the Identifier MUST be
> prefixed with the string \"http://\".

So the email address is normalised to the URL <http://example@yahoo.com>
(which is treated the same as <http://yahoo.com/>), which is then used
for discovery. As shown above, this results in an identifier select
request so works for all Yahoo users.

I wonder if the Yahoo developers realised that this would happen and set
things up accordingly? If not, then this is a happy accident. It isn\'t
quite the same as having support for email addresses in OpenID since the
user may end up having to enter their email address a second time in the
OP if they don\'t already have a session cookie.

It is certainly better than the RP presenting an error if the user
accidentally enters an email address into the identity field. It seems
like something that any OP offering email addresses to its users should
implement.

---
### Comments:
#### [Kevin Turner](http://kevin.janrain.com/) - <time datetime="2008-04-03 02:47:42">3 Apr, 2008</time>

The thing to keep in mind though is this is currently an accident, and
not a supported use case. The HTTP-fetching code in many OpenID
implementations doesn\'t really know what to do with the user@ part of
the URL, i.e. it\'ll try to use it as a hostname instead of translating
it to parameters for basic auth, and it\'ll break.

So you\'re better off just typing in \"yahoo.com\", really.

---
#### [Armin Ronacher](http://lucumr.pocoo.org/) - <time datetime="2008-04-03 04:24:19">3 Apr, 2008</time>

That\'s against the spec though. HTTP URLs must not have a
authentification part. That\'s reserved for FTP and some others.

---
#### James Henstridge - <time datetime="2008-04-03 12:10:02">3 Apr, 2008</time>

Kevin: I agree that typing \"yahoo.com\" is easier and what users should
be directed to use. I just found it interesting that an approximation of
the user\'s intent happens if they enter their email address.

Armin: it is true that the HTTP RFC doesn\'t specify handling of the
userinfo portion of the authority section, but does seem to be supported
by most implementations (they probably do URI generic syntax processing
before any HTTP-specific processing). I agree that this isn\'t the sort
of thing that you\'d want to start relying on, but it is nice that it
half works though.

---
#### [Chris Cunningham](http://blondechris.com/) - <time datetime="2008-04-03 21:21:24">3 Apr, 2008</time>

> I agree that this isn't the sort of thing that you'd want to start
> relying on

That\'d be why you wouldn\'t be wanting to implicitly condone it.

\- Chris

---
#### James Henstridge - <time datetime="2008-04-04 16:05:22">4 Apr, 2008</time>

Chris: I\'m not arguing that providers should tell their users to enter
email addresses into OpenID forms: giving them a shorter constant string
is definitely the better option.

However if users do enter their email address anyway, if it is possible
to give the desired behaviour why not do so?

---
