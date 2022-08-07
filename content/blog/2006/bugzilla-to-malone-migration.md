---
title: 'Bugzilla to Malone Migration'
slug: bugzilla-to-malone-migration
date: 2006-01-16T13:01:20+08:00
draft: false
tags: ['Launchpad', 'Ubuntu']
---

The Bugzilla migration on Friday went quite well, so we\'ve now got all
the old Ubuntu bug reports in [Launchpad](https://launchpad.net/).
Before the migration, we were up to bug \#6760. Now that the migration
is complete, there are more than 28000 bugs in the system. Here are some
quick points to help with the transition:

-   All `bugzilla.ubuntu.com` accounts were migrated to Launchpad
    accounts with a few caveats:
    1.  If you already had a Launchpad account with your bugzilla email
        address associated with it, then the existing Launchpad account
        was used.
    2.  No passwords were migrated from Bugzilla, due to differences in
        the method of storing them. You can set the password on the
        account at <https://launchpad.net/+forgottenpassword>.
    3.  If you had a Launchpad account but used a different email to the
        one on your Bugzilla account, then you now have two Launchpad
        accounts. You can merge the two accounts at
        <https://launchpad.net/people/+requestmerge>.

-   If you have a `bugzilla.ubuntu.com` bug number, you can find the
    corresponding Launchpad bug number with the following URL:\

    > `http://launchpad.net/malone/bugtrackers/ubuntu-bugzilla/$BUGZILLA_ID`

    This will redirect to the Launchpad bug watching that bugzilla bug.
    This URL can easily be used to make a Firefox keyword bookmark.

-   You can file bugs on Ubuntu at
    <https://launchpad.net/distros/ubuntu/+filebug>. Note that the form
    expects a *source* package name rather than a *binary* package name.
    If you only have a binary package name, you can use the following
    command to find the source package name:\

    > [apt-cache show \$packagename \| grep \^Source:]{.kbd}

    We\'ll make it easier to enter bugs when you only know the binary
    package name in the future.

-   The Launchpad data model for bugs differs from Bugzilla in that a
    single bug can be targetted at multiple packages or products
    (internally, we call these *bug tasks*). To change information about
    a bug task (source package name, assignee, status, priority,
    severity, etc), you must first click on the bug target in the \"fix
    requested in\" table at the top of the bug page.

There are still a few issues that need to be ironed out. The mailing
lists subscribed to most Ubuntu bugs are not yet properly configured to
accept mail from Launchpad, so result in \"held for moderation\"
messages. These issues should get fixed shortly.

---
### Comments:
#### [AdamW](http://www.happyassassin.net/) - <time datetime="2006-01-17 07:47:07">2 Jan, 2006</time>

\"Now that the migration is complete, there are more than 28000 bugs in
the system.\"

Awesome! That means Ubuntu is now officially buggier than Mandriva
(20,655 bugs, as of a few minutes ago). Anyone feel like having a
ludicrously misleading PR war? I\'m bored. :)

---
