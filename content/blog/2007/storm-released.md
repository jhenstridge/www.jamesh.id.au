---
title: 'Storm Released'
slug: storm-released
date: 2007-07-15T22:24:17+08:00
tags: ['Launchpad', 'Python', 'Storm']
---

This week at the [EuroPython](http://www.europython.org/) conference,
Gustavo Niemeyer announced the release of
[Storm](http://storm.canonical.com/) and gave a tutorial on using it.

Storm is a new [object relational
mapper](http://en.wikipedia.org/wiki/Object-relational_mapping) for
Python that was developed for use in some Canonical projects, and we\'ve
been working on moving [Launchpad](https://launchpad.net/) over to it.
I\'ll discuss a few of the nice features of the package:

**Loose Binding Between Database Connections and Classes**

Storm has a much looser binding between database connections and the
classes used to represent records in particular tables. The standard way
of querying the database uses a store object:

    for obj in store.find(SomeClass, conditions):
        # do something with obj (which will be a SomeClass instance)

Some things to note about this syntax:

-   The class used to represent rows in the table is passed to find(),
    so it is possible to have multiple classes representing a single
    table. This can be useful with large tables where you are only
    interested in a few columns in some cases.
-   The class used to represent the table is not bound to a particular
    connection. So instances of it can come from different stores.

**Lockstep Iteration**

As well as iterating over a single table, a Storm result set can iterate
over multiple tables together. For instance, if we have a table
representing people and a table representing email addresses (where each
person can have multiple email addresses), it is possible to iterate
over them in lockstep:

    for person, email in store.find((Person, Email), Person.id == Email.person):
        print person.name, email.address

**Automatic Flushing Before Queries**

One of the gotchas when using SQLObject was the way it locally cached
updates to tables. This is a great way to reduce the number of updates
sent to the database, but could result in unexpected results when
performing subsequent SELECT queries. It was up to the programmer to
remember to flush changes before doing a query.

With Storm, the store will flush pending changes automatically before
performing the query.

**Easy To Execute Raw SQL**

An ORM can really help when developing a database driven application,
but sometimes plain old SQL is a better fit. Storm makes it easy to
execute raw SQL against a particular store with the store.execute()
method. This method returns an object that you can iterate over to get
the tuples from the result set. It also makes sure that any local
changes have been flushed before executing the query.

**Nice Clean Code**

After working with SQLObject for a while, Storm has been a breath of
fresh air. The internals are clean and nicely laid out, which makes
hacking on it very easy. It was developed using [test-driven
development](http://en.wikipedia.org/wiki/Test-driven_development)
methodology, so there is an extensive test suite that makes it easy to
validate changes.
