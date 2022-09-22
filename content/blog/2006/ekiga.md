---
title: 'Ekiga'
slug: ekiga
date: 2006-04-11T06:30:06+08:00
tags: ['Gnome', 'Ubuntu']
---

I\'ve been testing out [Ekiga](http://www.ekiga.org/) recently, and so
far the experience has been a bit hit and miss.

-   Firewall traversal has been unreliable. Some numbers (like the
    [SIPPhone echo test](17474743246@proxy01.sipphone.com)) work great.
    In some cases, no traffic has gotten through (where both parties
    were behind Linux firewalls). In other cases, voice gets through in
    one direction but not the other. [Robert
    Collins](http://www.robertcollins.net/) has some [instructions on
    setting up
    siproxd](http://advogato.org/person/robertc/diary.html?start=48)
    which might solve all this though, so I\'ll have to try that.
-   The default display for the main window is a URI entry box and a
    dial pad. It would make much more sense to display the user\'s list
    of contacts here instead (which are currently in a separate window).
    I rarely enter phone numbers on my mobile phone, instead using the
    address book. I expect that most VoIP users would be the same,
    provided that using the address book is convenient.
-   Related to the previous point: the [Ekiga.net registration
    service](http://www.ekiga.net/) seems to know who is online and who
    is not. It would be nice if this information could be displayed next
    to the contacts.
-   Ekiga supports multiple sound cards. It was a simple matter of
    selecting \"Logitech USB Headset\" as the input and output device on
    the audio devices page of the preferences to get it to use my
    headset. Now I hear the ring on my desktop\'s speakers, but can use
    the headset for calls.
-   It is cool that Ekiga supports video calls, but I have no video
    camera on my computer. Even though I disabled video support in the
    preferences, there is still a lot of knobs and whistles in the UI
    related to video.

Even though there are still a few warts, Ekiga shows a lot of promise.
As more organisations provide SIP gateways become available (such as the
[UWA](http://www.uwa.edu.au/) gateway), this software will become more
important as a way of avoiding expensive phone charges as well as a way
of talking to friends/colleagues.

---
### Comments:
#### Daniel Frey - <time datetime="2006-04-12 02:37:55">12 Apr, 2006</time>

I have a Logitech USB Headset, too, and the fact it doesn\'t work with
Ekiga is not an Ekiga problem. Try plugging it into another USB port,
probably leaving out a HUB and trying a port at the computer itself.
More info here: <http://bugzilla.gnome.org/show_bug.cgi?id=329609>

Daniel

---
####  - <time datetime="2006-04-12 02:50:43">12 Apr, 2006</time>

Sorry for the noise, I misread what you wrote. Obviously, you don\'t
have the problem I had. Daniel

---
#### [-](http://-) - <time datetime="2006-04-19 22:29:46">19 Apr, 2006</time>

The fact that incoming connections (such as sound) aren\'t let in
through a Linux NAT is a feature. If you have a Linux firewall, you can
also try conntrack\_sip from Netfilter unstable. It works just like
conntrack\_ftp, no configuration necessary.

---
#### HENOKE - <time datetime="2006-04-25 06:14:22">25 Apr, 2006</time>

i am trying to get the source code for SIP based VOIP so it can guide me
in my project
can u help me please

---
