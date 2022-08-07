---
title: 'OpenID 2.0 Specification Approved'
slug: openid-20-specification-approved
date: 2007-12-10T13:38:39+09:00
draft: false
tags: ['OpenID']
---

It looks like the [OpenID Authentication
2.0](http://openid.net/specs/openid-authentication-2_0.html)
specification has finally been released, along with [OpenID Attribute
Exchange
1.0](http://openid.net/specs/openid-attribute-exchange-1_0.html). While
there are some questionable features in the new specification (namely
XRIs), it seems like a worthwhile improvement over the previous
specification. It will be interesting to see how quickly the new
specification gains adoption.

While this is certainly an important milestone, there are still areas
for improvement.

**Best Practices For Managing Trust Relationships With OPs**

The proposed [Provider Authentication Policy
Extension](http://openid.net/specs/openid-provider-authentication-policy-extension-1_0-02.html)
allows a Relying Party to specify what level of checking it wants the
OpenID Provider to perform on the user (e.g. phishing resistant, multi
factor, etc). The OP can then tell the RP what level of checking was
actually performed.

What the specification doesn\'t cover is why the RP should believe the
OP. I can easily set up an OP that performs no checking on the user but
claims that it performed \"Physical Multi-Factor Authentication\" in its
responses. Any RP that acted on that assertion would be buggy.

This isn\'t to say that the extension is useless. If the entity running
the RP also runs the OP, then they might have good reason to believe the
responses and act on them. Similarly, they might decide that
[JanRain](http://janrain.com/) are quite trustworthy so believe
responses from [myOpenID](https://www.myopenid.com/).

What is common in between these situations is that there is a trust
relationship between the OP and RP that is outside of the protocol. As
the specification gives no guidance on how to set up these
relationships, they are likely to be ad-hoc and result in some OpenIDs
being more useful than others.

At a minimum, it\'d be good to see some best practices document on how
to handle this.

**Trusted Attribute Exchange**

As mentioned in my previous article on [OpenID Attribute
Exchange](http://blogs.gnome.org/jamesh/2007/11/26/openid-ax/), I
mentioned that attribute values provided by the OP should be treated as
being self asserted. So if the RP receives an email address or Jabber ID
via attribute exchange, there is no guarantee that the user actually
owns them. This is a problem if the RP wants to start emailing or
instant messaging the user (e.g. OpenID enabled mailing list management
software). Assuming the RP doesn\'t want to get users to revalidate
their email address, what can it do?

One of the simplest solutions is to use a trust relationship with the
OP. If the RP knows that the OP will only transfer email addresses if
the user has previously verified them, then they need not perform a
second verification. This leaves us in the same situation as described
in the previous situation.

Another solution that has been proposed by [Sxip](http://www.sxip.com/)
is to make the attribute values self-asserting. This entails making the
attribute value contain both the desired information plus a digital
signature. Using the email example, if the email address has a valid
digital signature and the RP trusts the signer to perform email address
verification, then it can accept the email address without further
verification.

This means that the RP only needs to manage trust relationships with the
attribute signers rather than every OP used by their user base. If there
are fewer attribute signers than OPs then this is of obvious benefit to
the RP. It also benefits the user since they no longer limited to one of
the \"approved\" OPs.

**Canonical IDs for URL Identifiers**

I\'ve [stated
previously](http://blogs.gnome.org/jamesh/2007/11/11/openid-identifier-reuse/)
that I think the support for identifier reuse with respect to URL
identifiers is a bit lacking.  It\'d be nice to see it expanded in a
future specification revision.

---
### Comments:
#### [OpenID](http://vanirsystems.com/danielsblog/2007/12/11/openid/) - <time datetime="2007-12-12 02:54:51">3 Dec, 2007</time>

\[\...\] James Henstridge gives an in depth account of the differences
in his blog post titled "OpenID 2.0", with some additional information
in his more recent post titled "OpenID 2.0 Specification Approved".
\[\...\]

---
#### [PROGRAMAS LIVRES &raquo; OpenID 2.0 aprovado](http://www.programaslivres.net/2007/12/14/openid-20-aprovado/) - <time datetime="2007-12-15 05:20:25">6 Dec, 2007</time>

\[\...\] aprovadas as especificações do OpenID \[\...\]

---
