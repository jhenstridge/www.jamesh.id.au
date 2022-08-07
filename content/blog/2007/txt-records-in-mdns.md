---
title: 'TXT records in mDNS'
slug: txt-records-in-mdns
date: 2007-06-15T13:27:54+08:00
tags: ['Gnome']
---

[Havoc](http://log.ometer.com/2007-06.html#14 "Finding Your Local Network"):
for a lot of services advertised via mDNS, the client doesn\'t have the
option of ignoring TXT records if it wants to behave correctly.

For example, the [Bonjour Printing
Specification](http://developer.apple.com/networking/bonjour/BonjourPrinting.pdf)
puts the underlying print queue name in a TXT record (as multiple
printers might be advertised by a single print server). While it says
that the server can omit the queue name (in which case the default queue
name \"auto\" is used), a client is not going to be able to do what the
user asked without checking for the presence of the record.

Rather than thinking of TXT records as optional data, it is better to
think of them as \"stuff that is can not be used to perform searches\".
In the printer example above, the fact that you can\'t search by print
queue name is not a problem because users instead pick a printer based
on the human readable service name which is exposed as a DNS name.

In your example of including session and machine identifiers in TXT
data, it would be enough to tell a client that two services belonged to
the same machine or session, but it wouldn\'t let you do searches like
\"find all the card game servers belonging to the same session as the
guy I\'m chatting with\".  For that you\'d also need to advertise DNS
names that include the machine identifier or session identifier.
