---
title: 'Python time.timezone / time.altzone edge case'
slug: python-timetimezone-timealtzone-edge-case
date: 2006-12-31T13:22:42+09:00
tags: ['Bazaar', 'Python']
---

While browsing the log of one of my [Bazaar](http://bazaar-vcs.org/)
branches, I noticed that the commit messages were being recorded as
occurring in the +0800 time zone even though WA switched over to
daylight savings.

Bazaar stores commit dates as a standard UNIX seconds since epoch value
and a time zone offset in seconds. So the problem was with the way that
time zone offset was recorded. The code in `bzrlib` that calculates the
offset looks like this:

    def local_time_offset(t=None):
        """Return offset of local zone from GMT, either at present or at time t."""
        # python2.3 localtime() can't take None
        if t is None:
            t = time.time()

        if time.localtime(t).tm_isdst and time.daylight:
            return -time.altzone
        else:
            return -time.timezone

Now the `tm_isdst` flag was definitely being set on the time value, so
it must have something to do with one of the `time` module constants
being used in the function. Looking at the values, I was surprised:

    >>> time.timezone
    -28800
    >>> time.altzone
    -28800
    >>> time.daylight
    0

So the time module thinks that I don\'t have daylight saving, and the
alternative time zone has the same offset as the main time zone (+0800).
This seems a bit weird since `time.localtime()` says that the time value
is in daylight saving time.

Looking at the Python source code, the way these variables are
calculated on Linux systems goes something like this:

1.  Get the current time as seconds since the epoch.
2.  Round this to the nearest year (365 days plus 6 hours, to be exact).
3.  Pass this value to `localtime()`, and record the `tm_gmtoff` value
    from the resulting `struct tm`.
4.  Add half a year to the rounded seconds since epoch, and pass that to
    `localtime()`, recording the `tm_gmtoff` value.
5.  The earlier of the two offsets is stored as `time.timezone` and the
    later as `time.altzone`. If these two offsets differ, then
    `time.daylight` is set to `True`.

Unfortunately, the UTC offset used in Perth at the beginning of 2006 and
the middle of 2006 was +0800, so +0800 gets recorded as the daylight
saving time zone too. In the new year, the problem should correct
itself, but this highlights the problem of relying on these constants.

Unfortunately, the `time.localtime()` function from the Python standard
library does not expose `tm_gmtoff`, so there isn\'t an easy way to
correctly calculate this value.

With [the patch I
did](https://code.launchpad.net/people/jamesh/+branch/pytz/tzfile) for
[pytz](http://cheeseshop.python.org/pypi/pytz) to parse binary time zone
files, it would be possible to use the `/etc/localtime` zone file with
the Python `datetime` module without much trouble, so that\'s one
option. It would be nice if the Python standard library provided an easy
way to get this information though.

---
### Comments:
#### [mathew](http://www.pobox.com/~meta/) - <time datetime="2007-01-01 04:19:15">1 Jan, 2007</time>

\"Bazaar stores commit dates as a standard UNIX seconds since epoch
value plus a time zone offset in seconds.\"

Well, that\'s useful to know. Specifically, I now know never to go near
bzr, as it\'s obviously designed by complete idiots.

The only sensible way to record timestamps is to store them in UTC, and
make converting to and from display format and display time zone be a
client function.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-01-01 10:45:44">1 Jan, 2007</time>

Matthew: I guess I was a bit ambiguous in the post above. Bazaar stores
a \"seconds since epoch field\" plus a \"time zone offset field\". If
you are using bzrlib, these are revision.timestamp and revision.timezone
respectively.

It was recording the UTC time correctly for my commits, but it was
determining an incorrect time zone offset, and that problem seems to be
caused by easily misused standard library features.

---
