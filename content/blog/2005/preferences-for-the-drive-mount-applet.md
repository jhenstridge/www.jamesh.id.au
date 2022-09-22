---
title: 'Preferences for the Drive Mount Applet'
slug: preferences-for-the-drive-mount-applet
date: 2005-12-16T13:39:52+08:00
tags: ['Gnome']
---

In my previous article, I outlined the thought process behind the
redesign of the drive mount applet. Although it ended up without any
preferences, I don\'t necessarily think that it doesn\'t *need* any
preferences.

A number of people commented on the last entry requesting a particular
preference: the ability to hide certain drives in the drive list. Some
of the options include:

1.  Let the user select which individual drives to display
2.  Let the user select which classes of drive to display (floppy,
    cdrom, camera, music player, etc).
3.  Select whether to display drives only when they are mounted, or only
    when they are mountable (this applies to drives which contain
    removable media).

Of these choices, the first is probably the simplest to understand, so
might be the best choice. It could be represented in the UI as a list of
the available drives with a checkbox next to each. In order to not hide
new drives by default, it would probably be best to maintain a list of
drives to hide rather than drives to show.

It does bring up the question of how to identify what a \"drive\" is. On
my Ubuntu system, the first USB mass storage device I plug in usually
gets the same mount point. If we identify drives by their mount point,
hiding that mount point will effectively hide all of those drives.
Perhaps the [HAL](http://www.freedesktop.org/wiki/Software/hal) UDI
would be appropriate here.

The third choice is also interesting: why display an icon for a
removable media drive if there is no media in the drive? This sort of
feature could probably be implemented independently of the previously
discussed choice. It is also the sort of change that probably needs to
be addressed in `gnome-vfs` and HAL though. Fixing it at that level
would also provide the same benefit to other `GnomeVFSVolumeMonitor`
using apps, such as Nautilus.

---
### Comments:
#### Stephane Chauveau - <time datetime="2005-12-16 23:41:51">16 Dec, 2005</time>

My feeling is that the applet could change the way it displays the
drives.
The alternative way could be a single button/icon that opens a popup
window displaying all drives (a bit like the calendar window obtained by
clicking on the clock applet).

The old and the new methods could cohabitate for example, by providing
an option to limit the number of drives that can be displayed in the
panel before switching to the button mode. A side effect is that the
maximal size of the applet is known so it would make sense to use a
fixed size for the applet (applets with dynamix sizes are always a
pain).

The button could provide some information (e.g. number of drives) and it
could also \'flash\' when a drive is added or removed.

---
#### Anders Olsson - <time datetime="2005-12-17 00:00:31">17 Dec, 2005</time>

I think that a common reason that people try the drive mount applet is
because there\'s no fast and easy way to unmount/eject removable media
in gnome. One either needs to find the drive icon which exists somewhere
on the desktop which in turn is buried under all the application windows
or one needs to find an open nautilus window or open a new one where one
can right click the drive and choose eject. I\'m sure there are many
other ways as well but no really quick and easy one.

I\'m thinking this is a use case that the drive mount applet is not well
suited for and shouldn\'t need to be. Removable media is normally
automounted so I never need to mount it manually. And if I want to open
a removable drive in nautilus I can do it equally easy from the Places
menu. Maybe right-clicking the drive in the Places menu should bring up
a menu where I can unmount it as I can in nautilus?

Anyway, my point is that the only functionality that is normally needed
in regards to removable media is the ability to unmount it, which should
be provided by the desktop and not by a special applet because it is a
very common and universally needed feature. I think the drive mount
applet is more useful for drives that I need to manually mount and
unmount, such as harddrive partitions that I don\'t want permanently
mounted or network drives that are not always available.

---
#### Stephane Chauveau - <time datetime="2005-12-17 00:58:11">17 Dec, 2005</time>

\> the only functionality that is normally needed in
\> regards to removable media is the ability to unmount it

Well\... unplugging a memory card without unmounting it first is unsafe
so I tend to unmount my cards without unpluging them. Later I may have
to re-mount it.

Also, do not forget that automount is not always the right thing to do.
Within a few years, wireless drives will be very common (in key chains,
mobile phones, \...) . Do you want to automount your neigbours Wifi key
drive each time he turns it on? I do not think so.

Automount is also a security risk. First because they could carry
viruses but also because it takes only a few seconds for an outsider to
upload or download large amount of data using a simple usb key. By the
way, Gnome should have a (non-user controled) option to enforce some
kinds of authentification (password, GPG key, device ID, \...) before
any removable volume can be mounted.



---
#### Rob J. Caskey - <time datetime="2005-12-17 02:25:48">17 Dec, 2005</time>

I would suggest that if you could right click on the entry in the places
side bar in Nautilus and select Eject most people could do without this
applet.

Sincerely,
\--Rob

---
#### anon - <time datetime="2005-12-17 12:02:34">17 Dec, 2005</time>

Interesting, I am glad to hear that work is put into this. I currently
have 9 icons visible (4 x USB + 4 x NFS + 1 x DVD). I only wanted a way
to unmount my iPod.

---
