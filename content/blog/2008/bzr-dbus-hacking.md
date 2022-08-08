---
title: 'bzr-dbus hacking'
slug: bzr-dbus-hacking
date: 2008-03-27T23:45:17+09:00
tags: ['Bazaar', 'D-Bus']
---

When working on my [bzr-avahi
plugin](bzr-avahi/index.md), Robert
asked me about how it should fit in with his
[bzr-dbus](https://launchpad.net/bzr-dbus) plugin. The two plugins offer
complementary features, and could share a fair bit of infrastructure
code. Furthermore, by not cooperating, there is a risk that the two
plugins could break when both installed together.

Given the dependencies of the two packages, it made more sense to put
common infrastructure in bzr-dbus and have bzr-avahi depend on it. That
said, bzr-dbus is a bit more difficult to install than bzr-avahi, since
it requires installation of a D-Bus service activation file. After
looking at the code, it seemed that there was room to simplify how
bzr-dbus worked and improve its reliability at the same time.

The primary purpose of bzr-dbus is to send signals over the session bus
whenever the head revision of a branch changes. This was implemented
using a daemon that is started using D-Bus activation, and sends out the
signals in response to method calls made by short lived bzr processes.

While this seems to be the design the [dbus-python
tutorial](http://dbus.freedesktop.org/doc/dbus-python/doc/tutorial.html)
guides you to use, I don\'t think it is the best fit for bzr-dbus. The
approach I took was to do away with the daemon altogether: the D-Bus
session bus does a pretty good job of broadcasting the signals on its
own.

The code that previously asked the broadcast daemon to send the revision
signal was changed to simply send the signal. The following helper made
this pretty easy to do without having to write any extra classes to emit
the signals:

    def send_signal(bus, dbus_interface, signal_name, signature, *args):
        """Send a signal on the bus."""
        message = dbus.lowlevel.SignalMessage('/', dbus_interface, signal_name)
        message.append(signature=signature, *args)
        bus.send_message(message)

With these changes, the commit hook now only needs to connect to the
session bus and fire off the signal and return. Previously it was
connecting to the bus, getting an the broadcast service (which might
involve activating it), sending a method call message and waiting for a
method return message. The new code is faster and if no one is listening
for the signals, it only wakes the bus.

For code that was consuming the signals, they had to switch to the
`bus.add_signal_receiver()` method to register the callbacks, which
allows you to subscribe to a signal irrespective of its origin.

The only missing feature with these changes was annotating the signals
with additional URLs when the branch was being shared over the network.
As these additional URLs are only really interesting when accessing the
branch remotely, I moved the functionality to the \"bzr lan-notify\"
command so that it annotates the revision announcements just before
broadcasting them to the local network.

With all the changes applied, the D-Bus API consists entirely of signal
emissions, which gives a looser coupling between the various components:
each component will happily function in the absence of the others, which
is great for reliability.

Once the patches are merged, I\'ll have to look at porting bzr-avahi to
this infrastructure. Together, these two plugins offer compelling
features for local network collaboration.
