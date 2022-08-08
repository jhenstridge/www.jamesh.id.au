---
title: 'Seeking in Transcoded Streams with Rygel'
slug: dlna-time-seek
date: 2009-07-24T16:46:18+08:00
tags: ['DLNA', 'Gnome', 'PlayStation 3', 'UPnP']
---

When looking at various UPnP media servers, one of the features I wanted
was the ability to play back my music collection through my PlayStation
3.  The complicating factor is that most of my collection is encoded in
Vorbis format, which is not yet supported by the PS3 (at this point, it
doesn\'t seem likely that it ever will).

Both [MediaTomb](http://mediatomb.cc/) and
[Rygel](http://live.gnome.org/Rygel) could handle this to an extent,
transcoding the audio to raw LPCM data to send over the network.  This
doesn\'t require much CPU power on the server side, and only requires
1.4 Mbit/s of bandwidth, which is manageable on most home networks. 
Unfortunately the only playback controls enabled in this mode are play
and stop: if you want to pause, fast forward or rewind then you\'re out
of luck.

Given that Rygel has a fairly simple code base, I thought I\'d have a go
at fixing this.  The first solution I tried was the one I\'ve mentioned
a few times before: with uncompressed PCM data file offsets can be
easily converted to sample numbers, so if the source format allows time
based seeking, we can easily satisfy byte range requests.

I got a basic implementation of this working, but it was a little bit
jumpy and not as stable as I\'d like.  Before fully debugging it, I
started looking at the mysterious [DLNA](http://www.dlna.org/) options
I\'d copied over to get things working.  One of those was the \"DLNA
operation\", which was set to \"range\" mode.  Looking at the
[GUPnP](http://www.gupnp.org/) header files, I noticed there was another
value named \"timeseek\".  When I picked this option, the HTTP requests
from the PS3 changed:

    GET /... HTTP/1.1
    Host: ...
    User-Agent: PLAYSTATION 3
    Connection: Keep-Alive
    Accept-Encoding: identity
    TimeSeekRange.dlna.org: npt=0.00-
    transferMode.dlna.org: Streaming

The pause, rewind and fast forward controls were now active, although
only the pause control actually worked properly. After fast forwarding
or rewinding, the PS3 would issue another HTTP request with the
`TimeSeekRange.dlna.org` header specifying the new offset, but the
playback position would reset to the start of the track when the
operation completed. After a little more experimentation, I found that
the playback position didn\'t reset if I included
`TimeSeekRange.dlna.org` in the response headers. Of course, I was still
sending back the beginning of the track at this point but the PS3 acted
as though it was playing from the new point in the song.

It wasn\'t much more work to update the GStreamer calls to seek to the
requested offset before playback and things worked pretty much as well
as for non-transcoded files.  And since this solution didn\'t involve
byte offsets, it also worked for Rygel\'s other transcoders.  It even
worked to an extent with video files, but the delay before playback was
a bit too high to make it usable \-- fixing that would probably require
caching the GStreamer pipeline between HTTP requests.

**Thoughts on DLNA**

While it can be fun to reverse engineer things like this, it was a bit
annoying to only be able to find out about the feature by reading header
files written by people with access to the specification.  I can
understand having interoperability and certification requirements to use
the DLNA logo, but that does not require that the specifications be
private.

As well as keeping the specification private, it feels like some aspects
have been intentionally obfuscated, using bit fields represented in both
binary and hexadecimal string representations inside the resource\'s
protocol info.  This might seem reasonable if it was designed for easy
parsing, but you need to go through two levels of XML processing (the
SOAP envelope and then the DIDL payload) to get to these flags. 
Furthermore, the attributes inherited from the [UPnP MediaServer
specifications](http://www.upnp.org/specs/av/) are all human readable so
it doesn\'t seem like an arbitrary choice.

On the bright side, I suppose we\'re lucky they didn\'t use
cryptographic signatures to lock things down like Apple has with some of
their protocols and file formats.

---
### Comments:
#### Dom - <time datetime="2009-07-24 18:13:17">24 Jul, 2009</time>

Hey sounds great. Do you have a branch or an ETA when we might see the
fixes in git://git.gnome.org/rygel ? :)

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-07-24 19:14:28">24 Jul, 2009</time>

\@Dom: should be merged soon (Zeeshan is reviewing/merging it).

---
#### Zeeshan Ali - <time datetime="2009-07-24 20:18:22">24 Jul, 2009</time>

Already merged!

---
#### [maxauthority](http://vimperator.org) - <time datetime="2009-07-28 21:25:31">28 Jul, 2009</time>

Did you try the \"PS3 media server\" -
http://ps3mediaserver.blogspot.com/? It\'s a java dlna server, but at
least in the 1.20betas it\'s just so pleasant to use, and even
auto-transcodes most formats which the PS3 does not understand.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-08-04 18:43:48">4 Aug, 2009</time>

\@maxauthority: I hadn\'t seen that package before I started hacking on
this feature in Rygel. Given Rygel\'s integration with GNOME and
FreeDesktop.org technologies, it seems like a better code base to work
on.

---
