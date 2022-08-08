---
title: 'Using Storm with Django'
slug: using-storm-with-django
date: 2008-08-01T17:23:16+08:00
tags: ['Django', 'Python', 'Storm', 'Zope']
---

I\'ve been playing around with [Django](http://www.djangoproject.com/) a
bit for work recently, which has been interesting to see what choices
they\'ve made differently to [Zope 3](http://wiki.zope.org/zope3/). 
There were a few things that surprised me:

-   The ORM and database layer defaults to autocommit mode rather than
    using transactions.  This seems like an odd choice given that all
    the major free databases support transactions these days.  While
    autocommit might work fine when a web application is under light
    use, it is a recipe for problems at higher loads.  By using
    transactions that last for the duration of the request, the testing
    you do is more likely to help with the high load situations.
-   While there is a middleware class to enable request-duration
    transactions, it only covers the database connection.  There is no
    global transaction manager to coordinate multiple DB connections or
    other resources.
-   The ORM appears to only support a single connection for a request. 
    While this is the most common case and should be easy to code with,
    allowing an application to expand past this limit seems prudent.
-   The tutorial promotes schema generation from Python models, which
    I feel is the wrong choice for any application that is likely to
    evolve over time (i.e. pretty much every application).  I\'ve
    [written about this previously](orm-schema-generation.md) and
    believe that migration based schema management is a more workable
    solution.
-   It poorly [reinvents thread local storage](tls-python.md) in a few
    places.  This isn\'t too surprising for things that existed prior
    to Python 2.4, and probably isn\'t a problem for its default mode
    of operation.

Other than these things I\'ve noticed so far, it looks like a nice
framework.

**Integrating Storm**

I\'ve been doing a bit of work to make it easy to use
[Storm](http://storm.canonical.com/) with Django.  I posted some initial
details [on the mailing
list](http://thread.gmane.org/gmane.comp.python.storm/673).  The initial
code has been [published on
Launchpad](https://code.launchpad.net/~jamesh/storm/django-support) but
is not yet ready to merge. Some of the main details include:

-   A middleware class that integrates the Zope global transaction
    manager (which requires just the zope.interface and transaction
    packages).  There doesn\'t appear to be any equivalent functionality
    in Django, and this made it possible to reuse the existing
    integration code (an approach that has been taken to use Storm with
    [Pylons](http://pylonshq.com/)).  It will also make it easier to
    take advantage of other future improvements (e.g. only committing
    stores that are used in a transaction, two phase commit).
-   Stores can be configured through the application\'s Django settings
    file, and are managed as long lived per-thread connections.
-   A simple get\_store(name) function is provided for accessing
    per-thread stores within view code.

What this doesn\'t do yet is provide much integration with existing
Django functionality (e.g. django.contrib.admin).  I plan to try and get
some of these bits working in the near future.

---
### Comments:
#### Raf - <time datetime="2008-08-01 23:26:38">1 Aug, 2008</time>

Storm looked alright until I found out that you need to type in the SQL
manually even though you have a set of nice models to work with already
defined :/

---
#### James Henstridge - <time datetime="2008-08-02 19:21:48">2 Aug, 2008</time>

Raf: I\'d agree that the current state of schema management in Storm is
not that great (i.e. it is non-existent). However, I believe that schema
generation as found in Django is not the right solution: a migration
framework is what is needed for long lived applications (e.g. like Ruby
on Rails).

---
#### Torsten Bronger - <time datetime="2008-08-03 05:42:53">3 Aug, 2008</time>

Maybe Django Evolution will improve the situation.

---
#### James Henstridge - <time datetime="2008-08-05 19:49:47">5 Aug, 2008</time>

Django Evolution looks interesting, but seems to keep some of the
problems of schema generation: if you do two deployments of an
application at different times with different versions, running
\"syncdb\" at that time, then upgrade both deployments to the latest
version and evolve the schemas are you sure that the two schemas are
identical?

If you set up both deployments using a single base schema with
migrations run on top in the same order, then the answer will be yes. If
they were deployed with different base schemas and a different set of
migrations, then it depends on how good Django Evolution is :)

---
#### [Eduardo Willians](http://pycappuccino.blogspot.com/) - <time datetime="2008-08-16 23:40:30">16 Aug, 2008</time>

Awesome! Congrats, as Django is becoming the de facto option for web
development, integrating Storm with Django will help both projects,
especially because both are excellent.

---
#### [James Henstridge &raquo; Storm 0.13](storm-013.md) - <time datetime="2008-08-29 16:21:35">29 Aug, 2008</time>

\[\...\] The minimum dependencies of the storm.zope.zstorm module have
been reduced to just the zope.interface and transaction modules.  This
makes it easier to use the per-thread store management code and global
transaction management outside of Zope apps (e.g. for integrating with
Django). \[\...\]

---
