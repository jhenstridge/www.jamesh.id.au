---
title: 'NBN talk at PLUG'
slug: nbn-talk-at-plug
date: 2012-03-17T22:47:37+08:00
---

Earlier in the week, I attended a [PLUG](http://www.plug.org.au/)
discussion panel about the [National Broadband
Network](http://en.wikipedia.org/wiki/National_Broadband_Network). 
While I had been following some of the high level information about the
project, it was interesting to hear some of the more technical
information.

The evening started with a presentation by Chris Roberts from [NBN
Co](http://www.nbnco.com.au/), and was followed by a panel discussion
with Gavin Tweedie from [iiNet](http://www.iinet.net.au/) and Warrick
Mitchel from [AARNet](http://www.aarnet.edu.au/).

{{< figure src="plug-nbn-panel.jpg"
        caption="James Bromberger introducing the panel: Chris Roberts (NBN Co), Gavin Tweedie (iiNet) and Warrick Mitchel (AARNet)" >}}

One question I had was when they\'ll get round to building out the
network where I live.  There is a [rollout map on the NBN Co
site](http://www.nbnco.com.au/rollout/rollout-map.html), but it
currently only shows plans for works that will commence within a year. 
Apparently they plan to release details on the three year plan by the
end of this month, so hopefully my suburb will appear in that list.

The NBN is being built on top of three methods of connection: [GPON
fibre](http://en.wikipedia.org/wiki/Passive_optical_network) for built
up areas, fixed [LTE](http://en.wikipedia.org/wiki/Long_Term_Evolution)
wireless (non roaming) for the smaller towns where it is not economical
to provide fibre, and satellite broadband for the really remote areas. 
All three connection methods provide a common interface to service
providers, so companies that provide services over the network are not
required to treat the three methods differently.  The wireless and
satellite connections will initially run at 12Mb/s down and 1Mb/s up,
while fibre connections can range from 25/5 to 100/40 (with the higher
connection speeds incurring higher wholesale prices).  It should be
quite an improvement over the upload speed  I\'m currently getting on
ADSL2.

Chris brought in some sample \"User Network Interface\" (UNI) boxes that
would be used on premises with a fibre connection.  It provided 4
gigabit Ethernet ports, and 2 telephony ports.

{{< figure src="nbn-box.jpg"
        caption="The inside of a current generation NBN interface box" >}}

Rather than the 4 Ethernet ports being part of a single network as
you\'d expect for similar looking routers, each port represents a
separate service.  So the single box can support connections to 4 retail
ISPs, or for any other services delivered over the network (e.g. a cable
TV service).  You would still need a router to provide firewall, NAT and
wifi services, but since it only requires Ethernet for the WAN port
there should be a bit more choice in routers than if you limit yourself
to ones with ADSL modems built in.  In particular, it should be easier
to find a router capable of running an open firmware like OpenWRT or
CeroWRT.

The box also acts as a
[SIP](http://en.wikipedia.org/wiki/Session_Initiation_Protocol "Session Initiation Protocol")
[ATA](http://en.wikipedia.org/wiki/Analog_telephone_adapter "Analog Telephone Adapter"),
where each of the two telephony ports can be configured to talk to the
servers of different service providers.

It is also possible for NBN Co to remotely monitor the UNI boxes in
people\'s houses, so they can tell when they drop off the network.  This
means that they have the ability to detect and respond to faults without
relying on customer complaint calls like we do for the current Telstra
copper network.

Since the NBN is supposed to provide a service equivalent to the current
copper telephone network, the UNI box is paired with a battery pack to
keep the telephony ports active during black outs, similar to how a
wired telephone draws power from the exchange.  This battery pack is
somewhat larger than the UNI box, holding a 7.2 Ah lead acid battery. 
At 10W, this can keep the box running for around 8 hours.  The battery
pack will automatically cut power before it is completely drained, but
has an emergency switch to deliver the remaining energy at the expense
of ruining the battery.

**Next PLUG Event**

If you\'re in Perth, why not come down to the next PLUG event on March
26th?  It is an open source themed pub quiz at the Moon & Sixpence. 
Last year\'s quiz was a lot of fun, and I expect this one will be the
same.

---
### Comments:
#### Raphael - <time datetime="2012-03-19 15:00:44">19 Mar, 2012</time>

What sort of technology is used on the optical side ? \*pon, ethernet
\...?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2012-03-19 15:14:28">19 Mar, 2012</time>

\@Raphael: as mentioned in the post, it is GPON.

---
