---
title: 'Client Side OpenID'
slug: client-side-openid
date: 2008-02-18T14:13:13+09:00
draft: false
tags: ['OpenID']
---

The following article discusses ideas that I wouldn\'t even class as
vapourware, as I am not proposing to implement them myself. That said,
the ideas should still be implementable if anyone is interested.

One well known security weakness in [OpenID](http://openid.net/) is its
weakness to phishing attacks. An OpenID authentication request is
initiated by the user entering their identifier into the Relying Party,
which then hands control to the user\'s OpenID Provider through an HTTP
redirect or form post. A malicious RP may instead forward the user to a
site that looks like the user\'s OP and record any information they
enter. As the user provided their identifier, the RP knows exactly what
site to forge.

**Out Of Band Authorisation**

One way around this is for the OP to authenticate the user and get
authorisation out of band --- just because the authentication message
begins and ends with HTTP requests does not mean that the actual
authentication/authorisation need be done through the web browser.

Possibilities include performing the authorisation via a Jabber message
or SMS, or some special purpose protocol. Once authorisation is granted,
the OP would need to send the OpenID response. Two ways for the web
browser to detect this would be polling via AJAX, or using a server-push
technique like
[Comet](http://en.wikipedia.org/wiki/Comet_%28programming%29).

**Using a Browser Extension**

While the above method adds security it takes the user outside of their
web browser, which could be disconcerting. We should be able to provide
an improved user experience by using a web browser extension. So what is
the best way for the extension to know when to do its thing?

One answer is **whenever the user visits the server URL of their OP**.
Reading through the specification there are no other times when the user
is required to visit that URL. So if the web browser extension can
intercept GET and POST requests to a particular URL, it should be able
to reliably detect when an authentication request is being initiated.

At this point, the extension can take over up to the point where it
redirects the user back to the RP. It will need to communicate with the
OP in some way to get the response signed, but we have the option of
using some previously established back channel.

**Moving the OP Client Side**

Using the browser extension from the previous section as a starting
point, we\'ve moved some of the processing to the client side. We might
now ask how much work can be moved to the client, and how much work
needs to remain on the server?

From the specification, there are three points at which the RP needs to
make a direct connection to the OP (or a related server):

1.  When performing discover, the RP needs to be able to read an HTML or
    XRDS file off some server.
2.  The `associate` request, used to generate an association that lets
    the RP verify authentication responses.
3.  The `check_authentication` request, used to verify a response in the
    case where an association was not provided in the request (or the OP
    said the association was invalid).

In all other cases, communication is mediated through the user\'s
browser (so are being intercepted by the browser extension).
Furthermore, these three cases should only occur after the user
initiates an OpenID authentication request. This means that the browser
extension should be active and talking to the server.

So one option would be to radically simplify the server side so that it
simply proxies the `associate` and `check_authentication` requests to
the browser extension via a secure channel. This way pretty much the
entire OP implementation resides in the browser extension with no state
being handled by the server.

**Conclusion**

So it certainly looks like it is possible to migrate almost everything
to the client side. That still leaves open the question of whether
you\'d actually want to do this, since it effectively makes your
identity unavailable when away from a computer with the extension
installed (a similar problem to use of self asserted infocards with
Microsoft\'s CardSpace).

Perhaps the intermediate form that still performs most of the OP
processing on the server is more useful, providing a level of phishing
resistance that would be difficult to fake (not only does it prevent
rogue RPs from capturing credentials, the \"proxied OP\" attack will
fail to activate the extension all together).

---
### Comments:
#### Andrew - <time datetime="2008-02-18 14:02:12">1 Feb, 2008</time>

I think you mean \"rogue\" RPs, not \"rouge\" :)

---
#### [Raithmir](http://kulthea.net/id/) - <time datetime="2008-02-18 18:31:23">1 Feb, 2008</time>

Interesting article, it\'s certainly something that should be looked
into IMO.

The main thing that worries me about OpenID is that once someone finds
out your password then there\'s potentially a lot of sites a hacker has
access to, posing as you. More needs to be done, and your suggestions go
some way to alleviating that.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-02-18 19:13:54">1 Feb, 2008</time>

Andrew: fixed.

Raithmir: It is true that revealing your OpenID identity\'s login
credentials gives someone access to many sites, but it is not
particularly worse than the current status quo. Most sites use an email
address to identify the user, and provide a way to send a \"password
reset\" mail to that address. So if you reveal your mail server login
credentials to someone, then they\'ve effectively got control of your
account on all the sites you used that email address with.

---
#### alex - <time datetime="2008-02-18 21:35:54">1 Feb, 2008</time>

How about when you register to OpenID you upload a small picture. Then,
the login page shows you this picture- say, your face.

It\'s a very visual way of avoiding phishing.

Disclaimer: I only have some knowledge about how OpenID works.

---
#### Christopher - <time datetime="2008-02-18 21:40:58">1 Feb, 2008</time>

What I found interesting was the approach that MyOpenID uses, where I
believe you can install an SSL certificate direct into your browser from
their site. So any time you were forwarded to (what you thought was)
MyOpenID and it prompted you for your password (as opposed to doing the
SSL magic), you\'d know you\'re on rogue site.

---
#### Rob J. Caskey - <time datetime="2008-02-18 21:49:57">1 Feb, 2008</time>

Christopher:

I\'m going to me-to the anon fellow above me. Certs are the way of the
future, and they should live on the Gnome keychain and be presented in a
Cardspace like selector. RPs can select with set of authentication
mechanisms they wish to support: my personal preference is that Infocard
be the dominate one because Cardspace on windows solves the same problem
fairly well, and there are no show-stopper problems with it. The
MS-blessed term for generic implementations of Cardspace is Infocard.

There is already a Firefox plugin that sorta-worked last time I checked
on it about 9 months ago, it lives at
http://code.google.com/p/openinfocard/downloads/list, but I would love
to see it in Gnome proper. SSL certs wouldn\'t be bad either, but
gnome-integration is a must.

---
#### [Matthew](http://www.braintube.com) - <time datetime="2008-02-18 22:40:53">1 Feb, 2008</time>

Folks are already using XMPP to do it:\
http://openid.xmpp.za.net/\
http://sameplace.cc/wiki/openid-integration\
for example.

---
#### [Owen Taylor](http://fishsoup.net) - <time datetime="2008-02-19 02:02:02">2 Feb, 2008</time>

To me, reducing the threat of phishing boils down to to one or both of
two things: change around the interaction so that the user never expects
to have to enter a password on the web, or to eliminate entirely the
existence of a password that is useful to phish. Current methods of
improving OpenID (require logging in beforehand, make your OP\'s page
more verifiably authentic etc), all fall down, because they assume the
existence of an alert user who understands what is going on and has a
good sense of when something unusual happens.

Information Cards have some nice properties\... in particular they have
a well thought-out user interaction model that does not involve entering
passwords into a web page. The biggest problem is probably is that
implementing them brings in all sorts of WS-\* goo. A client side OP
sounds a bit like reinventing information cards. But I think at that
point you have to ask what the goals are: to integrate into the OpenID
ecosystem? to make things easier to implement by not having WS-\*? etc.
The worst thing would be to end up with the broken OpenID user
interaction, but incompatible with both most OpenID RP\'s and with
information card RP\'s.

---
#### steve - <time datetime="2008-02-19 02:47:02">2 Feb, 2008</time>

I was going to suggest the exact same as Alex above. Require the user to
upload some picture(or text for accessibility) that they\'ll recognise
and expect when they go to their genuine site.

---
#### [John Drinkwater](http://ezri.nextraweb.com/) - <time datetime="2008-02-19 02:47:23">2 Feb, 2008</time>

James, You can achieve this using http://openid.xmpp.za.net/ (this does
over-XMPP openid auth like you said), and sameplace.cc, an XMPP firefox
extension. You receive a message when you go to log-in, and all you have
to do is reply, and then the stall while waiting for
http://openid.xmpp.za.net/ to load, unblocks and you log in to the RP.
Pretty simple.

Personally I'm not going to touch all the \*Card\* stuff, seems a little
ott and.. controlling, I'm quite happy using regular browser certs, the
only thing needing improvement is the usability and awareness for newbs.

---
#### Frej Soya - <time datetime="2008-02-19 06:19:37">2 Feb, 2008</time>

I\'ve been thinking/trying to get openid in mugshot/online.gnome.org
(only broken patch so far on local disk). Mugshot would improve if it
could auto-detect other web\"applications\" at sign-up time - so it
seems like a good place for an openid-provider.

But the out-of-band extra security dawned on me - there already is a
xmpp connection from mugshot client to server - but I wasn\'t sure if it
actually increased security, and I didn\'t stop to think about it.

Motivating that other people believes it does :)

---
#### [Dirk Gently](http://linuxtidbits.wordpress.com/) - <time datetime="2008-02-19 07:55:08">2 Feb, 2008</time>

Nice to hear someone is thinking about this. I\'ve heard of this kick
and just can\'t seem to understand why it\'s catching on. The browser
stores every password I possibly need and though OpenID would be super
nice to joining a new site (heck it could even get rid of the signin
form in alot of instances), I\'m not about to trade security for it.

FF3b4!??? hmmm.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-02-19 19:07:55">2 Feb, 2008</time>

alex, steve: the image/text customisation method is already in use at
sites like myopenid. Note however that the image needs to be associated
with the computer (e.g. via a cookie with a large expiry time) rather
than to anything the user types in. If the OP displayed these sorts of
customisations during an authentication request at a new computer, then
a rogue RP could do the same by proxying the page.

Matthew, John: I am not too surprised to see that someone has done the
out-of-band XMPP authentication solution (which is pretty cool!). I
haven\'t seen anything along the lines of the browser extension I
outline, which I think could provide an interesting user experience.

---
#### [James](http://trs80.ucc.asn.au/) - <time datetime="2008-02-19 20:18:13">2 Feb, 2008</time>

The [Simile Appalachian OpenID
extension](http://simile.mit.edu/wiki/Appalachian) has some amount of
[phishing
protection](http://simile.mit.edu/wiki/Appalachian_Anti-Phishing) in it,
I haven\'t investigated how much though.

---
#### [Kevin Turner](http://kevin.janrain.com/) - <time datetime="2008-02-20 02:34:15">3 Feb, 2008</time>

[Seatbelt](https://pip.verisignlabs.com/seatbelt.do), Sxipper, and
Information Cards are browser extensions that can all integrate with
some existing OPs today.

The infocard WS-\* goo isn\'t so bad as you might think. There\'s a
BSD-licensed python implementation for self-issued infocards that you
can refer to at http://code.google.com/p/py-self-issued-rp/

---
