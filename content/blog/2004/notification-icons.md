---
title: 'Notification Icons'
slug: notification-icons
date: 2004-09-17T07:05:19+08:00
draft: false
tags: ['Gnome']
---

I decided to go ahead and write the code to allow
[Zenity](http://cvs.gnome.org/viewcvs/zenity/) to listen for commands on
stdin. It was pretty easy to add, and Glynn accepted the patch so it is
in the latest CVS version. The main difference between the
implementation and what I described earlier is that you need to pass the
`--listen` argument to Zenity to activate this mode (without it, it acts
as a one-shot notification icon where it exits when the icon is clicked
on). The easiest way to use it from a bash script is to tie Zenity to a
file descriptor like this:

> `exec 3> >(zenity --notification --listen)`

You can then feed commands to the notification icon by echoing things to
that file descriptor. For example:

> `echo "tooltip: a new tooltip" >&3`

The available commands are `icon`, `tooltip` and `visible`. When you\'ve
finished and want to kill off the icon, you can simply close the file
descriptor:

> `exec 3>&-`

Some things that would be good to add are message balloon support
(although the Gnome system tray doesn\'t seem to support them right now)
and support for animated images (useful to get the user\'s attention
while message balloons don\'t work).

One of the reasons for adding this functionality to Zenity was for use
in jhbuild. Davyd did [the initial
prototype](http://www.livejournal.com/~davyd/114890.html) for this, but
the idea for the notification icon seemed fairly generic and useful
outside of jhbuild. Also, by putting it in Zenity there is less to
maintain in jhbuild itself `:)`
