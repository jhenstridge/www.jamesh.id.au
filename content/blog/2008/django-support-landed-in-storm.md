---
title: 'Django support landed in Storm'
slug: django-support-landed-in-storm
date: 2008-09-19T14:23:51+08:00
tags: ['Django', 'Python', 'Storm']
---

Since [my last article](using-storm-with-django.md) on integrating
[Storm](http://storm.canonical.com/) with
[Django](http://www.djangoproject.com/), I\'ve merged my changes to
Storm\'s trunk. This missed the 0.13 release, so you\'ll need to use
Bazaar to get the latest trunk or wait for 0.14.

The focus since the last post was to get Storm to cooperate with
Django\'s built in ORM. One of the reasons people use Django is the
existing components that can be used to build a site. This ranges from
the included user management and administration code to full [web shop
implementations](http://www.satchmoproject.com/). So even if you plan
to use Storm for your Django application, your application will most
likely use Django\'s ORM for some things.

When I last posted about this code, it was possible to use both ORMs in
a single app, but they would use separate database connections. This
had a number of disadvantages:

-   The two connections would be running separate transactions in
    parallel, so changes made by one connection would not be visible to
    the other connection until after the transaction was complete. This
    is a problem when updating records in one table that reference rows
    that are being updated on the other connection.
-   When you have more than one connection, you introduce a new failure
    mode where one transaction may successfully commit but the other
    fail, leaving you with only half the changes being recorded. This
    can be fixed by using two phase commit, but that is not supported by
    either Django or Storm at this point in time.

So it is desirable to have the two ORMs sharing a single connection.
The way I\'ve implemented this is as a Django database engine backend
that uses the connection for a particular named per-thread store and
passes transaction commit or rollback requests through to the global
transaction manager. Configuration is as simple as:

    DATABASE_ENGINE = 'storm.django.backend'
    DATABASE_NAME = 'store-name'
    STORM_STORES = {'store-name': 'database-uri'}

This will work for PostgreSQL or MySQL connections: Django requires some
additional set up for SQLite connections that Storm doesn\'t do.

Once this is configured, things mostly just work. As Django and Storm
both maintain caches of data retrieved from the database though,
accessing the same table with both ORMs could give unpredictable
results. My code doesn\'t attempt to solve this problem so it is
probably best to access tables with only one ORM or the other.

I suppose the next step here would be to implement something similar to
Storm\'s `Reference` class to represent links between objects managed by
Storm and objects managed by Django and vice versa.
