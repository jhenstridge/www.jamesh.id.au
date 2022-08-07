---
title: 'Thoughts on OAuth'
slug: thoughts-on-oauth
date: 2008-10-23T11:46:53+08:00
tags: ['OAuth', 'OpenID', 'Python']
---

I\'ve been playing with [OAuth](http://oauth.net/) a bit lately. The
OAuth specification fulfills a role that some people saw as a failing of
[OpenID](http://openid.net/): programmatic access to websites and
authenticated web services. The expectation that OpenID would handle
these cases seems a bit misguided since the two uses cases are quite
different:

-   OpenID is designed on the principle of letting arbitrary OpenID
    providers talk to arbitrary relying parties and vice versa.
-   OpenID is intentionally vague about how the provider authenticates
    the user. The only restriction is that the authentication must be
    able to fit into a web browsing session between the user and
    provider.

While these are quite useful features for a decentralised user
authentication scheme, the requirements for web service authentication
are quite different:

-   There is a tighter coupling between the service provider and client.
    A client designed to talk to a photo sharing service won\'t have
    much luck if you point it at a micro-blogging service.
-   Involving a web browser session in the authentication process for
    individual web service request is not a workable solution: the
    client might be designed to run offline for instance.

While the idea of a universal web services client is not achievable,
there are areas of commonality between different the services: gaining
authorisation from the user and authenticating individual requests. This
is the area that OAuth targets.

While it has different applications, it is possible to compare some of
the choices made in the protocol:

1.  The secrets for request and access tokens are sent to the client in
    the clear. So at a minimum, a service provider\'s request token URL
    and access token URL should be served over SSL. OpenID nominally
    avoids this by using [[Diffie-Hellman Key
    Exchange](http://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange)
    to avoid evesdropping, but ended up needing it to avoid man in the
    middle attacks. So sending them in the clear is probably a more
    honest approach.]{.info}
2.  Actual web service methods can be authenticated over plain HTTP in a
    fairly secure means using the HMAC-SHA1 or RSA-SHA1 signature
    methods. Although if you\'re using SSL anyway, the PLAINTEXT
    authentication method is probably not any worse than HMAC-SHA1.
3.  The authentication protocol supports both web applications and
    desktop applications. Though any security gained through consumer
    secrets is invalidated for desktop applications, since anyone with a
    copy of the application will necessarily have access to the secrets.
    A few other points follow on from this:
    -   [The RSA-SHA1 signature method is not appropriate for use by
        desktop applications. The signature is based only on information
        available in the web service request and the RSA key associated
        with the consumer, and the private key will need to be
        distributed as part of the application. So if an attacker
        discovers an access token (not access token secret), they can
        authenticate.]{.info}
    -   The other two authentication methods --- HMAC-SHA1 and
        PLAINTEXT --- depend on an access token secret. Along with the
        access token, this is essentially a proxy for the user name and
        password, so should be protected as such (e.g. via the [GNOME
        keyring](http://live.gnome.org/GnomeKeyring)).  It still sounds
        better than storing passwords directly, since the token won\'t
        give access to unrelated sites the user happened to use the same
        password on, and can be revoked independently of changing the
        password.
4.  While the OpenID folks found a need for a formal extension mechanism
    for version 2.0 of that protocol, nothing like that seems to have
    been added to OAuth.  There are now a number of proposed extensions
    for OAuth, so it probably would have been a good idea.  Perhaps it
    isn\'t as big a deal, due to tigher coupling of service providers
    and consumers, but I could imagine it being useful as the two
    parties evolve over time.

So the standard seems decent enough, and better than trying to design
such a system yourself.  Like OpenID, it\'ll probably take until the
second release of the specification for some of the ambiguities to be
taken care of and for wider adoption.

From the Python programmer point of view, things could be better.  The
library available from the OAuth site seems quite immature and lacks
support for a few aspects of the protocol.  It looks okay for simpler
uses, but may be difficult to extend for use in more complicated
projects.
