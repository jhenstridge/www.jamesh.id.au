---
title: 'Two‐Phase Commit in Python''s DB‐API'
slug: python-tpc
date: 2008-03-04T15:19:31+09:00
tags: ['PostgreSQL', 'Python', 'Storm']
---

Marc uploaded a new revision of the [Python](http://www.python.org/)
[DB-API 2.0 Specification](http://www.python.org/dev/peps/pep-0249/)
yesterday that documents the new two phase commit extension that I
helped develop on the db-sig mailing list.

My interest in this started from the desire to support two phase commit
in [Storm](http://storm.canonical.com/) -- without that feature there
are far fewer occasions where its ability to talk to multiple databases
can be put to use. As I was doing some work on
[psycopg2](http://www.initd.org/tracker/psycopg/) for
[Launchpad](https://launchpad.net/), I initially put together a
[PostgreSQL](http://www.postgresql.org/) specific patch, which was
(rightly) rejected by Federico.

He suggested that it would be better to try and standardise on an API on
the db-sig list, so that\'s what I did. I looked over the API exposed by
other database adapters that supported 2PC, and the 2PC APIs of the
major free databases that did not have support in their Python adapters
([MySQL](http://www.mysql.com/) and PostgreSQL). The resulting API is a
bit more complicated than my original PostgreSQL-only but has the
advantage of being implementable on other databases such as MySQL.

Below is a simple example of using the API directly (missing some of the
error handling):

    # begin transactions for each database connection
    conn1.tpc_begin(conn1.xid(42, 'transaction ID', 'connection 1'))
    conn2.tpc_begin(conn2.xid(42, 'transaction ID', 'connection 2'))
    # Do stuff with both connections
    ...
    try:
        conn1.tpc_prepare()
        conn2.tpc_prepare()
    except DatabaseError:
        conn1.tpc_rollback()
        conn2.tpc_rollback()
    else:
        conn1.tpc_commit()
        conn2.tpc_commit()

Or alternatively, if you\'ve got one connection supporting 2PC and the
other only supporting one-phase commit, it could be structured as
follows:

    # begin transactions for each database connection
    conn1.tpc_begin(conn1.xid(42, 'transaction ID', 'connection 1'))
    # Do stuff with both connections
    ...
    try:
        conn1.tpc_prepare()
        conn2.commit()
    except DatabaseError:
        conn1.tpc_rollback()
        conn2.rollback()
    else:
        conn1.tpc_commit()

While it is possible to use the 2PC API directly, it is expected that
most applications will rely on a transaction manager to coordinate
global transactions, such as [Zope\'s](http://www.zope.org/)
[transaction](http://pypi.python.org/pypi/transaction) module.

The hope is that by offering a consistent API, Python application
frameworks will be more likely to bother supporting this feature of
databases. Hopefully you\'ll be able to use the API with PostgreSQL and
Storm soon.
