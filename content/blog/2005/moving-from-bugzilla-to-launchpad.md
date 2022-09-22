---
title: 'Moving from Bugzilla to Launchpad'
slug: moving-from-bugzilla-to-launchpad
date: 2005-11-09T07:46:25+08:00
tags: ['Launchpad', 'Ubuntu']
---

One of the things that was discussed at
[UBZ](http://wiki.ubuntu.com/UbuntuBelowZero) was moving Ubuntu\'s bug
tracking over to [Launchpad](https://launchpad.net/). The current
situation sees bugs in `main` being filed in
[bugzilla](https://bugzilla.ubuntu.com/) while bugs in `universe` go in
Launchpad. Putting all the bugs in Launchpad is an improvement, since
users only need to go to one system to file bugs.

I wrote the majority of the conversion script before the conference, but
made a few important improvements at the conference after discussions
with some of the developers. Since the bug tracking system is probably
of interest to people who weren\'t at the conf, I\'ll outline some of
the details of the conversion below:

-   We are only migrating the open bugs \-- the existing bugzilla will
    remain available to read those bugs though.

-   Any bugzilla user account associated with an open bug (asignee,
    reporter, cc, qa contact or commenter) will be imported into
    Launchpad. If you already have a Launchpad account but use a
    different email for your bugzilla account, you have the following
    options:

    1.  Add your bugzilla email to your Launchpad account.
    2.  In bugzilla, change your email to one of the addresses
        registered to your Launchpad account.
    3.  After the migration, merge the extra account into your existing
        account.

    Note that passwords are not migrated, because Launchpad uses a
    different password hashing algorithm to Bugzilla

-   All comments and attachments are imported.

-   Bugs are filed against the appropriate package under the \"Ubuntu\"
    distribution in Launchpad.

-   A bug watch is created, pointing at the original Bugzilla bug, so
    you can see any information not migrated.

-   If the bug was marked UPSTREAM and a bug tracker URL is included in
    the bugzilla URL field, then we attempt to create a bug task against
    the upstream product and link it to the remote bug. This depends on
    the upstream product existing and being linked to the package, so
    doesn\'t always succeed. This feature was implemented to keep
    [Sebastien](http://www.advogato.org/person/seb128/) happy, 68% of
    the `UPSTREAM` bugs are assigned to him.

-   Some of the bugzilla bugs are actually imported from
    [debbugs](http://bugs.debian.org/). For these bugs, a bug task will
    be filed against Debian linked to the appropriate debbugs bug.

There are a few other things that need completing on the production
Launchpad server before we can do the migration, but we should have a
test import done on [the staging server](https://staging.launchpad.net/)
tomorrow some time.

---
### Comments:
#### [Chris Samuel](http://www.csamuel.org/) - <time datetime="2005-11-27 21:01:59">27 Nov, 2005</time>

It\'s been a few weeks now - how\'s this going ?

cheers!
Chris

---
#### James Henstridge - <time datetime="2005-11-28 18:43:52">28 Nov, 2005</time>

Things have progressed a little slower than anticipated. Performing the
import on the production database depends on some other data being
imported first (the packaging history for Ubuntu warty, hoary, breezy
and dapper).

The good news is that we will be importing all the bugs now, not just
the open ones, so that bugzilla.ubuntu.com can eventually be switched
off.

---
