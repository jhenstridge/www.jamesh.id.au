---
title: 'Drive Mount Applet (again)'
slug: drive-mount-applet-again
date: 2005-12-17T13:56:31+08:00
tags: ['Gnome']
---

[Thomas](http://thomas.apestaart.org/log/index.php?p=331): that
behaviour looks like a bug. Are all of those volumes mountable by the
user? The drive mount applet is only meant to show icons for the mount
points the user can mount.

Note also that the applet is using the exact same information for the
list of drives as Nautilus is. If the applet is confusing, then
wouldn\'t Nautilus\'s \"Computer\" window also be confusing?

To help debug things, I wrote a little program to dump all the data
provided by `GnomeVFSVolumeMonitor`:

> <http://www.gnome.org/~jamesh/code/gvfs-list-drives.c>

Does the output look sane for you? In particular, are any drives or
volumes marked \"user visible\" that should not be?

---
### Comments:
#### [Marius Gedminas](http://mg.b4net.lt/) - <time datetime="2005-12-18 00:08:33">18 Dec, 2005</time>

The drive mount applet shows two icons on my thinkpad: a floppy drive
(which I don\'t have), and a CD drive (which is the only one I want).

I\'m not sure how GNOME could figure out that the floppy drive doesn\'t
exist, since even the kernel thinks it is there.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-12-18 00:25:38">18 Dec, 2005</time>

Marius: do you happen to have an entry in /etc/fstab for the floppy
drive mount point? If you remove it, Gnome will probably stop thinking
you have a floppy drive.

---
#### [Jeremy Nickurak](http://bg.rifetech.com) - <time datetime="2005-12-18 14:11:53">18 Dec, 2005</time>

The \"Computer\" window has text labels for all icons in it, making it
substantially more navigable, although much more desktop-space-greedy.

---
