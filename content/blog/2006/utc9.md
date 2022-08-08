---
title: 'UTC+9'
slug: utc9
date: 2006-12-04T11:46:35+09:00
tags: ['Gnome', 'Launchpad', 'Python', 'Ubuntu']
---

Daylight saving started yesterday: the first time since 1991/1992 summer
for Western Australia. The legislation finally passed the upper house on
21st November (12 days before the transition date). The updated
[`tzdata`](ftp://elsie.nci.nih.gov/pub/) packages were released on 27th
November (6 days before the transition). So far, there hasn\'t been an
updated package released for Ubuntu (see [bug
72125](https://bugs.launchpad.net/bugs/72125)).

One thing brought up in the Launchpad bug was that not all applications
used the system `/usr/share/zoneinfo` time zone database. So other
places that might need updating include:

-   [Evolution](http://www.gnome.org/projects/evolution/) has a database
    in `/usr/share/evolution-data-server-$version/zoneinfo/` that is in
    iCalendar `VTIMEZONE` format.
-   [Java](http://www.java.net/) has a database in
    `/usr/lib/jvm/java-$version/jre/lib/zi`. This uses a different
    binary file format.
-   [pytz](http://cheeseshop.python.org/pypi/pytz/) (used by [Zope
    3](http://wiki.zope.org/zope3) and
    [Launchpad](https://launchpad.net/) among others) has a database
    consisting of generated Python source files for its database.

All the above rules time zone databases are based on the same source
time zone information, but need to be updated individually and in
different ways.

In a way, this is similar to the zlib security problems from a few years
back: the same problem duplicated in many packages and needing to be
fixed over and over again. Perhaps the solution is the same too: get rid
of the duplication so that in future only one package needs updating.

As a start, I put together a patch to `pytz` so that it uses the same
format binary time zone files as found in `/usr/share/zoneinfo` ([bug
71227](https://bugs.launchpad.net/bugs/71227)). This still means it has
its own time zone database, but it goes a long way towards being able to
share the system time zone database. It\'d be nice if the other
applications and libraries with their own databases could make similar
changes.

For people using Windows, there is [an update from
Microsoft](http://www.microsoft.com/australia/technet/timezone/).
Apparently you need to install one update now, and then a second update
next year --- I guess Windows doesn\'t support multiple transition rules
like Linux does. The page also lists a number of applications that will
malfunction and not know about the daylight saving shift, so I guess
that they have similar issues of some applications ignoring the system
time zone database.

---
### Comments:
#### [mathew](http://www.pobox.com/~meta/) - <time datetime="2006-12-05 02:22:06">5 Dec, 2006</time>

Another example of the same problem being \"solved\" over and over again
is locales. I created a locale definition for en-US\@ISO (ISO 8601),
only to discover that it only works for command line programs\--X
software has its own locale system.

---
#### Henri - <time datetime="2006-12-05 04:42:22">5 Dec, 2006</time>

Just out of curiosity, why doesn\'t Australia switch at the same time as
most of the rest of the world? Most South American countries that observ
it switch at the same time as Europe and Asia does. Our North American
friends always has to be special of course, but that\'s just business as
usual.

---
#### James Henstridge - <time datetime="2006-12-05 11:12:40">5 Dec, 2006</time>

Henri: Looking at the time zone definitions from the tzdata package,
there is a huge variation in the start/end dates for different countries
and the times of day they choose to have the transitions (and whether
they define the transition times in terms of standard time or wall clock
time). Some countries like Brazil don\'t even have a predictable rule
for determining the transition dates.

Europe seems to be a bit of an anomaly, with a bunch of countries
agreeing on transition times (not that that\'s a bad thing).

---
