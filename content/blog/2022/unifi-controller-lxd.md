---
title: "Running the UniFi Controller under LXD"
date: 2022-10-27T17:54:13+08:00
tags:
  - Linux
  - Networking
  - Ubuntu
  - UniFi
---

A while back I bought some UniFi access points. I hadn't gotten round
to setting up the Network Controller software to properly manage them
though, so thought I'd dig into setting that up.

<!--more-->

It's nice that Ubiquiti provides the controller software through an
apt repository, but it turns out to depend on MongoDB which is [no
longer packaged][1] in the latest Ubuntu LTS release due to the SSPL
licensing change. Further more the controller specifically asks for a
MongoDB before 4.0, again likely due to the licensing change.

A while back Dustin Kirkland [wrote up a guide for running the
controller under LXD][2], so I thought I'd give that a go. It's been 6
years since that post though, so some of it was a bit out of date
(both on the Ubuntu side and Ubiquiti).

This guide is based on my experience setting things up on Ubuntu
Server 22.04 LTS, but will probably work for other releases from
around that time.


## Bridge the Ethernet Device

By default, LXD containers sit on their own network and are connected
to the rest of the world via a dnsmasq/NAT. I wanted the controller to
sit on the network so that layer 2 device discovery works, so the
container needs to sit on the main network.

This is done by creating a new bridge interface, and adding the main
interface to it. Other virtual interfaces can then be added to the
bridge so their traffic can make it out to the LAN.

As the Ubuntu Server install had set up my network config via Netplan,
I decided to continue using that. I edited the config file in
`/etc/netplan/` to read:

```yaml
network:
  version: 2
  ethernets:
    enp2s0:
      dhcp4: false
  bridges:
    br0:
      interfaces:
        - enp2s0
      macaddress: NN:NN:NN:NN:NN:NN
      dhcp4: true
```

The MAC address I specified here is that of the `enp2s0` interface:
without it, the `br0` interface was assigned a randomised MAC
address. This isn't strictly necessary, but meant the server kept the
same DHCP leases as before.

Now I just need to remember to treat `br0` as the main network
interface rather than `enp2s0`.


## Setting up the Container

Simos Xenitellis [wrote up a post about how to put LXD containers on a
bridge][3], so I basically did the same. First we create a profile
fragment to create a bridged ethernet device:

```sh
lxc profile create br0
lxc profile edit br0 <<EOF
description: Bridged networking profile
devices:
  eth0:
    name: eth0
    nictype: bridged
    parent: br0
    type: nic
EOF
```

I can then launch a new Ubuntu 20.04 container using the bridged
Ethernet profile:

```
lxc launch -p default -p br0 ubuntu:focal unifi-controller
```

Starting a shell with `lxc shell unifi-controller`, I could verify
that the container was assigned an address by the LAN's DHCP server.

I also took the opportunity to reboot the server at this point to
verify that the container would start on boot, and have keep the same
MAC address.


## Installing the Controller into the container

I used Ubiquiti's [APT installation guide][4]. Those instructions deal
with even older Ubuntu versions, so a number of the steps can be
skipped. In the end, these were the only commands I needed to run from
the `lxc shell` shell session:

```sh
wget -O /etc/apt/trusted.gpg.d/unifi-repo.gpg https://dl.ui.com/unifi/unifi-repo.gpg
echo 'deb https://www.ui.com/downloads/unifi/debian stable ubiquiti' > /etc/apt/sources.list.d/unifi-repo.list
apt update
apt install openjdk-8-jre-headless unifi
```

At this point, the controller is running, so the rest is configured
through the web interface at (substituting in the container's IP
address):

`https://NNN.NNN.NNN.NNN:8443/`

After providing my UniFi account credentials to the setup wizard, I
could set up the network. The controller was able to discover and
adopt the APs without any special configuration. Even remote
management was possible via the [UniFi Network Portal website][5]
(although not through the newer [UniFi Portal website][6]).


## Future

While I've been impressed with the performance of the APs and the
extra visibility the controller gives into what's going on with the
network, it is a bit concerning to see how much out of date software
it relies on. OpenJDK 8 is fairly long in the tooth, and MongoDB 3.6.x
support ended in April last year.

It seems Ubiquiti has been migrating away from self-hosted controllers
to running their software on dedicated "UniFi OS Console" devices,
which run a different version of the software. Although not all of the
console devices can run the same set of UniFi applications, giving
them a bit of an uncertain future too.

But given Ubuntu 20.04's regular support period runs until April 2025,
I guess I'll stick with this setup until then and see what the device
landscape looks like at that point.


[1]: https://bugs.launchpad.net/ubuntu/+source/mongodb/+bug/1879494
[2]: https://blog.dustinkirkland.com/2016/12/unifi-controller-in-lxd.html
[3]: https://blog.simos.info/how-to-make-your-lxd-containers-get-ip-addresses-from-your-lan-using-a-bridge/
[4]: https://help.ui.com/hc/en-us/articles/220066768-UniFi-How-to-Install-and-Update-via-APT-on-Debian-or-Ubuntu
[5]: https://network.unifi.ui.com/
[6]: https://unifi.ui.com/
