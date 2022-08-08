---
title: 'Features vs. Preferences'
slug: features-vs-preferences
date: 2005-12-16T04:52:29+08:00
tags: ['Gnome']
---

As most people know, there has been some flamewars accusing Gnome
developers of removing options for the benefit of \"idiot users\". I\'ve
definitely been responsible for removing preferences from some parts of
the desktop in the past. Probably the most dramatic is the drive mount
applet, which started off with a preferences dialog with the following
options:

-   **Mount point**: which mount point should the icon watch the state
    of?
-   **Update interval**: at what frequency should the mount point be
    polled to check its status?
-   **Icon**: what icon should be used to represent this mount point. A
    selection of various drive type icons were provided for things like
    CDs, Floppys, Zip disks, etc.
-   **Mounted Icon** and **Unmounted Icon**: if \"custom\" was selected
    for the above, let the user pick custom image files to display the
    two states.
-   **Eject disk when unmounted**: whether to attempt to eject the disk
    when the unmount command is issued.
-   **Use automount-friendly status test**: whether to use a status
    check that wouldn\'t cause an automounter to mount the volume in
    question.

These options (and the applet in general) survived pretty much intact
from the Gnome 1.x days. However the rest of Gnome (and the way people
use computers in general) had moved forward since then, so it seemed
sensible to rethink the preferences provided by the applet:

1.  Nautilus\'s volume handling has matured a lot since then, and been
    pushed down to the platform as the `GnomeVFSVolumeMonitor` API. This
    API makes it possible to enumerate mounted volumes and mount points
    on the system, so we can do a lot better than providing an entry box
    and file chooser to select a mount point.
2.  The `GnomeVFSVolumeMonitor` provides asynchronous notification of
    mount/unmount events, removing the need for the applet to poll the
    status. If the applet isn\'t polling, then there is no reason for it
    to provide the update interval preference.
3.  The `GnomeVFSVolumeMonitor` API provides icon names for volumes
    depending on the drive type. If we can detect that a disk is a
    floppy or a cdrom or whatever, why ask them what sort of icon to
    use? This change also means that the icon can be picked from the
    user\'s selected icon theme, providing better integration with the
    rest of the desktop (not to mention the accessibility benefits when
    the HighContrast icon theme is used).
4.  Certain types of volumes always make sense to eject on unmount.
    Other volumes don\'t. Since we know the volume type, we should be
    able to just do the right thing.
5.  Since the applet is no longer directly checking the mount point
    status, the \"Use automout-friendly status test\" preference
    doesn\'t make sense. But even if it was applicable, it is the sort
    of preference that only has one sane value: assuming both types of
    status check work, why wouldn\'t you want to use the one that works
    with automounters?

The other major change I made was due to a change in the types of
volumes people mount: USB devices. If you have a fixed number of mount
points/devices you care about, then the old model works pretty well. If
you have a large number of devices, and rarely plug them all in at once,
you probably don\'t want to create drive mount applets for all of them.
My solution was to alter the drive mount applet to display a button for
each user mountable volume on the system rather than one applet per
mount point.

The result was an applet with *no* preferences. However, I\'d contend
that it has more features than before. It has been improved further
since then, to provide media-type specific options (e.g. start the movie
player if you insert a DVD Video disc).

---
### Comments:
#### [Philip Langdale](http://intr.overt.org/blog) - <time datetime="2005-12-16 14:30:30">16 Dec, 2005</time>

The problem I have with the current drive mount applet (and the reason
it no longer graces my panel) is that it\'s all or nothing - you can\'t
have a subset of mountable volumes and you can\'t alter the layout. I
have a 4-in-1 flash card reader, 2 cdroms and an ide floppy drive. So, I
get dumped with 7 items inefficiently layed out (I use a single 48 pix
panel; old school). I only use 1 of the 4 flash slots, so I\'d rather
ignore the other 3, and vertical items make a lot more sense for my
panel dimensions.

---
#### Luca De Rugeriis - <time datetime="2005-12-16 14:40:39">16 Dec, 2005</time>

Same here: it would be nice if it was possible to hide some of the
buttons.

---
#### [Davyd](http://www.davyd.id.au/) - <time datetime="2005-12-16 15:52:08">16 Dec, 2005</time>

James, you have provided us with a most wonderful example of our
wonderfulness.

Philip/Luca, this is a common feature request, and is probably relevant
to people with lots of little devices, so is a patch forthwith? If you
were going to implement this, I would recommend storing a mask of drives
to hide, rather than a list of drives to show. That way new devices that
have never been seen before always appear, and could then be hidden by
the user.

---
#### [Daniel Borgmann](http://dborg.wordpress.com) - <time datetime="2005-12-16 17:31:33">16 Dec, 2005</time>

Exactly, there is a huge difference between features and options. In the
ideal case, the only choice a user \_ever\_ has to make should be \"what
do I want to do\". And that is what GNOME is all about.

Some people insist on having unlimited customizability available and I
understand that GNOME isn\'t the right desktop for them. But that is not
the same as functionality. Functionality means to me \"the ability to do
something\", not \"a specific method to do something\".

---
#### [Stephane Chauveau](http://www.chauveau-central.net) - <time datetime="2005-12-16 18:49:42">16 Dec, 2005</time>

I agree with the problem of having too many devices. The first thing to
do would be insure that their order is somewhat predictable.

I think that the problem woud better be managed at a higher level. What
I have in mind would be something like having a user preference file for
libhal where keys could be specified for known devices.

For example, a removable device could have the key \".user\_pref.show\"
with the values \"always\", \"when-mountable\"\
, \"when-mounted\" or \"never\"

---
#### [Murray Cumming](http://www.murrayc.com) - <time datetime="2005-12-16 19:11:38">16 Dec, 2005</time>

\> I only use 1 of the 4 flash slots, so I\'d rather ignore the other 3

Wouldn\'t it make sense to just automatically ignore drives that
couldn\'t be mounted, such as card slots with no cards in them? You
don\'t want to see them because there\'s nothing you could do with them.

---
#### [Ralph Wabel](http://ralph-wabel.net) - <time datetime="2005-12-16 19:42:12">16 Dec, 2005</time>

it would be enough if people can select which drives he wants to display
on the panel. Some people only want their cd/dvd drives, but the rest
they don\'t care about. I really hope such a highly requested feature
will be implemented!

---
#### Tomas Frydrych - <time datetime="2005-12-17 07:36:12">17 Dec, 2005</time>

Except \#4 is broken (see
<http://bugs.gnome.org/show_bug.cgi?id=319208>), and without a
preference to turn this \'smart\' behaviour off you are stuck with
broken and rather irritating behaviour.

---
#### bu - <time datetime="2005-12-17 08:37:32">17 Dec, 2005</time>

<http://gnomesupport.org/forums/viewtopic.php?t=8384&start=15>

---
