---
title: 'Psycopg2 2.0.7 Released'
slug: psycopg2
date: 2008-04-15T14:55:50+08:00
tags: ['PostgreSQL', 'Python']
---

Yesterday Federico [released version 2.0.7 of
psycopg2](http://lists.initd.org/pipermail/psycopg/2008-April/006013.html)
(a [Python](http://www.python.org/) database adapter for
[PostgreSQL](http://www.postgresql.org/)).  I made a fair number of the
changes in this release to make it more usable for some of
[Canonical](http://www.canonical.com/)\'s applications.  The new release
should work with the development version of Storm, and shouldn\'t be too
difficult to get everything working with other frameworks.

Some of the improvements include:

-   Better selection of exceptions based on the
    [SQLSTATE](http://www.postgresql.org/docs/current/static/errcodes-appendix.html)
    result field.  This causes a number of errors that were reported as
    ProgrammingError to use a more appropriate exception (e.g.
    DataError, OperationalError, InternalError).  This was the change
    that broke Storm\'s test suite as it was checking for
    ProgrammingError on some queries that were clearly not programming
    errors.
-   Proper error reporting for commit() and rollback(). These methods
    now use the same error reporting code paths as execute(), so an
    integrity error on commit() will now raise IntegrityError rather
    than OperationalError.
-   The compile-time switch that controls whether the display\_size
    member of Cursor.description is calculated is now turned off by
    default.  The code was quite expensive and the field is of limited
    use (and not provided by a number of other database adapters).
-   New QueryCanceledError and TransactionRollbackError exceptions.  The
    first is useful for handling queries that are canceled by
    [statement\_timeout](http://www.postgresql.org/docs/8.3/static/runtime-config-client.html#GUC-STATEMENT-TIMEOUT). 
    The second provides a convenient way to catch serialisation failures
    and deadlocks: errors that indicate the transaction should be
    retried.
-   Fixes for a few memory leaks and GIL misuses. One of the leaks was
    in the notice processing code that could be particularly problematic
    for long-running daemon processes.
-   Better test coverage and a driver script to run the entire test
    suite in one go.  The tests should all pass too, provided your
    database cluster uses unicode (there was a report just before the
    release of one test failing for a LATIN1 cluster).

If you\'re using previous versions of psycopg2, I\'d highly recommend
upgrading to this release.

Future work will probably involve support for the DB-API two phase
commit extension, but I don\'t know when I\'ll have time to get to that.

---
### Comments:
#### Glenn Williams - <time datetime="2008-04-15 23:59:42">2 Apr, 2008</time>

Thanks James,

I have used psycopg2 for years, and appreciate everyone\'s work.
Especially yours and Federico\'s.

Glenn

---
#### Nick - <time datetime="2008-04-18 08:40:45">5 Apr, 2008</time>

I\'m another happy user saying a big \"thanks!\". Keep up the good work
:)

---
