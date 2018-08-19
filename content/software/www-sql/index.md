---
title: "WWW-SQL"
date: 1998-11-17T00:00:00+08:00
draft: false
---

WWW-SQL is one of the first pieces of free software I wrote, back when
I was in university.  It is a CGI script that allows simple programs
to be embedded in web pages, with access to either a
[MySQL](https://www.mysql.com/) or
[PostgreSQL](https://www.postgresql.org/) database.

<!--more-->

The provided language was based on that provided by the W3-mSQL tool
developed by [Hughes Technologies](http://Hughes.com.au/) for their
mSQL database.

I haven't touched the code base in two decades, and the implementation
is not great security wise (it wouldn't be too difficult to write a
page vulnerable to SQL injection attacks or cross-site request
forgery, for instance).  So the code is mostly of historical interest.
For new projects, I'd suggest using a well maintained framework like
[Django](https://www.djangoproject.com/).

## Current Version

The current version is 0.5.7.  It doesn't add any new features if you
don't use the new scanner.  If you have been testing it, you will find
support for while loops.  Here is the relevant section of the
Changelog:

    www-sql-0.5.7:  17-November-1998
        - Fixed a small inconsistency between the new and old scanners, so
          that the new one recognises &lt;!SQL as well as &lt;!sql.
        - Made the new scanner the default for compiles.  You can use the old
          input scanner with the --without-new-scanner argument to configure.
        - Added a sentance to the ftime function documentation to clarify that
          the offset is given in seconds.
        - Now AFFECTED_ROWS and INSERT_ID are set for failed queries (to 0 and
          -1 respectively).
        - Added the uinclude command.  It is identical to the include command,
          except that it is executed unconditionally (even if shielded by an
          if statement).  This may be more useful to some people.

You can also review the complete <a href="Changelog">Changelog</a>

## Documentation</h2>

At the moment, the only documentation is the manual distributed with
the source.  An <a href="www-sql.html">online version</a> exist on
this web site.

## The Source

The source of the last release is available from the Ibiblio software
collection:

http://www.ibiblio.org/pub/linux/apps/database/www/www-sql-0.5.7.tar.gz
