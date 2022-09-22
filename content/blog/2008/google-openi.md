---
title: 'Re: Continuing to Not Quite Get It at Google...'
slug: google-openi
date: 2008-10-30T17:30:02+09:00
tags: ['OpenID']
---

[David](http://opensourcetogo.blogspot.com/2008/10/continuing-to-not-quite-get-it-at.html):
taking a quick look at [Google\'s
documentation](http://code.google.com/apis/accounts/docs/OpenID.html),
it sure looks like OpenID to me. The main items of note are:

1.  It documents the use of OpenID 2.0\'s directed identity mode. Yes
    this is \"a departure from the process outlined in OpenID 1.0\", but
    that could be considered true of all new features found in 2.0.
    Google certainly isn\'t the first to implement this feature:

    -   [Yahoo\'s OpenID page](http://openid.yahoo.com/) recommends
        users enter \"yahoo.com\" in the identity box on web sites,
        which will initiate a directed identity authentication request.
    -   We\'ve been using directed identity with
        [Launchpad](https://launchpad.net/) to implement single sign on
        for various Canonical/Ubuntu sites.

    Given that Google account holders identify themselves by email
    address, users aren\'t likely to know a URL to enter, so this kind
    of makes sense.

2.  The identity URLs returned by the OpenID provider do not directly
    reveal information about the user, containing a long random string
    to differentiate between users. If the relying party wants any user
    details, they must request them via the standard OpenID Attribute
    Exchange protocol.

3.  They are performing access control based on the OpenID realm of the
    relying party. I can understand doing this in the short term, as it
    gives them a way to handle a migration should they make an
    incompatible change during the beta. If they continue to restrict
    access after the beta, you might have a valid concern.

It looks like there would be no problem talking to their provider using
existing off the shelf OpenID libraries (like the ones from JanRain).

If you have an existing site using OpenID for login, chances are that
after registering the realm with Google you\'d be able to log in by
entering Google\'s OP server URL. At that point, it\'d be fairly
trivial to add another button to the login page -- sites seem pretty
happy to plaster provider-specific radio buttons and entry boxes all
over the page already \...

---
### Comments:
#### [Lefty](http://opensourcetogo.blogspot.com/) - <time datetime="2008-10-30 16:48:07">30 Oct, 2008</time>

Yeah, looks like it\'s (mostly) ((but not quite, yet)) OpenID, so it
seems I might have jumped the gun a little.

If I did, it\'s mainly because Google does indeed have this habit of not
really engaging with the community at large all that well. I got very
tired over the past year of listening to folks like Eric Chu spout FUD
like \"existing open source projects don\'t ship on schedule\" (in spite
of the fact that GNOME ships every six months, like clockwork), that
\"existing open source projects are too desktop-oriented\" (which is
simply arrant nonsense), and the like, as justifications for reinventing
wheels all over the place\--rather than actually working with the
community\--with Android\...

---
#### [Lefty](http://opensourcetogo.blogspot.com/) - <time datetime="2008-10-30 17:02:17">30 Oct, 2008</time>

Oh, and for what it\'s worth, I\'d say the necessity to \"plaster
another provider-specific radio buttons and entry boxes onto the login
page\" pretty much defeats the purpose of OpenID, but maybe that\'s just
me\...

---
#### James Henstridge - <time datetime="2008-10-30 17:18:25">30 Oct, 2008</time>

As I said, the protocol examples they give look like correct OpenID
messages (no \"mostly\" about it).

Once the OpenID realm white listing is out of the way (either by
registering a realm or when Google removes the white list), you\'d be
able to log in using \"https://www.google.com/accounts/o8/id\" as an
identity URL -- no special buttons required. If they wanted it\'d be
pretty easy to make \"google.com\" provide the same discovery
information, similar to what Yahoo has done. Of course, this isn\'t a
big deal while the white list is in place since such sites will probably
be set up with a button.

---
#### [Will Norris](http://will.norris.name/) - <time datetime="2008-10-31 03:03:56">31 Oct, 2008</time>

While there is a XRDS document [published on
google.com](http://www.google.com/xrds/xrds.xml), my understanding after
the OpenID UX Summit last week is that the consumer side would actually
be gmail.com (google.com is for google employees). But yes, it does
sound like that is the plan.

---
