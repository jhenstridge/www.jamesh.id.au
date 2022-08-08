---
title: 'Annoying Firefox Bug'
slug: annoying-firefox-bug
date: 2006-04-03T13:38:26+08:00
tags: ['Gnome', 'Ubuntu']
---

Ran into an [annoying Firefox
bug](https://launchpad.net/distros/ubuntu/+source/firefox/+bug/37828)
after upgrading to [Ubuntu
Dapper](https://launchpad.net/distros/ubuntu/dapper). It seems to affect
rendering of ligatures.

At this point, I am not sure if it is an Ubuntu specific bug. The
current conditions I know of to trigger the bug are:

-   Firefox 1.5 (I am using the 1.5.dfsg+1.5.0.1-1ubuntu10 package).
-   Pango rendering enabled (the default for Ubuntu).
-   The web page must use a font that contains ligatures and use those
    ligatures. Since the \"DejaVu Sans\" includes ligatures and is the
    default \"sans serif\" font in Dapper, this is true for a lot of
    websites.
-   The text must be justified (e.g. use the \"`text-align: justify`\"
    CSS rule).

If you view a site where these conditions are met with an affected
Firefox build, you will see the bug: ligature glyphs will be used to
render character sequences like \"`ffi`\", but only the advance of the
first character\'s normal glyph is used before drawing the next glyph.
This results in overlapping glyphs:

{{< figure src="firefox-ligatures.png" >}}

It also results in a weird effect when selecting text, since the
ligatures get broken appart if the selection begins or ends in the
middle of the ligature, causing the text to jump around.

I wonder if this bug affects the Firefox packages in any other
distributions, or is an Ubuntu only problem?

---
### Comments:
#### max - <time datetime="2006-04-03 19:57:51">3 Apr, 2006</time>

Yes I have the same thing on Debian.

---
#### [niall](http://niall.evil.ie) - <time datetime="2006-04-03 20:02:28">3 Apr, 2006</time>

I\'ve seen it on OS-X as well

---
#### obi - <time datetime="2006-04-03 20:28:34">3 Apr, 2006</time>

Same thing on Debian with Epiphany here.

---
#### Henrik - <time datetime="2006-04-03 20:49:23">3 Apr, 2006</time>

I see this on FreeBSD too.

---
#### [Simos](http://simos.info/blog/) - <time datetime="2006-04-03 21:07:39">3 Apr, 2006</time>

Ubuntu Dapper (current updates) has DejaVu 2.3.\
There is a bug (probably) in Pango that causes these issues. DejaVu
2.4.1+ has a workaround to get to work.\
If you have the time, you can try to install 2.4.1 to try out. There is
a process to update DejaVu as found in Dapper to get this issue solved.\
See\
<https://launchpad.net/distros/ubuntu/>+source/ttf-dejavu/+bug/35470\
<https://launchpad.net/distros/ubuntu/>+source/ttf-dejavu/+bug/37565

---
#### James Henstridge - <time datetime="2006-04-03 21:29:01">3 Apr, 2006</time>

Simos: I don\'t think that bug is related.

I grabbed version 2.4.1 of DejaVu Sans and put it in my \~/.fonts
folder, restarted firefox and verified that it was using the new version
of the font by looking in /proc/\$pid/maps. The problem persisted.

If it was a bug in the font, I\'d expect it to be visible in other
applications and not just with justified text.

---
#### [Ralph Aichinger](http://www.pangea.at/%7eralph/fil-kerningbug.png) - <time datetime="2006-04-03 22:19:21">3 Apr, 2006</time>

Yes, same here in Debian unstable, see:\
<http://www.pangea.at/%7eralph/fil-kerningbug.png>

---
#### Gregor - <time datetime="2006-04-03 22:23:01">3 Apr, 2006</time>

I have the same problem, Dapper Flight 6. Sorry, am no developer so I
don\'t know what else information you need.

---
#### [Reinout van Schouwen](http://www.vanschouwen.info/) - <time datetime="2006-04-03 22:55:34">3 Apr, 2006</time>

Epiphany/Firefox and Yelp on Mandriva had a very similar problem that
was solved when Firefox was no longer built with pango enabled.

---
####  - <time datetime="2006-04-03 23:26:49">3 Apr, 2006</time>

I have the same problem (albiet much less frequently - I use a different
font altogether) on Gentoo, with Firefox compiled from source. I\'m
pretty sure it\'s not a packaging bug.

---
#### Mike Hearn - <time datetime="2006-04-04 00:50:52">4 Apr, 2006</time>

The Mozilla project makes generic Linux binaries available, you could
use them to compare against. I don\'t remember if they are built with
Pango by default or not.

---
#### James Henstridge - <time datetime="2006-04-04 01:44:20">4 Apr, 2006</time>

Mike: you can switch to the non-Pango code in the Ubuntu packages (and
any other builds with Pango enabled) by defining MOZ\_DISABLE\_PANGO=1
in the environment.

The bug does not occur with pango text rendering disabled, but it also
doesn\'t use the ligatures provided by the font.

However, disabling Pango isn\'t that interesting to me since it also
prevents firefox from rendering a number of other languages correctly.
As a user, I don\'t want to have to make a decision about which set of
languages I want to display correctly: I want them all to display
properly. With that aim in mind, the Pango backend seems like the one to
promote and improve.

---
#### [Hampus Wessman](http://hampus.vox.nu/) - <time datetime="2006-04-16 04:16:10">16 Apr, 2006</time>

I had some problems with this in Firefox 1.5 on Debian. All the Swedish
charactes (åäö) caused this bug and it was really annoying! Changing the
font from DejaVu to Bitstream solved all problems though. Don\'t know if
it is DejaVu\'s or Pango\'s fault, but it works well with Bitstream for
now\...\
The very same font works excellent in OpenOffice by the way, because I
just wrote a text spanning 26 pages, in Swedish, without any problems.
It looked good both on screen and when I printed it out.\
Your comments helped me alot - thanks!

---
#### [Leatherwood](http://www.shadowcouncil.org/leatherwood/) - <time datetime="2006-05-23 10:36:09">23 May, 2006</time>

I have the same problem in Debian Unstable, though I first noticed it
when using the FreeSerif, FreeSans, and FreeMono fonts. The most
annoying bug I noticed was that monospace text left out characters
entirely: the word \"strict\" looked like \"trict.\" For the moment,
I\'ve switched to fonts that don\'t use ligatures, but it sure is
annoying! And I miss my FreeX fonts.

---
