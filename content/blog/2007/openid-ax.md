---
title: 'OpenID Attribute Exchange'
slug: openid-ax
date: 2007-11-26T17:18:03+09:00
draft: false
tags: ['OpenID', 'openid.ax']
---

In my [previous article on OpenID
2.0](http://blogs.gnome.org/jamesh/2007/10/23/openid-20/), I mentioned
the new [Attribute
Exchange](http://openid.net/specs/openid-attribute-exchange-1_0-08.html "OpenID Attribute Exchange 1.0 - Draft 08")
extension. To me this is one of the more interesting benefits of moving
to OpenID 2.0, so it deserves a more in depth look.

As mentioned previously, the extension is a way of transferring
information about the user between the OpenID provider and relying
party.

**Why use Attribute Exchange instead of FOAF or Microformats?**

Before deciding to use OpenID for information exchange, it is worth
looking at whether it is necessary at all.

There are existing solutions for transferring user data such as
[FOAF](http://www.foaf-project.org/) and the [hCard
microformat](http://microformats.org/wiki/hcard). As the relying party
already has the user\'s identity URL, it\'d be trivial to discover a
FOAF file or hCard content there. That said, there are some
disadvantages to this method:

1.  Any information published in this way is available to everyone. This
    might be fine for some classes of information (your name, a picture,
    your favourite colour), but not for others (your email address,
    phone number or similar).
2.  The same information is provided to all parties. Perhaps you want to
    provide different email addresses to work related sites.
3.  The RP needs to make an additional request for the data. If we can
    provide the information as part of the OpenID authentication
    request, it will reduce the number of round trips that need to be
    made. In turn, this should reduce the amount of time it takes to log
    the user in.

**Why use Attribute Exchange instead of the Simple Registration
extension?**

There already exists an OpenID extension for transferring user details
to the RP, in the form of the [Simple
Registration](http://openid.net/specs/openid-simple-registration-extension-1_1-01.html "OpenID Simple Registration Extension 1.1 - Draft 1")
extension. It has already been used in the field, and works with OpenID
1.1 too.

One big downside of SREG is that it only supports a limited number of
attributes. If you need to transfer more attributes, you basically have
two choices:

1.  use some other extension to transfer the remaining attributes
2.  make up some new attribute names to send with SREG and hope for the
    best.

The main problem with (2) is that there is no way to tell between your
own extensions to SREG and someone else\'s which will likely create
interoperability problems if when an attribute name conflict occurs. So
this solution is not a good idea outside of closed systems. This leaves
(1), for which Attribute Exchange is a decent choice.

**What can I do with Attribute Exchange?**

There are two primary operations that can be performed with the
extension:

1.  fetch some attribute values
2.  store some attribute values

Both operations are performed as part of an OpenID authentication
request. Among other things, this allows:

-   The OP to ask the user which requested attributes to send
-   If the OP has not stored values for the requested attributes, it
    could get the user to enter them in and store them for next time.
-   The OP could use a predefined policy to decide what to send the RP.
    One possibility would be to generate one-time email addresses
    specific to a particular RP.
-   For store requests, the OP can ask the user to confirm that they
    want to store the attributes.

**Fetching Attributes**

An attribute fetch request is a normal authentication request with a few
additional fields:

-   **openid.ax.mode**: this needs to be set to \"fetch\_request\"
-   **openid.ax.required**: a comma separated list of attribute aliases
    that the RP needs (note that this does not guarantee that the OP
    will return those attributes).
-   **openid.ax.if\_available**: a comma separated list of attribute
    aliases that the RP would like returned if available.
-   **openid.ax.type.*alias***: for each requested attribute alias, the
    URI identifying the attribute type
-   **openid.ax.count.*alias***: the number of values the RP would like
    for the attribute.
-   **openid.ax.update\_url**: a URL to send updates to (will be
    discussed later).

The use of URIs to identify attributes makes it trivial to define new
attributes without conflicting with other people (and as with XML
namespaces, the attribute aliases are arbitrary). However, the extension
is only useful if the OP and RP can agree on attribute types. To help
with this, there is a collection of [community defined attribute
types](http://www.axschema.org/types/) at
[axschema.org](http://www.axschema.org/).

As an example, imagine a web log that uses OpenID to authenticate
comment posts. Rather than just printing the OpenID URL for the
commenter, it could use attribute exchange to request their name, email,
website and hackergotchi. The authentication request might contain the
following additional fields:

    openid.ns.ax=http://openid.net/srv/ax/1.0
    openid.ax.mode=fetch_request
    openid.ax.required=name,hackergotchi
    openid.ax.if_available=email,web
    openid.ax.type.name=http://axschema.org/namePerson
    openid.ax.type.email=http://axschema.org/contact/email
    openid.ax.type.hackergotchi=http://axschema.org/media/image/default
    openid.ax.type.web=http://axschema.org/contact/web/default

In the successful authentication response, the following fields will be
included (assuming the OP supports the extension):

-   **openid.ax.mode**: must be \"fetch\_response\"
-   **openid.ax.type.*alias***: specify the type URI for each attribute
    being returned.
-   **openid.ax.count.*alias***: the number of values being returned for
    the given attribute alias (defaults to 1).
-   **openid.ax.value.*alias***: the value for the given attribute
    alias, if no corresponding openid.ax.count.*alias* field was sent.
-   **openid.ax.value.*alias*.*n***: the *n*th value for the given
    attribute alias, if a corresponding openid.ax.count.*alias* field
    was sent. The first attribute value is sent with n = 1.
-   **openid.ax.update\_url**: to be discussed later.

For the web log example given above, the response might look like:

    openid.ns.ax=http://openid.net/srv/ax/1.0
    openid.ax.mode=fetch_response
    openid.ax.type.name=http://axschema.org/namePerson
    openid.ax.type.email=http://axschema.org/contact/email
    openid.ax.type.hackergotchi=http://axschema.org/media/image/default
    openid.ax.value.name=John Doe
    openid.ax.value.email=john@example.com
    openid.ax.count.hackergotchi=0

In this response, we can see the following:

1.  The user has provided their name and email
2.  They have not provided any information about their web site. Either
    the OP does not support the attribute or the user has declined to
    provide it.
3.  The use has explicitly stated that they have no hackergotchi (i.e.
    it is a zero-valued attribute).

**Storing Attributes**

Using the Attribute Exchange fetch request, it is possible to outsource
management of pretty much all the user\'s profile information to the OP.
That said, the user will still need to update their profile data
occasionally. Telling them to go to their OP to change things and then
log in again is not particularly user friendly though.

Using the store request, the RP can let the user update their profile on
site and then transfer the changes back to the OP. Like the fetch
request, a store request is performed as part of an OpenID
authentication request. The additional request fields are pretty much
identical to a store response, except that **openid.ax.mode** is set to
\"store\_request\".

In the positive authentication response, the RP can see whether the data
was successfully stored by checking the **openid.ax.mode** response
field. If the data was stored, then it will be set to
\"store\_response\_success\". If the data was not stored it will be set
to \"store\_response\_failure\" and an error message may be found in
**openid.ax.error**.

**Asynchronous Attribute Updates**

One downside of the Simple Registration extension is that it only
transferred user details on login. This means that it is only possible
to get updates to attribute values by asking the user to log in again.
The Attribute Exchange extension provides a way to solve this problem in
the form of the **openid.ax.update\_url** request field.

When a \"fetch\_request\" is issued with the **openid.ax.update\_url**
field set, a compliant OP will record the following:

1.  the claimed ID and local ID from the authentication request
2.  the list of requested attributes
3.  the update\_url value (after verifying that it matches the
    **openid.realm** value of the authentication request).

The OP will then include **openid.ax.update\_url** in the authentication
response as an acknowledgement to the RP. When any of the given
attributes are updated the OP will send an *unsolicited positive
authentication response* to the given update URL. This will effectively
be the same as the original authentication response (i.e. for the same
claimed ID and local ID), but with new values for the changed
attributes.

As there is no mention of unsolicited authentication responses in the
main OpenID authentication specification, it is worth looking at what
checking the RP should do. This includes:

-   **Is this OP still authoritative for the claimed ID?** This is
    checked by performing discovery on the claimed ID and verifying that
    it results in the same server URL and local ID as given in the
    response.
-   **Did the message come from the OP?** As with a standard response,
    there should be a signature for the fields. Since the OP does not
    know what association to use for the signature, a new private
    association will be used. By issuing a \"check\_authentication\"
    request to the OP, the RP can verify that the message originated
    from the OP.

If these checks fail the RP should respond with a 404 HTTP error code,
which tells the OP to stop sending updates. If the message is valid, the
RP can update the user\'s profile data.

**Caveats**

While the Attribute Exchange extension provides significant features
above those provided by Simple Registration, but it still has its
limitations:

1.  Any attribute values provided to the RP are self-asserted.
2.  Related to the above, there is no way for a third party to make
    assertions about attribute values.

For (1), the solution is to perform the same level of verification on
the attribute value as if the user had entered it directly. So an OpenID
enabled mailing list manager should verify the email address provided by
attribute exchange before subscribing the user. In contrast, an OpenID
enabled shop probably doesn\'t need to do further verification of the
user\'s shipping address (since it is in the user\'s best interest to
provide correct information).

The exception to this rule is when there is some other trust
relationship between the OP and RP. For instance, if the RP knows that
the OP will only send an email address if it has first been validated,
then it may decide to trust the email address without performing its own
validation checks. This is most likely to be useful in closed systems
that happen to be using OpenID for single sign-on.

---
### Comments:
#### [Will Norris](http://will.norris.name) - <time datetime="2007-11-27 02:17:22">2 Nov, 2007</time>

Excellent explanation of AX, James. I\'m quite curious to see how RP
will try to use attribute storage down the road\... I imagine there will
need to be some best practices from the community as to what is and is
not appropriate to push back to the OP to store. I can easily imagine an
RP going crazy with it and basically treat the OP as its database. I
would also be careful about limiting the scope of AX, particularly your
first caveat \-- \"Any attribute values provided to the RP are
self-asserted.\" I\'ve been doing some work on bringing OpenID to
college campuses, and initially I imagine that \*none\* of the
attributes will be self-asserted unless the campus has alternate means
for modifying the data\... they will all come for the university\'s
enterprise data store. AX is just a format for carrying attributes on
the wire\... it says nothing about where the data came from. But I guess
your point is that if there isn\'t a pre-existing trust relationship,
the attributes may as well be self-asserted because you simply don\'t
know.

---
#### Johnny Bufu - <time datetime="2007-11-27 03:29:16">2 Nov, 2007</time>

James,

This is a great review of Attribute Exchange, thanks for taking the time
to write it up! A few comments:

Re: unsolicited positive assertion

They are mentioned in the spec in a couple of places:

10\. Responding to Authentication Requests\
\"Relying Parties SHOULD accept and verify assertions about Identifiers
for which they have not requested authentication. OPs SHOULD use private
associations for signing unsolicited positive assertions.\"\
http://openid.net/specs/openid-authentication-2\_0-12.html\#responding\_to\_authentication

11.2. Verifying Discovered Information\
\"If the Claimed Identifier was not previously discovered by the Relying
Party (the \"openid.identity\" in the request was
\"http://specs.openid.net/auth/2.0/identifier\_select\" or a different
Identifier, or if the OP is sending an unsolicited positive assertion),
the Relying Party MUST perform discovery on the Claimed Identifier in
the response to make sure that the OP is authorized to make assertions
about the Claimed Identifier.\"\
(this clarification was added after draft12, so it\'s only in SVN, not
yet published)

Re: verified attributes

Attribute Exchange deals only with the transport of the attributes, not
with their content, acquisition, source, trust. There\'s a separate
extension proposal that deals exactly with the trust issue for
attributes:

OpenID Signed Assertions\
http://www.mail-archive.com/specs\@openid.net/msg00907.html

A demonstrative implementation of this (using verification of emails as
the example) is available at:

https://verify.sxip.com/email/\
(retrieve a signed assertion saying that Sxip has verified your email
address)

https://verify.sxip.com/demorp/\
(present the signed assertion to an OpenID 2.0 RP using Attribute
Exchange, which trusts Sxip with the verification process)

Johnny

---
#### LionsPhil - <time datetime="2007-11-27 06:16:23">2 Nov, 2007</time>

I\'m not sure that 404 is the most applicable HTTP status code to use
here. 403 might be clearer.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-11-28 08:31:37">3 Nov, 2007</time>

Will: one thing to keep in mind is that some OPs may only have limited
support for attribute exchange: they may support a set of well known
attributes, but not arbitrary attributes. Furthermore, it is going to be
a while before RPs can depend on the presence of this extension (outside
of closed systems, that is).

Johnny: that looks pretty interesting. Including enough information in
the value to perform verification does partially solve the problem. It
pushes the need for a special RP ↔ OP trust relationship and changes it
to an RP ↔ attribute signer trust relationship. It still isn\'t clear
how to handle these trust relationships on the open internet.

LionsPhil: the specification mentions the 404 status code. If you think
403 is better, consider joining the OpenID specs mailing list and
suggesting the change.

---
