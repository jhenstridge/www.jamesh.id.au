---
title: 'Ubuntu packages for Rygel'
slug: ubuntu-packages-for-rygel
date: 2009-06-17T12:17:58+08:00
tags: ['Gnome', 'Launchpad', 'PlayStation 3', 'Ubuntu', 'UPnP']
---

I promised [Zeeshan](http://zee-nix.blogspot.com/) that I\'d have a look
at his [Rygel UPnP Media Server](http://live.gnome.org/Rygel) a few
months back, and finally got around to doing so.  For anyone else who
wants to give it a shot, I\'ve put together some Ubuntu packages for
Jaunty and Karmic in a [PPA](https://help.launchpad.net/Packaging/PPA)
here:

-   <https://launchpad.net/~jamesh/+archive/upnp>

Most of the packages there are just rebuilds or version updates of
existing packages, but the Rygel ones were done from scratch.  It is the
first Debian package I\'ve put together from scratch and it wasn\'t as
difficult as I thought it might be.  The tips from the \"Teach me
packaging\" workshop at the Canonical All Hands meeting last month were
quite helpful.

After installing the package, you can configure it by running the
\"rygel-preferences\" program.  The first notebook page lets you
configure the transcoding support, and the second page lets you
configure the various media source plugins.

I wasn\'t able to get the [Tracker](http://projects.gnome.org/tracker/)
plugin working on my system, which I think is due to Rygel expecting the
older Tracker D-Bus API.  I was able to get the folder plugin working
pretty easily though.

Once things were configured, I ran Rygel itself and an extra icon showed
up on my PlayStation 3.  Getting folder listings was quite slow, but
apparently this is limited to the folder back end and is currently being
worked on.  It\'s a shame I wasn\'t able to test the more mature Tracker
back end.

With
[LPCM](http://en.wikipedia.org/wiki/Linear_pulse_code_modulation "Linear pulse code modulation")
transcoding enabled, I was able to successfully play a
[Vorbis](http://xiph.org/vorbis/) file on the PS3.  With transcoding
disabled, I wasn\'t able to play any music \-- even files in formats the
PS3 could handle natively.  This was apparently due to the folder
backend not providing the necessary metadata.  I didn\'t have any luck
with MPEG2 transcoding for video.

It looks like Rygel has promise, but is not yet at a stage where it
could replace something like MediaTomb.  The [external D-Bus media
source](http://live.gnome.org/Rygel/MediaServerSpec) support looks
particularly interesting.  I look forward to trying out version 0.4 when
it is released.

---
### Comments:
#### foo - <time datetime="2009-06-17 14:13:55">3 Jun, 2009</time>

Could we get this in Debian too?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-06-17 14:39:13">3 Jun, 2009</time>

It isn\'t even in Ubuntu yet. These are just personal packages. It
shouldn\'t be much trouble rebuilding them on Debian though.

It\'d probably be difficult to get it into either Debian or Ubuntu
proper until 0.4 is released anyhow: there are a few copyright messages
claiming \"all rights reserved\" which conflicts with them also claiming
to be LGPL\'d. I reported that problem and it should be cleared up for
the next release.

---
#### Marc-Andre Lureau - <time datetime="2009-06-18 03:07:36">4 Jun, 2009</time>

James, I started a packaging for Debian,
http://git.debian.org/?p=collab-maint/rygel.git;a=summary. Tell me if
your\'s is more advanced or how we can join the effort. I am guilty, I
didn\'t send an ITP. No worries.

---
#### [More Rygel testing - James Henstridge](more-rygel-testing.md) - <time datetime="2009-06-19 00:06:45">5 Jun, 2009</time>

\[\...\] James Henstridge Random stuff Skip to content « Ubuntu packages
for Rygel \[\...\]

---
#### stoffe - <time datetime="2009-09-27 18:27:48">0 Sep, 2009</time>

Is it possible to get an update to 4.1? Please?

---
