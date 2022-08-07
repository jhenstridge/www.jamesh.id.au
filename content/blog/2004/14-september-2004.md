---
title: '14 September 2004'
slug: 14-september-2004
date: 2004-09-15T06:54:12+08:00
tags: ['Gnome']
---

**Foundation Elections (continued)**

[bolsh](http://www.advogato.org/person/bolsh/diary.html?start=24): as I
said, many real elections make modifications to an idealised STV system
to simplify vote counting. The [counting for the `.au` senate
elections](http://www.aec.gov.au/_content/What/voting/count_senate.htm)
sounds like it takes a random sample of votes when transfering
preferences too.

Also, in my description a candidate needed to get more votes than the
quota and the quota could be fractional. In contrast, the Australian
senate elections say candidates must reach the [Droop
Quota](http://en.wikipedia.org/wiki/Droop_Quota), which is the smallest
integer greater than the quota formula I used. If you are using random
sampling for preference transfers so that each ballot has a weight of
either 0 or 1, then this is equivalent. However, if you count fractional
votes, then it does make a difference.

Since the votes are all collected electionically for the foundation
elections, it shouldn\'t be any more difficult to count the votes
exactly (which the pSTV software you pointed out trivial).

I agree that it would be interesting to get people to list preferences
on the ballot even if we don\'t switch to STV for the election (I
mentioned this in one of my foundation-list emails). The top 11
preferences could be used to perform the existing vote counting
algorithm.

**Work**

The preview release of Ubuntu will be coming out later today. While most
of the work I\'ve been doing is in some of the backend infrastructure
rather than packaging, for the past half week I\'ve been helping out
with some of the Gnome modifications. I doubt all of the changes will be
accepted up stream, but I think a number of them would be welcome
changes for Gnome 2.10.

I also now realise how bad the
[`battstat_applet`](http://cvs.gnome.org/viewcvs/gnome-applets/battstat/)
code is, and can understand why Glynn started from scratch. It seems
like a good thing to improve for 2.10. Davyd mentioned on IRC that it
would be nice if it could work with UPSs as well as laptop batteries.
[NUT](http://www.networkupstools.org/) can easily provide all the info
that the applet gets from the APM or ACPI code, so this shouldn\'t be
too difficult. I wonder how useful sysadmins would find such a feature?

**Thunderbird**

The new version of thunderbird looks quite nice. As well as the usual
incremental improvements, this release can also act as an RSS reader. It
converts items from the feeds into email messages and puts them in the
chosen folder. You can then manage them as you would your mail. It\'s an
interesting way of reading sites like planet gnome. If the feeds provide
full content like the PG does, then you probably want to turn on the
\"Show the article summary instead of loading the web page\" option. For
feeds without much content you can leave that option off and it will
load the linked web page instead.
