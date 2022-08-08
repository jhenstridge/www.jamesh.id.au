---
title: 'PulseAudio'
slug: pulseaudio
date: 2009-02-25T21:24:58+09:00
tags: ['Gnome']
---

It seems to be a fashionable to blog about experiences with PulseAudio,
I thought I\'d join in.

I\'ve actually had some good experiences with PulseAudio, seeing some
tangible benefits over the ALSA setup I was using before.  I\'ve got a
cheapish surround sound speaker set connected to my desktop.  While it
gives pretty good sound when all the speakers are used together, it
sounds like crap if only the front left/right speakers are used.

ALSA supports multi-channel audio with the motherboard\'s sound card
alright, but apps producing stereo sound would only play out of the
front two speakers.  There are some howtos on the internet for setting
up a separate ALSA device that routes stereo audio to all the speakers
in the right way, but that requires that I know in advance what sort of
audio an application is going to generate: something like Totem could
produce mono, stereo or surround output depending on the file I want to
play.  This is more effort than I was usually willing to do, so I ended
up flicking a switch on the amplifier to duplicate the front left/right
channels to the rear.

With PulseAudio, I just had to edit the /etc/pulse/daemon.conf file and
set default-sample-channels to 6, and it took care of converting mono
and stereo output from apps to play on all the speakers while still
letting apps producing surround output play as expected.  This means I
automatically get the best result without any special effort on my part.

I\'m not too worried that I had to tell PulseAudio how many speakers I
had, since it is possible to plug in a number of speaker configurations
and I don\'t think the card is capable of sensing what has been attached
(the manual documents manually selecting the speaker configuration in
the Windows driver).  It might be nice if there was a way to configure
this through the GUI though.

I\'m looking forward to trying the \"[flat
volume](http://0pointer.de/blog/projects/oh-nine-fifteen.html)\" feature
in future versions of PulseAudio, as it should get the best quality out
of the sound hardware (if I understand things right, 50% volume with
current PulseAudio releases means you only get 15 bits of quantisation
on a 16-bit sound card).  I just hope that it manages to cope with the
mixers my sound card exports: one two-channel mixer for the front
speakers, one two-channel mixer for the rear two speakers and two single
channel mixers for the center and LFE channels.

---
### Comments:
#### Jackflap - <time datetime="2009-02-25 23:42:58">25 Feb, 2009</time>

Well, I\'ve come across a couple of bugs where sound intermittently
disappears when using PA, but setting to ALSA fixed those.

Other than that, I\'m all for PA with the promise of being able to
stream my audio to a pair of bluetooth speakers while simultaneously
playing the audio out of a pair of wired speakers. Multi-room sound
system here we come!

Haven\'t tested yet tho, so it may be a pipe-dream :)

---
#### Rob J. Caskey - <time datetime="2009-02-25 23:47:40">25 Feb, 2009</time>

I too use PA and am happy with it but I would like to note that \"edit
the /etc/pulse/daemon.conf file and set default-sample-channels to 6\"
is considered special effort and not automatic by 99.99% of people on
the earth, all of which would not be able to do it.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-02-26 00:16:55">26 Feb, 2009</time>

Rob: right. I think a GUI would help a lot here.

That said, I don\'t think it is possible to automatically configure this
with my sound card: it is possible to connect between 2 and 8 speakers,
and there doesn\'t seem to be any way to detect what the user has
connected. If it was possible to automatically configure, the Windows
drivers wouldn\'t ask you how many speakers you had.

---
#### Achim Frase - <time datetime="2009-02-26 00:40:56">26 Feb, 2009</time>

I just would like to note, that you will be able to reconfigure your
speaker setup without edition daemon.conf.\
That will happen in the near future with PA 0.9.15.

Sure there is no GUI for it today but maybe \"tomorrow\" ;-)

PA will also automatically probe which combinations for playback and
capture are working with your sound card and allow on-the-fly
reconfiguration.

For more information on that topic you should take a look at Lennart\'s
blog.

On-the-fly Reconfiguration of Devices (aka \"S/PDIF Support\")\
http://0pointer.de/blog/projects/oh-nine-fifteen.html

---
#### Zink - <time datetime="2009-02-26 02:24:28">26 Feb, 2009</time>

Funnily enough I had the opposite experience. I have a similar feature
exposed by alsa (the surround sound feature from the hda audio driver).
It is done automatically on the hardware (just like what you\'re doing
in software here except there\'s no CPu overhead) and exposed by
alsamixer. In my case I couldn\'t have this feature back when using
pulseaudio even when changing the channels, only the two main speakers
would play.

---
