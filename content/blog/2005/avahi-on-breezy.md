---
title: 'Avahi on Breezy'
slug: avahi-on-breezy
date: 2005-11-01T17:38:15+08:00
tags: ['Avahi', 'Ubuntu']
---

During conferences, it is often useful to be able to connect to connect
to other people\'s machines (e.g. for collaborative editing sessions
with [Gobby](http://gobby.0x539.de/)). This is a place where mDNS
hostname resolution can come in handy, so you don\'t need to remember IP
addresses.

This is quite easy to set up on Breezy:

-   Install the `avahi-daemon`, `avahi-utils` and `libnss-mdns` packages
    from universe.
-   Restart dbus in order for the new system bus security policies to
    take effect with \"`sudo invoke-rc.d dbus restart`\".
-   Start `avahi-daemon` with \"`sudo invoke-rc.d avahi-daemon start`\".
-   Edit `/etc/nsswitch.conf`, and add \"`mdns`\" to the end of the
    \"`hosts:`\" line.

Now your hostname should be advertised to the local network, and you can
connect to other hosts by name (of the form `hostname.local`). You can
also get a list of the currently advertised hosts and services with the
`avahi-discover` program.

While the hostname advertising is useful in itself, it should get a lot
more useful in Dapper, as more programs are built with mDNS support.

---
### Comments:
#### lp - <time datetime="2005-11-02 02:02:48">2 Nov, 2005</time>

avahi-browse is not able to show you a list of advertised \*hosts\*.
This is a limitation of the mDNS protocol. Only services may be
enumerated

---
#### Ross - <time datetime="2005-11-02 03:17:04">2 Nov, 2005</time>

Assuming you run a SSH daemon, copy ssh.server from
/usr/share/doc/avahi-daemon/examples/ to /etc/avahi/services (iirc) and
Avahi will advertise your SSH server.

lp, avahi hacks around that fact by exporting a \"workstation\" service
automatically. :)

---
#### lp - <time datetime="2005-11-02 07:35:43">2 Nov, 2005</time>

It\'s not just avahi that does this. Apple does it too.

---
#### ed__ - <time datetime="2005-11-02 15:42:36">2 Nov, 2005</time>

you can also add \'local\' to the /etc/resolv.conf search line so that
non-fqdn\'s are automatically queried against .local. saves a few
keystrokes if you can stand the security implications.

---
#### Chris Stankevitz - <time datetime="2005-11-03 11:21:25">3 Nov, 2005</time>

FYI, just found this entry from google:

[http://blogs.gnome.org/view/jamesh/2005/08/29/0](comparison-of-configsaliases-in-bazaar-cvs-and-subversion.md)

Thanks so much, it was a big help!

Chris

---
