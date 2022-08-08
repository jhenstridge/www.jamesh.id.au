---
title: '22 October 2003'
slug: 22-october-2003
date: 2003-10-23T02:47:35+08:00
---

**Laptop**

I started running out of space on my laptop, so decided it would be
easier to buy a new hard disk rather than clean things up (after all, I
could get a 40GB drive for about AU\$200, which would give me more than
3 times as much storage, and had almost identical power requirements).
If only things were that easy \...

After backing everything up, the first problem was taking the old hard
disk out of the machine. The
[m300](http://h20000.www2.hp.com/bizsupport/TechSupport/Home.jsp?locale=en_US&prodTypeId=321957&prodSeriesId=96234&cc=us)
is quite a nice machine, as you only need to undo one screw to remove
the hard drive mounting. Getting the hard drive out of the mounting was
a bit more of a problem as there were two torx screws holding the drive
in. Moreover, I didn\'t have access to a small enough torx driver `:(`.
Luckily the screw heads were raised enough that it was possible to undo
them using some pliers without damaging anything.

After getting the new drive into the mounting frame and into the
machine, I needed to get Windows 98 onto the drive. This was required to
get the hibernation working under Linux (the BIOS saves the contents of
memory to a special file on the Windows partition). It turned out that
the CD that came with the laptop was a quick restore disk, and wanted to
create a full 40GB partition, rather than use the use the smaller
partition I had already created. It them proceeded to screw up the
restore, leaving me with a system that (a) wouldn\'t boot fully, and (b)
was convinced that there were errors on the hard disk, but just
couldn\'t find them. I guess that the restore CD managed to mis-format
the drive somehow. In the end, I had to borrow a 98 CD and do a clean
install, which worked perfectly (and let me install to a smaller
partition). I can see how a quick restore CD could be useful in many
common cases, but this one was nowhere near as robust as I would have
liked.

Compared to this, getting Linux up and running was trivial. After
completing the restore, I did a few tests with `hdparm -Tt` which showed
that the new disk had a read performance of 25MB/s (in comparison, the
old disk did 13MB/s), which has resulted in noticably shorter compile
times on the laptop. It is also a lot quieter when busy.

This should put off the need to get a new laptop for quite a while.

**Gnome 2.5**

Updated my system to CVS head, and things are looking good. The new
Nautilus feels even faster (especially in spatial mode). Apparently
metadata plugins are planned for 2.6, which should be interesting. It
should allow people to implement things like
[TortoiseCVS](http://www.tortoisecvs.org/), augmenting the existing
views rather than creating a completely new view like
[Apotheke](http://apotheke.berlios.de/) does.
