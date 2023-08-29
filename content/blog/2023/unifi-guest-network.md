---
title: "Setting up a guest network with Unifi APs"
date: 2023-08-29T20:51:48+08:00
tags:
  - Linux
  - Networking
  - UniFi
---

I've been pretty happy with the Unifi wifi access points I picked up a
few months back, but one of the things I hadn't managed to replicate
over my old setup was a guest wifi network.

If I went all-in and bought a Unifi router, this would probably be
fairly trivial to set up. But I wanted to build on the equipment I
already had for now. Looking [at some old docs][1], I'd need to get
trunked VLAN traffic to the APs to separate the main and guest
networks.

So I picked up a pair of [Netgear GS308EP POE smart
switches][2]. While they don't integrate into the Unifi network
controller like Ubiquiti switches, but they had the benefit of being
in stock and support POE on all ports.

I was using [HomePlug][3] adapters to connect between my living room
and office over the electrical wiring, so planned to connect things up
like so:

<div class="f5">

```goat
.--------.     .--------.     .----------.     .----------.     .--------.
| router |<--->| switch |<--->| homeplug |<--->| homeplug |<--->| switch |
'--------'     '--------'     '----------'     '----------'     '--------'
                   ^                                                ^
                   |                                                |
                   v                                                v
              .----------.                                     .----------.
              | unifi ap |                                     | unifi ap |
              '----------'                                     '----------'
```
</div>

While it might be best practice to have a separate VLAN for
management, I decided to keep my main network as VLAN 1. I arbitrarily
decided my guest network would be VLAN 20. The idea was to send
[tagged traffic][4] between the two switches over the homeplug
network, and also to the two APs.

## Configuring the switches

After doing the basic configuration of the switches and upgrading
their firmware, it was time to configure the VLANs. The Netgear web UI
has a number of modes for setting up VLANs of increasing complexity,
and unfortunately will reset everything if you switch modes (even if
you go from a simple mode to a more complex mode).

After reading the Netgear and Unifi docs it seemed that the final
"Advanced 802.1Q VLAN" mode was necessary, so I chose that.

To start, I clicked the "add VLAN" button to add my guest VLAN,
configuring it to be excluded on all ports except for the AP and and
Homeplug where it was configured to send tagged traffic.

I then edited the default VLAN, and set it to tag traffic to the
Homeplug adapter and send untagged traffic to the AP (since traffic
from the controller needs to be untagged).

I then made the same configuration changes on the second switch.

## Configuring the router

Unfortunately, the TP-Link router I'm currently using doesn't support
802.1Q tagging, so configuration is a bit different there.

Instead, it has a basic port-based VLAN setup where different ports on
the router can be assigned to different VLANs and optionally be
isolated from each other. So I split one of the router ports off into
an isolated network to act as the guest network.

In order to get the traffic correctly tagged, I connected two patch cables from the router to one of the switches, and configured it as:

* For the main VLAN, send untagged traffic to the first port and exclude the second port.
* For the guest VLAN, exclude the first port and send untagged traffic to the second port.
* Update the PVID table so that untagged traffic received from the second port is treated as guest VLAN traffic.

## Configuring Unifi Network

With all the above configuration, the Unifi Network controller could
still see the access points, which was a good start. All that was left
was to set up the guest wifi.

First of all, I needed to tell the controller about the guest VLAN:

1. From the Networks page of the settings, click "Create New" under "Virtual Networks".
2. Pick a name (I chose "Guest"), set the router to "Third-party Gateway", and the VLAN ID to the guest VLAN's ID.

Next, we need to set up a new wifi network:

1. From the Wifi page of the settings, click "Create New".
2. Set the name and password as appropropriate.
3. For the network, pick the new virtual network we just created.

Everything else can be left as defaults. With that, the new wifi
network is available. When connecting, the router hands out a DHCP
address on it's guest network, indicating that the traffic is being
correctly tagged.

## QR Code Login for Mobile Devices

Modern mobile operating systems can log into a wifi network via a QR
code. This is just a standard QR code [containing data in this
format][5]:

```
WIFI:S:${network};T:WPA;P:${password};;
```

[Inkscape][6] works pretty well for turning a string like this into a
QR code. From the menu, pick Extensions -> Render -> Barcode -> QR
Code, and paste in the string. The result can then be printed out
ready for people to scan.


[1]: https://web.archive.org/web/20230203173816/https://help.ui.com/hc/en-us/articles/204962144-UniFi-VLAN-Traffic-Tagging
[2]: https://www.netgear.com/au/business/wired/switches/plus/gs308ep/
[3]: https://en.wikipedia.org/wiki/HomePlug
[4]: https://en.wikipedia.org/wiki/IEEE_802.1Q
[5]: https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11
[6]: https://inkscape.org/
