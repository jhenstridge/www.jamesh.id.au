---
title: 'Investigating OBEX over USB'
slug: investigating-obex-over-usb
date: 2007-06-18T10:14:44+08:00
tags: ['Gnome', 'Ubuntu']
---

I\'ve had a number of requests for USB support in gnome-vfs-obexftp. At
first I didn\'t have much luck talking to my phone via USB. Running the
`obex_test` utility from OpenOBEX gave the following results:

    $ obex_test -u
    Using USB transport, querying available interfaces
    Interface 0:   (null)
    Interface 1:   (null)
    Interface 2:   (null)
    Use 'obex_test -u interface_number' to run interactive OBEX test client

Trying to talk via any of these interface numbers failed. After reading
up a bit, it turned out that I needed to add a `udev` rule to give
permissions on my phone. After doing so, I got a better result:

    $ obex_test -u
    Using USB transport, querying available interfaces
    Interface 0: Nokia Nokia 6230 (null)
    Interface 1: Nokia Nokia 6230 (null)
    Interface 2: Nokia Nokia 6230 (null)
    Use 'obex_test -u interface_number' to run interactive OBEX test client

With the change, I was also able to access the phone using the `obexftp`
command line client. This seemed enough to start investigating a bit
further. The OpenOBEX API for setting up USB connections goes something
like this:

1.  The app calls `OBEX_FindInterfaces()`, which returns a list of
    `obex_interface_t` structures that represent the different
    discovered interfaces.
2.  The app picks one of the discovered interfaces (based on the
    manufacturer, product and serial number strings), then connects to
    it using `OBEX_InterfaceConnect()`.

There are a number of issues with this interface though.

-   If the phone doesn\'t provide a serial number via its USB interface
    (like my 6230 doesn\'t), the `obex_interface_t` structure is not
    enough to identify a particular phone.
-   If the phone exposes multiple OBEX USB interfaces for some reason,
    OpenOBEX lists it multiple times. In the `obex_test` output shown
    above, there was a single phone attached -- not three.
-   There is no way to tell when phones are connected or disconnected.
    While HAL can do that job for us, there is no way to map from the
    device information provided by HAL to one of the discovered
    interfaces provided by OpenOBEX.

To sum up, it shouldn\'t be difficult to hack support for USB
connections into gnome-vfs-obexftp with URLs like `obex://usb-N/` (where
N is the number of the discovered interface), but there are a number of
features I\'d need to provide a good user experience:

1.  The ability to ask OpenOBEX to connect to a particular USB device,
    rather than having to deal with its discovery interface.
2.  A good set of udev rules to grant the needed permissions on common
    phones so they don\'t need to find out why things only work as root.

---
### Comments:
#### [davidz](http://blog.fubar.dk) - <time datetime="2007-06-18 11:46:15">18 Jun, 2007</time>

Someone posted a patch to HAL that I merged that exports the so-called
\"USB Interface Decscription\" textual value

http://gitweb.freedesktop.org/?p=hal.git;a=commit;h=8e00f386dd4af855116cb1082c0ae6fd8db7ce5e

This patch is in hal 0.5.9. There\'s some more info in this thread

http://lists.freedesktop.org/archives/hal/2007-March/007761.html

It might be worth having a bunch of .fdi files in hal-info tag the
appropriate USB interface with something so you can discover them from
gnome-vfs? I bet it varies what the textual description of the interface
is given the mobile phone though. But it should be feasible.

Hope this helps and keep on rocking on OBEX! Thanks!

---
#### [davidz](http://blog.fubar.dk) - <time datetime="2007-06-18 11:47:22">18 Jun, 2007</time>

Btw, forgot to mention that one point of having it in HAL is that with
the ACL-patch (that is also in 0.5.9) we\'d use this rather than udev
rules to add ACL\'s to the device file.

---
#### James Henstridge - <time datetime="2007-06-18 12:10:27">18 Jun, 2007</time>

Hi David,

I just checked my own phone, none of the three OBEX interfaces provided
an interface description (lsusb reports iInterface = 0). From a look at
the code, the \"(null)\" bits in the obex\_test output would have
displayed these interface description strings were provided. As all
three interfaces behaved identically, I didn\'t realise that HAL needed
any extra features :)

Your suggestion of using FDI files to tag the usable interfaces seems
sensible \-- I\'d originally been planning to just look up the devices
by the interface class/subclass like OpenOBEX currently does.

That still leaves the question of how to get OpenOBEX to connect to a
device I discover with HAL, but that is an OpenOBEX problem rather than
a HAL problem.

---
#### James Henstridge - <time datetime="2007-06-18 13:48:38">18 Jun, 2007</time>

Actually, there is one area I wouldn\'t mind seeing HAL improve is to
add Bluetooth device support. If I am going to add USB support, it\'d be
nice if I could share as much discovery code between the Bluetooth and
USB cases as possible.

---
#### [Olivier Berger](http://www.olivierberger.com/weblog/) - <time datetime="2007-06-19 14:32:32">19 Jun, 2007</time>

Hi.

Nice to see such progress. For what it\'s worth, I\'ve written a small
piece on using my SE K610i phone with OBEX over USB here :

[Transfering files to the Sony Ericsson K610i from GNU/Linux through USB
+
OBEX](http://www.olivierberger.com/weblog/index.php/2006/11/12/66-transfering-files-to-the-sony-ericsson-k610i-from-gnu-linux-through-usb-obex).

Best regards,

---
