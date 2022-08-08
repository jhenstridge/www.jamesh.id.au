---
title: 'Avahi on Breezy followup'
slug: avahi-on-breezy-followup
date: 2005-11-03T01:23:31+08:00
tags: ['Avahi', 'Ubuntu']
---

So after I posted some instructions for setting up Avahi on Breezy, a
fair number of people at [UBZ](http://wiki.ubuntu.com/UbuntuBelowZero)
did so. For most people this worked fine, but it seems that a few
people\'s systems started spewing a lot of network traffic.

It turns out that the problem was actually caused by the
[`zeroconf`](http://packages.ubuntu.com/breezy/net/zeroconf) package
(which I did not suggest installing) rather than Avahi. The `zeroconf`
package is not needed for service discovery or `.local` name lookup, so
if you are at UBZ you should remove the package or suffer the wrath of
Elmo.

---
### Comments:
#### torkel - <time datetime="2005-11-03 10:01:00">3 Nov, 2005</time>

What kind of traffic?

Was it spewing a \*lot\* of ARP-requests by any chance? In that case I
have been hit by it too ;-)

/torkel

---
#### [Phil](http://technomancy.us) - <time datetime="2005-11-03 10:17:51">3 Nov, 2005</time>

I heard Gaim is avahi-enabled. Is that what you\'re talking about using?
Are there Ubuntu packages for this yet?

---
#### [Chris Cunningham](http://thumper.kicks-ass.org) - <time datetime="2005-11-03 10:57:09">3 Nov, 2005</time>

I heard Gaim is avahi-enabled

HEAD is, no released build is. Certainly not the current Ubuntu package.

\- Chris\

---
#### James Henstridge - <time datetime="2005-11-03 12:56:52">3 Nov, 2005</time>

torkel: yes, I think that is what was happenning. It looks like there is
an updated version of the zeroconf package that fixes this, but it
isn\'t in Breezy.

---
#### [Trent Lloyd](http://www.freedesktop.org/Software/Avahi) - <time datetime="2005-11-03 13:34:28">3 Nov, 2005</time>

Last check, gaim was not avahi enabled, but it does support the
network-iChat stuff apple uses using Howl, and avahi svn (yet to be
released as 0.6) features an API/ABI compatible layer for Howl (and
bonjour) so you could use it with this.

---
#### [Anand Kumria](http://www.progsoc.org/~wildfire/aum/) - <time datetime="2005-11-03 14:08:40">3 Nov, 2005</time>

This was found and fixed some time ago in zeroconf 0.3 (fixed on the
12th July \-- almost 4 months ago).

Updated packages are already in Debian testing (i.e. Ubuntu Dapper) and
everyone ought to be able to grab it and try it out.

---
#### [Davyd](http://www.davyd.id.au) - <time datetime="2005-11-03 14:51:07">3 Nov, 2005</time>

What does zeroconf do that NetworkManager doesn\'t do?

Also, Gaim now supports the iChat protocol? That is pretty rad, when I
tried it out some time ago [it didn\'t
work](http://www.livejournal.com/users/davyd/2004/06/13/).

---
#### anti - <time datetime="2005-11-03 17:33:17">3 Nov, 2005</time>

Well, you indirectly did recommend to install zeroconf: The package is
recommended by libnss-mdns which in turn was recommended by your post
:-)

So, if the package installer of choice is configured to install
recommended packages (default for e.g. aptitude) - that\'s why it was
installed.

---
#### James Henstridge - <time datetime="2005-11-04 02:31:53">4 Nov, 2005</time>

Hi Anand,

It looks like the release with the fix came out a little after the
upstream version freeze for Breezy:

<https://wiki.ubuntu.com/BreezyReleaseSchedule>

Since this problem annoys network admins enough though, so the fix might
be released for Breezy as an update or backport.

---
#### torkel - <time datetime="2005-11-04 06:03:15">4 Nov, 2005</time>

And it can also more or less bring down some routers\... :-(

---
