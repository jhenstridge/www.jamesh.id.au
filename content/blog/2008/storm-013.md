---
title: 'Storm 0.13'
slug: storm-013
date: 2008-08-29T16:21:20+08:00
tags: ['Launchpad', 'Python', 'Storm', 'Zope']
---

Yesterday, Thomas rolled the 0.13 release of
[Storm](http://storm.canonical.com/), which can be [downloaded from
Launchpad](https://launchpad.net/storm/trunk/0.13). Storm is the object
relational mapper for [Python](http://www.python.org/) used by
[Launchpad](https://launchpad.net/) and
[Landscape](http://www.canonical.com/projects/landscape), so it is
capable of supporting quite large scale applications. It is seven
months since the last release, so there is a lot of improvements. Here
are a few simple statistics:

|                        |  0.12|  0.13|  Change|
| -----------------------|------|------|--------|
| Tarball size (KB)      |   117|   155|      38|
| Mainline revisions     |   213|   262|      49|
| Revisions in ancestry  |   552|   875|     323|

So it is a fairly significant update by any of these metrics. Among the
new features are:

-   Infrastructure for tracing the SQL statements issued by Storm.
    Sample tracer implementations are provided to implement bounded
    statement run times and for logging statements (both features used
    for QA of Launchpad).
-   A validation framework. The property constructors take a validator
    keyword argument, which should be a function taking arguments
    (object, attr\_name, value) and return the value to set. If the
    function raises an exception, it can prevent a value from being
    set. By returning something different to its third argument it can
    transform values.
-   The `find()` and `ResultSet` API has been extended to make it
    possible to generate queries that use `GROUP BY` and `HAVING`. The
    primary use case for result sets that contain an object plus some
    aggregates associated with that object.
-   Some core parts of Storm have been accelerated through a C
    extension. This code is turned off by default, but can be enabled
    by defining the `STORM_CEXTENSIONS` environment variable to 1.
    While it is disabled by default, it is pretty stable. Barring any
    serious problems reported over the next release cycle, I\'d expect
    it to be enabled by default for the next release.
-   The minimum dependencies of the `storm.zope.zstorm` module have
    been reduced to just the `zope.interface` and `transaction`
    modules.  This makes it easier to use the per-thread store
    management code and global transaction management outside of Zope
    apps (e.g. for [integrating with Django](using-storm-with-django.md)).

It doesn\'t include my Django integration code though, since that isn\'t
fully baked. I\'ll post some more about that later.
