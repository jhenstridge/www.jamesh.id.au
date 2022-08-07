---
title: 'Playing Around With the Bluez D-BUS Interface'
slug: playing-around-with-the-bluez-d-bus-interface
date: 2006-10-19T12:13:34+08:00
tags: ['Gnome', 'Python', 'Ubuntu']
---

In my [previous entry](obex-in-nautilus/index.md) about using the
Maemo `obex-module` on the desktop, Johan Hedberg mentioned that
`bluez-utils` 3.7 included equivalent interfaces to the
`osso-gwconnect` daemon used by the method. Since then, the copy of
`bluez-utils` in Edgy has been updated to 3.7, and the necessary
interfaces are enabled in `hcid` by default.

Before trying to modify the VFS code, I thought I\'d experiment a bit
with the D-BUS interfaces via the D-BUS python bindings. Most of the
interesting method calls exist on the `org.bluez.Adapter` interface. We
can easily get the default adapter with the following code:

    import dbus

    bus = dbus.SystemBus()
    manager = dbus.Interface(
        bus.get_object('org.bluez', '/org/bluez'),
        'org.bluez.Manager')

    adapter = dbus.Interface(
        bus.get_object('org.bluez', manager.DefaultAdapter()),
        'org.bluez.Adapter')

At this point, it is possible to perform discovery:

    import dbus.glib
    import gtk

    def remote_device_found(addr, class_, rssi):
        print 'Found:', addr
    def discovery_complete():
        gtk.main_quit()

    adapter.connect_to_signal('RemoteDeviceFound', remote_device_found)
    adapter.connect_to_signal('DiscoveryCompleted', discovery_completed)

    adapter.DiscoverDevices()
    gtk.main()

It is also possible to configure periodic discovery, which will send
signals about devices that get found, disappear, or change name, so we
could easily implement the `obex:` directory listing that shows all
the devices found that support OBEX-FTP. One thing that isn\'t clear
from the [API
documentation](http://bluez.cvs.sourceforge.net/bluez/utils/hcid/dbus-api.txt?view=markup)
is what happens if multiple programs try to start or stop discovery at
the same time. It looks like the second program will get a
`org.bluez.Error.InProgress` error when it tries to begin discovery.
Ideally discovery would stay active til the last program interested in
the results closed. Maybe I am misunderstanding it a bit and you can
actually use the interface in this mode.

When we want to actually do OBEX-FTP with the device, we can establish
the rfcomm connection:

    rfcomm = dbus.Interface(
        bus.get_object('org.bluez', manager.DefaultAdapter()),
        'org.bluez.RFCOMM')

    # will return e.g. /dev/rfcomm0
    devname = rfcomm.Connect(bluetooth_address, 'ftp')

    # communicate with the phone via the new rfcomm device

    rfcomm.Disconnect(devname)

So it should be possible to modify `obex-method` to function with only
the daemons included in Ubuntu Edgy. All that\'s left is to do the
actual work `:)`.
