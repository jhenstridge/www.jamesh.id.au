---
title: 'Inkscape Migrated to Launchpad'
slug: inkscape-migrated-to-launchpad
date: 2007-11-28T14:13:32+09:00
tags: ['Gnome', 'Inkscape', 'Launchpad']
---

Yesterday I performed the migration of
[Inkscape](http://www.inkscape.org/)\'s bugs from
[SourceForge.net](http://sourceforge.net/) to
[Launchpad](https://launchpad.net/). This was a full import of all their
historic bug data -- about 6900 bugs.

As the import only had access to the SF user names for bug reporters,
commenters and assignees, it was not possible to link them up to
existing Launchpad users in most cases. This means that duplicate person
objects have been created with email addresses like
`$USERNAME@users.sourceforge.net`.

If you are a Launchpad user and have previously filed or commented on
Inkscape bugs, you can clean up the duplicate person object by going to
the following URL and entering your `$USERNAME@users.sourceforge.net`
address:

> <https://launchpad.net/people/+requestmerge>

After following the instructions in the email confirmation, all
references to the duplicate person will be fixed up to point at your
primary account (so bug mail will go to your preferred email address
rather than being redirected through SourceForge).

---
### Comments:
#### Peteris Krisjanis - <time datetime="2007-11-28 14:13:56">28 Nov, 2007</time>

Man, this is great that Inkscape will finally use Launchpad bug system.
I used Inkscape in few serious projects this year and wanted to report
bunch of bugs I encountered, but SF bug system, with all respect to
SF\'s long support of open source, is very hard to use. Launchpad, in
other way, are easiest system for this, at least for me.

Keepin rocking!

---
#### Wade Mealing - <time datetime="2007-11-28 17:26:18">28 Nov, 2007</time>

Man, this is horrible ! migrating to a closed source bug tracker. I\'ve
used sourceforge to lodge bugs before and it wasn\'t too hard. But
perhaps trac or something similar might have been a better solution, I
realise that I\'m armchairing here, but I guess that the inkscape coders
don\'t seem to think using free software is so important. Propriatary
software wins again !

I keep hearing (
https://bugs.launchpad.net/launchpad-answers/+bug/50699) that it\'s
going to be liberated, relying on software that -may- become free would
have us using xara extreme, but.. I\'ve contributed very little to
inkscape, so I guess I don\'t get a say.

Maybe I\'m just an unreasonable man, be warned that this migration
doesn\'t cost inkscape contributions from other free software
developers.

---
#### James Henstridge - <time datetime="2007-11-28 17:50:50">28 Nov, 2007</time>

Wade: the Inkscape developers were not interested in running their own
bug tracker (see
http://sourceforge.net/mailarchive/message.php?msg\_name=1196184862.7737.20.camel%40shi),
so setting up their own Trac instance wasn\'t on the cards.

One of their requirements was an exit strategy, and we do provide XML
bug tracker dumps on request from a project owner (we don\'t currently
have an automated process for this though).

As for the usability comparison, remember that there are two groups of
users for a bug tracker: users and developers. For users, the main
features are (1) filing bugs and (2) providing followup information on
those bugs. In contrast, a developer needs to work with the entire
collection of bugs so good categorisation and search tools are needed.

While you may have been satisfied with SF.net from a user perspective,
it seems that the Inkscape developers were not satisfied with it from a
developer perspective. I hope that you find Launchpad easy to use when
filing bugs in the future.

---
#### pinky - <time datetime="2007-11-28 18:17:48">28 Nov, 2007</time>

I\'m completely with Wade Mealing. It is very sad that a free software
project migrates to a proprietary development/bug-tracking platform.

This puts Inkscape definitely in a bad light. Hope you have thought
about it or will think about it.

I agree that sourceforge is quite bad. Personally I had never understood
how developers and/or users can like sourceforge. But there are other
options than non-free software. E.g. savannah, gnome,\....

---
#### [nicu buculei](http://nicubunu.blogspot.com/) - <time datetime="2007-11-28 18:29:40">28 Nov, 2007</time>

At this step Inkscape lost me as a bug reporter/triager (I used to do
this on the sf.net tracker). I won\'t make a Launchpad account.

---
#### James Henstridge - <time datetime="2007-11-28 22:39:34">28 Nov, 2007</time>

pinky, nicu: out of interest, are there particular reasons you find it
okay to work with SourceForge.net but not Launchpad?

---
#### naisioxerloro - <time datetime="2007-11-28 22:58:56">28 Nov, 2007</time>

Hi.\
Good design, who make it?

---
#### pinky - <time datetime="2007-11-29 00:10:41">29 Nov, 2007</time>

\@James Henstridge:

As i said before i\'m also not a fan of sourceforge. This has two
reasons. First i don\'t like it technically (especially in Europe it is
often really slow) and second sourceforge isn\'t complete free software.
Personally i don\'t have a sourceforge account because of my second
point.

So basically because of my second point i also think it isn\'t OK to
work with sourceforge but i could tolerate it in the sense that a lot of
projects started at sourceforge when sourceforge was free. This projects
doesn\'t migrate knowingly to non-free software but get pushed into it.
I would of course prefer if these projects would decide to leave
sourceforge and migrate to a complete free platform but i could at least
tolerate it if they stay for some time because of their \"dullness\" and
not because of their direct decision to use non-free software.

But if someone migrates away from sourceforge and choose knowingly
non-free software than i think this is a really bad move for a free
software project. (I just want to remember Linus decision to use a
non-free version control system for Linux. This was the same mistake.
And as time has shown he get even punished for it as the right holders
decided that they doesn\'t want Linus to use it for free anymore.)

---
#### [nicu buculei](http://nicubunu.blogspot.com/) - <time datetime="2007-11-29 00:26:21">29 Nov, 2007</time>

When I joined Inkscape I already had a sf.net account. Long ago they
were almost the only game in town.\
And for a particular reason: sf.net is not tied with any distro.

---
