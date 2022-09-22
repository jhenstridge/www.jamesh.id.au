---
title: 'Sansa Fuze'
slug: sansa-fuze
date: 2009-03-24T19:21:05+09:00
tags: ['Gnome', 'Rhythmbox', 'Sansa']
---

On my way back from Canada a few weeks ago, I picked up a SanDisk [Sansa
Fuze](http://www.sansa.com/players/sansa_fuze) media player. Overall, I
like it. It supports Vorbis and FLAC audio out of the box, has a decent
amount of on board storage (8GB) and can be expanded with a MicroSDHC
card. It does use a proprietary dock connector for data transfer and
charging, but that\'s about all I don\'t like about it. The choice of
accessories for this connector is underwhelming, so a standard mini-USB
connector would have been preferable since I wouldn\'t need as many
cables.

The first thing I tried was to copy some music to the device using
[Rhythmbox](http://projects.gnome.org/rhythmbox/). This appeared to
work, but took longer than expected. When I tried to play the music, it
was listed as having an unknown artist and album name. Looking at the
player\'s filesystem, the reason for this was obvious: Rhythmbox had
transcoded the music to MP3 and lost the tags. Copying the ogg files
directly worked a lot better: it was quicker and preserved the metadata.

Of course, getting Rhythmbox to do the right thing would be preferable
to telling people not to use it. Rhythmbox depends on information about
the device provided by
[HAL](http://www.freedesktop.org/wiki/Software/hal), so I had a look at
the relevant FDI files. There was one section for Sansa Clip and Fuze
players which didn\'t list Vorbis support, and another section for
\"Sansa Clip version II\". The second section was a much better match
for the capabilities of my device. As all Clip and Fuze devices support
the extra formats when running the latest firmware, I merged the two
sections ([hal bug
20616](https://bugs.freedesktop.org/show_bug.cgi?id=20616), [ubuntu bug
345249](https://bugs.edge.launchpad.net/ubuntu/+source/hal-info/+bug/345249)).
With the updated FDI file in place, copying music with Rhythmbox worked
as expected.

The one downside to this change is that if you have a device with old
firmware, Rhythmbox will no longer transcode music to a format the
device can play. There doesn\'t seem to be any obvious way to tell if a
device has a new enough firmware via USB IDs or similar, so I\'m not
sure how to handle it automatically. That said, it is pretty easy to
upgrade the firmware [following the instructions from their
forum](http://forums.sandisk.com/sansa/board/message?board.id=sansafuse&thread.id=9473),
so it is probably best to just do that.

---
### Comments:
#### davide - <time datetime="2009-03-24 21:26:59">24 Mar, 2009</time>

Hi, I\'ve the same player and I think it\'s a good one. I use it with
Banshee without any problems, but I think I\'ll dig a little on bug
report to fix this stuff on (my) Debian too.

I would like to know if you have dug a little on the video issue\... It
seems impossible, as today, to transfer any video from a linux box to a
sansa fuze player. SMC (the official tool) uses a very particular
options set to encode a video before the transfert.
If I\'ll have time, I would like to try to track down this set and use
on a linux machine with ffmpeg, mencoder or something we have\...

---
#### [Fabian Rodriguez](https://wiki.ubuntu.com/MagicFab) - <time datetime="2009-03-24 21:46:55">24 Mar, 2009</time>

Hi James,

Have you tried this from the Rhythmbox FAQ:

http://live.gnome.org/Rhythmbox/FAQ

\"How do I set the music dir in an external device?

Create a .is\_audio\_player file on the device. You can set a few fields
in this file to override the HAL device information like this:

audio\_folders=MUSIC/,RECORDINGS/
folder\_depth=2
output\_formats=application/ogg,audio/x-ms-wma,audio/mpeg

but if the HAL information for your device is wrong, you should file a
bug, either with your distribution or in http://bugs.freedesktop.org/,
to get it fixed. \"

It seems this would associate paths to audio formats which may help your
issue.

---
#### oliver - <time datetime="2009-03-24 22:51:57">24 Mar, 2009</time>

Hm\... so if Rhythmbox reencodes music from ogg to mp3, it doesn\'t add
the original tagging information to the new mp3 files??

---
#### [Vadim P.](http://vadi.myopenid.com) - <time datetime="2009-03-24 22:56:10">24 Mar, 2009</time>

Feh\... and I was just eyeing that player.

Is there none that supports linux okay besides that c-something (I
forgot, but they explicitly mention linux support) company?

---
#### Ilmari Vacklin - <time datetime="2009-03-24 23:40:51">24 Mar, 2009</time>

Vadim: Cowon players generally work fine on Linux. (And, of course,
support Vorbis and Flac).

---
#### [vpv](http://vpv.kapsi.fi/blog/) - <time datetime="2009-03-25 00:03:36">25 Mar, 2009</time>

Thanks for getting the fix into hal, I have a Sansa Clip here :)

---
#### [Dave Morley](http://www.davmor2.co.uk) - <time datetime="2009-03-25 00:30:03">25 Mar, 2009</time>

Hi I\'m looking at getting one of these for xmas or birthday. Would you
say they are worth the money and is the sound quality good?

---
#### [Adam Williamson](http://www.happyassassin.net) - <time datetime="2009-03-25 02:26:18">25 Mar, 2009</time>

I\'ve seen several cases like this. Others to think about - what about
something like a PSP or a smartphone, a device that\'s sophisticated
enough to have different capabilities depending on what software\'s
installed on it?

It would be nice if HAL / DeviceKit were flexible enough to handle
this\...

---
#### Mats Taraldsvik - <time datetime="2009-03-25 03:21:45">25 Mar, 2009</time>

Hi!

Nice! I was wondering why some audio-files from Rhythmbox did not
work\...

I\'ve got the Sansa Clip, and I am very pleased with it! (It uses a
standard mini-usb connector.)

When Rhythmbox transcodes to vorbis, the file\'s suffix becomes .oga,
and the Clip only plays .ogg. I made a small Python script to fix the
renaming recursively, which I keep in the Clip\'s root directory.

\@Vadim P. : these are mass storage devices, so they are supported very
well (unless you meant officially supported - I have no idea ). :)

---
#### Michael "Sansa" Howell - <time datetime="2009-03-25 08:13:15">25 Mar, 2009</time>

\> Is there none that supports linux okay besides that c-something (I
forgot, but they explicitly mention linux support) company?

Be fair. Sandisk supporting OGG is unusual, and an improvement over
previous support (I own an e200, which does not support OGG).
Of course, if you can get an e200v1 (I own one), you can install RockBox
or SansaLinux, but that doesn\'t count\...

---
#### James Henstridge - <time datetime="2009-03-25 08:28:55">25 Mar, 2009</time>

Fabian: creating an .is\_audio\_player file would make Rhythmbox work
for me. Fixing the HAL FDI files fixes the problem for everyone. So
that\'s what I did.

oliver: the version in Ubuntu Intrepid doesn\'t seem to, at least :(

Vadim: the player works fine with Linux. If you\'re happy to transfer
files using Nautilus or the command line, then you won\'t have any
trouble. You\'ll need to update the FDI files if you want to be able to
transfer ogg files with apps like Rhythmbox though. They even provide
firmware updates in a form that can be installed from a Linux machine.

Dave: it sounds okay to me, but I\'m not the best judge of sound
quality. There was a bunch of sample tracks on my player, so you might
be able to try listening in store.

Mats: The .oga nonsense has been fixed in the latest gnome-media
release. You can fix it locally by clicking the \"edit\" button next to
the format selector in the preferences dialog. Pick the \"CD Quality,
Lossy\" profile, click \"edit\", then change the file extension and
save. You might need to restart Rhythmbox or Sound Juicer for the change
to stick.

---
#### [Vadim P.](http://vadi.myopenid.com) - <time datetime="2009-03-25 09:06:28">25 Mar, 2009</time>

\@Ilmari: Yes, cowon! Thanks for reminding me.

And no, I won\'t be spending my money on a product where I would be
reinstalling the core firmware (possibly voiding my warranty) or
receiving zero support (\"sorry, your platform isn\'t supported\") when
something does not work ;)

---
#### Mats Taraldsvik - <time datetime="2009-03-25 09:41:56">25 Mar, 2009</time>

\@James: Ok, thanks. I have seen .ogv also, though\...

\@James, Dave : The Clip and Fuze are known for their sound quality - it
beats most players (after what I\'ve heard - in both senses ;) ).

@Vadim\. : I don\'t get your negativity. You could look at it from
another point of view, though :

\- The sansa team actually support their devices after they have been
sold, adding new features and such.
- In the forums, they (that is both the sansa team and community)
provide solutions for Windows, Mac AND Linux.

( If you had bothered with researching etc, etc ;) )

Also, if you buy the player, noone is forcing you to update the
firmware. The player worked well in Linux with the firmware that was on
the player when I bought it, and still does, with the latest firmware. I
\_love\_ it: Cheap, good sound quality and interface, works well in
Linux. :)

---
#### James Henstridge - <time datetime="2009-03-25 09:59:31">25 Mar, 2009</time>

Vadim: the original firmware on my player supported Vorbis audio. The
short getting started guide just documents connecting the device and
dragging files to it via the file manager. If that isn\'t enough for
you, then good luck finding player.

Mats: the .ogv extension is correct for Theora videos. See
http://wiki.xiph.org/index.php/MIME\_Types\_and\_File\_Extensions for
details. That page also defines use of .oga for ogg encapsulated audio
other than the existing Vorbis and Speex formats. The recommendation to
continue using .ogg or .spx for these files is precisely to maintain
compatibility with devices like the Fuze.

For one GNOME release, the \"CD Quality, Lossy\" profile had been
changed to use the .oga extension. I called this nonsense because it was
still producing Vorbis I Profile data, which should still be using the
.ogg extension. That bug has since been corrected.

---
#### [Vadim P.](http://vadi.myopenid.com) - <time datetime="2009-03-25 10:19:35">25 Mar, 2009</time>

\@Mats: you still get support after you replaced the firmware?

Unofficial support is certainly nice - they are not guaranteed to
provide it or service as a first-priority. Nor would you might be
getting all the features you paid for since they\'re windows-only (had
this with a webcam - zero which support linux. went with one that worked
out of the box fine, but ofc the fancy editing programs that came with
it are windows-only and lost value to me).

Thanks for clearing up that it works, but there is another player which
holds higher values (and no, I am not a purist, I run the nvidia
proprietary drivers just fine. I am just logical in my purchasing
power.)

---
#### James Henstridge - <time datetime="2009-03-25 16:18:31">25 Mar, 2009</time>

Vadim: why on earth would you lose support after installing an official
firmware update by following the given installation steps? We aren\'t
talking about replacing official firmware with something like RockBox.
If you did run into a problem and contacted SanDisk for support, I
wouldn\'t be surprised if they asked you to check if a firmware update
helped.

There is some Windows only software for the device used to convert
videos to a form usable by the device. I guess that could be classed as
lost value, but I haven\'t felt a need to put videos on the device yet
(the screen is fairly small). If I did, I imagine that ffmpeg or mplayer
could be used to do the format conversion.

Out of interest, what is the other device you\'re considering? I\'m
happy with what I\'ve got, but I\'d be interested to know about other
viable alternatives.

---
#### davide - <time datetime="2009-03-25 20:27:43">25 Mar, 2009</time>

\@James Henstridge: for the moment there is no way to use ffmpeg to
transfer video to the fuze\... :-(
the problem is track down every detail about the encode parameters in
SMC \...

---
#### [Vadim P.](http://vadi.myopenid.com) - <time datetime="2009-03-25 20:51:16">25 Mar, 2009</time>

No, I am talking about replacing the official firmware with someone
else, which is what many people are implying to do to get better
functionality out of it. Of course upgrading the official firmware would
not affect the support (unless it\'s not possible to do on Linux? I have
never done it).

I\'m considering one of these: http://www.cowonglobal.com/ (click mp3 on
top\... it\'s a silly flash site). But I personally can\'t decide
whenever I should get a player with video or not, and if I get it with
video, I might as well get a Ubuntu MID when one of those is out :-/

(for now, I\'m just re-using an old phone that\'s not in service anymore
as a player. Oddly enough, when connected to Ubuntu, it recognizes it as
a source of broadband internet but not a music player, so I have to take
the internal card out. But I can\'t complain, I got it for free)

---
#### Mats Taraldsvik - <time datetime="2009-03-25 23:17:26">25 Mar, 2009</time>

\@Vladim: If you did read my earlier post, you\'d know:

\- that the .ogg and .flac support for the players is an official patch
- there are descriptions on how to update the firmware for Windows, Mac
and Linux

How would you get support from anyone with external firmware, nevermind
which os you\'re on? I don\'t see the argument against the sansa
players, here\...

I looked at the Cowon players also, though, but they are f\*cking
expensive compared to the Fuze/Clip\...

---
#### Mats Taraldsvik - <time datetime="2009-03-25 23:22:08">25 Mar, 2009</time>

Ok, I didn\'t say explicitly that the firmware is official. It is.

---
#### davide - <time datetime="2009-03-25 23:37:04">25 Mar, 2009</time>

Vladim, yes, you just need the cp and zip utility to update the
firmware\...
ah, and not so old version of the kernel (you need fat and usb support).

I think it\'s all.

My player has seen a windows system only few days ago, just for some
hours\... (to recharge the battery, what you can actually do on linux
too)

---
#### Jon Pritchard - <time datetime="2009-03-27 04:46:31">27 Mar, 2009</time>

They\'re a good little player for the money, in the UK you can get an
8GB version including also an 8GB microSDHC card for \~£50 (Play.com).

Thanks for updating the fdi policy file, as when I come around to using
it on Linux I\'m sure it\'ll be appreciated, although I mainly just copy
the files over by hand.

I too wish that they just used a mini/microUSB connector instead of the
proprietary one. It\'s good news that the Clip uses this.

People should support Sandisk for officially supporting OGG and FLAC. I
wouldn\'t have considered buying one of their players without hearing
that the firmware update to support this was imminent. I hope Rockbox
can work out how to do firmware on these \'v2\' models.

---
