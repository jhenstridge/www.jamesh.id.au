---
title: '6 September 2004'
slug: 6-september-2004
date: 2004-09-07T04:12:31+08:00
draft: false
tags: ['JHBuild']
---

**linux.conf.au**

The LCA2004 team have put together the conference CD and DVD. Apparently
they will arrive in the mail in about a week.

They put the CD contents on the web first, and I was a bit disappointed
that the recording of my talk was missing (it does include my slides
though). However, when they put the DVD contents up I saw that it
included a video recording of the talk, which is pretty cool.

There are links to the CD and DVD contents [on the
wiki](http://twiki.linux.org.au/twiki/bin/view/Main/LCA2004Videos). The
video recording can be found by following one of the \"Explore DVD\"
links, and looking at the entry second from the bottom. There is also a
video of Havoc\'s keynote in there.

**jhbuild**

It sounds like [Fluendo](http://www.fluendo.com/) are looking at using
the [Subversion](http://subversion.tigris.org/) support I added to
jhbuild. There were a few bugs in the code that
[jdahlin](http://www.advogato.org/person/jdahlin/) fixed, but it seems
to be working pretty well. I still need to fix up the
[Arch](http://www.gnuarch.org/) support so that you don\'t need `tla`
unless you actually build a module managed by Arch.

I\'ve also dropped one of the old versions of Automake (1.6) from the
bootstrap moduleset and sanity checks. Maybe after Gnome 2.8 is out we
can clean up the last few modules still requiring Automake 1.4, which
should drop the number of Automake versions I need to deal with even
further.

**Elections**

Today is the last day people can enrol to vote in the federal election.
Last week we had John Howard defending one of his part members, Trish
Worth, for [comparing refugees to
animals](http://www.news.com.au/common/story_page/0,4057,10628293%255E421,00.html)
at a forum organised by the group Justice for Refugees.

There is also a Liberal (Peter King) who [lost preselection, but is
still running as an
independent](http://www.crikey.com.au/politics/2004/09/03-0006.html). He
has been accused of splitting the conservative vote, which is a bit
strange. I\'d assume that conservatives who vote for him would give
their second preference to the Liberal candidate, and vice versa. What
might happen is that Labor voters might pick the independent candidate
over the Liberal candidate (this happened in my electorate when a
similar thing happened a few years back).

Meanwhile, the National party leader is going round telling people that
[the Greens are really
communists](http://www.theage.com.au/articles/2004/09/06/1094322715096.html):
*\"They are watermelons. many of them - green on the outside and very,
very, very red on the inside.\"*

One other weird thing was the postal vote applications sent out by the
current MP. The weird thing was that they came with reply paid envelopes
to send the application back to the MP instead of the
[AEC](http://www.aec.gov.au/). She explained why in response to [a
letter in the local
paper](http://www.postnewspapers.com.au/20040904/letters/005.shtml), but
it still seems a bit weird for the applications to pass through the
office of the currently elected member.
