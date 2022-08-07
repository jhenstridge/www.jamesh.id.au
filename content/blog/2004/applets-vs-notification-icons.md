---
title: 'Applets vs. Notification Icons'
slug: applets-vs-notification-icons
date: 2004-09-17T11:21:47+08:00
draft: false
tags: ['Gnome']
---

It seems that a lot of people get confused by what things on the panel
should be applets and what should be notification icons. Originally, the
main difference between the two was this:

-   The lifecycle of an applet is managed by the panel, which in turn is
    tied to the lifecycle of the session. So applets generally live for
    the length of the session (unless they are added/removed part way
    through a session).
-   Notification icons are more transient. Their lifecycle is linked to
    whatever app they were created by. Once the app exits the
    notification icon goes away too.

There are some other differences though:

-   Applets can be moved around on the panel while notification icons
    are constrained to the system tray. If you accept that notification
    icons are transient then it isn\'t that big a deal.
-   KDE also implements the system tray spec, so a notification icon can
    be used on both desktops (plus any other desktop that implements the
    spec). In contrast, Gnome applets are Bonobo controls which makes
    them a bit difficult to use on other desktops.
-   The panel can merge menu items into the context menu of applets, and
    supports middle click drag to move applets.
-   The system tray is supposed to be able to display \"message
    balloons\" for the notification icons. This doesn\'t seem to work
    properly though. The reason for getting the system tray to show the
    balloons is so you don\'t get multiple applets popping up such
    notices on top of each other, and to make it easier for the user to
    manage such notifications.

Due to these differences there are a number of notification icons such
as Novell\'s [netapplet](http://cvs.gnome.org/viewcvs/netapplet/) which
more closely follow the lifecycle of an applet but are notification
icons for cross desktop compatibility.

While talking with Mark on IRC, it became apparent that a number of the
applets included with Gnome aren\'t strictly linked to the session\'s
lifetime. For example, my laptop has a PCMCIA wireless adapter, so I put
the wireless applet on my panel to show the signal strength. However, it
doesn\'t really make sense to display the applet when the card is
unplugged.

Similarly, if I share my home directory between a number of computers,
it doesn\'t make sense to show the volume control applet on systems
without a sound card or the battery status applet on systems without a
battery. So perhaps these applets shouldn\'t really be tied to the
panel\'s life cycle.

With infrastructure like
[NetworkManager](http://cvs.gnome.org/viewcvs/NetworkManager/) where
there is a user-level daemon used to communicate with the user when
necessary, it would make sense for that daemon to provide network status
as notification icons. This way the icons would only appear when the
associated device was attached. Something similar could be done for the
volume control and battery status applets \-- query HAL to see if they
need to be loaded.

However, with such long lasting notification icons you probably want
some of the features of applets such as being able to move them round a
bit. This indicates that it might not make so much sense to make such a
big distinction between applets and notification applets.

I wonder how difficult it would be to extend the system
tray/notification icon spec to handle the features applets currently
have?. From a quick look, the additional features include:

1.  Some way for icons to cooperate with the panel to handle moving
    icons around.
2.  Some way to uniquely identify applets so that the panel can place
    them in the same location next time the icon is created.
3.  Provide some standard context menu items. The standard ones that
    applets have merged in are \"Move\", \"Lock\" and \"Remove from
    panel\". Only the first two would need additions to handle.
4.  Better size negotiation. An applet can query the width and
    orientation of a panel when deciding what its size should be. I
    don\'t think a notification icon can do so.
5.  Figure out a good way to start notification icons on session
    startup.
6.  If notifcation icons can be moved to anywhere on the panel, where
    should truely transient icons be placed the first time? Currently
    they are placed in the system tray, which provides a convenient
    place for the user to expect to see such notifications.

This should also make it easier to provide more full featured panel
widgets that work cross desktop. I wonder how feasible it is?
