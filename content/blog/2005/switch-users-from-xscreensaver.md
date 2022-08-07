---
title: 'Switch users from XScreenSaver'
slug: switch-users-from-xscreensaver
date: 2005-12-05T10:49:43+08:00
tags: ['Gnome', 'Ubuntu']
---

[Joao](http://www.advogato.org/person/jvic/diary.html?start=29): you can
configure XScreenSaver to show a \"Switch User\" button in it\'s
password dialog (which calls `gdmflexiserver` when run). This lets you
start a new X session after the screen has locked. This feature is
turned on in Ubuntu if you want to try it out.

Of course, this is not a full solution, since it doesn\'t help you
switch to an existing session (you\'d need to guess the correct
Ctrl+Alt+F*n* combo). There is code in gnome-screensaver to support this
though, giving you a list of sessions you can switch to.

---
### Comments:
#### [Mike](http://mike.polycat.net) - <time datetime="2005-12-05 23:00:12">1 Dec, 2005</time>

Although it doesn\'t list sessions that are currently logged in, if you
try to log in again with GDM, it brings up a prompt asking you if you
want to start a new session or return to your other one. So while
perhaps not as convenient as allowing you to see which users are logged
in, you don\'t have to just guess the correct Fn key to press.

---
#### Craig Ringer - <time datetime="2005-12-06 00:25:51">2 Dec, 2005</time>

For starting a new session from an existing one, you can always just
make a launcher for gdmflexiserver. Fedora Core 4 has a precreated one
in Applications-\>System Tools-\>New Login in the GNOME menus; I don\'t
know about Ubuntu.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-12-06 02:11:59">2 Dec, 2005</time>

Craig: I\'m aware that there is a menu item to run gdmflexiserver (jvic
mentioned it too in the post this one replies to).

That doesn\'t help you if you\'re sitting at a workstation that someone
else has logged into and locked the screen on. This is where the
\"switch users\" button comes in handy.

---
####  - <time datetime="2005-12-06 06:16:20">2 Dec, 2005</time>

I\'m fairly sure only gnome-screensaver has this switch user button, not
XScreensaver. Or did Ubuntu patch XScreensaver?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-12-06 12:54:30">2 Dec, 2005</time>

anonymous: the feature has existed in xscreensaver since about March. It
may not be turned on by default though.

---
#### Andre - <time datetime="2005-12-11 02:29:14">0 Dec, 2005</time>

How can one activate this feature?\
What does one need to configure?

---
