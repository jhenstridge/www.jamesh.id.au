---
title: 'Bazaar (continued)'
slug: bazaar-continued
date: 2005-05-13T10:37:22+08:00
draft: false
tags: ['Bazaar']
---

I got a few responses to the comparison between CVS, Subversion and
Bazaar command line interfaces I posted earlier from
[Elijah](http://www.gnome.org/~newren/blog/2005/05/12),
[Mikael](http://micke.hallendal.net/archives/2005/05/version_control.html)
and [David](http://www.advogato.org/person/bolsh/diary.html?start=114).
As I stated in that post, I was looking at areas where the three systems
could be compared. Of course, most people would choose Arch because of
the things it can do with it that Subversion and CVS can\'t. Below I\'ll
discuss two of those things: disconnected development and distributed
development. I\'ll follow on from the examples in the previous post.

**Disconnected Development**

Disconnected development allows you to continue working on some code
while not having access to the main repository. I hinted at how to do
this in the previous post, but left out most of the details. The basic
steps are:

1.  Create an archive on your machine
2.  Branch the module you want to work on into your local archive.
3.  Perform your development as normal
4.  When you connect again, switch back to the mainline, merge your
    local branch and commit the changes.

To create the local archive, you follow the same procedure as for
creating the original archive. Something like this:

    mkdir ~/archives
    baz make-archive --signed joe@example.com ~/archives/joe@example.com

This creates an archive named `joe@example.com` (archive names are
required to be an email address, optionally followed by some extra info)
stored in the user\'s home directory.

Now we can create a branch in the local archive. From a working copy of
the mainline branch, run the following command:

    baz branch joe@example.com/modulename--devel--0

It was necessary to specify an archive name in this call to
`baz branch`, because the branch was being created in a different
archive to the one the working copy was pointing at. This leaves the
working copy pointing at the new branch, so you can start working on it
immediately.

You can commit as many revisions as you want, and compare to other
revisions on the branch.

When you have access to the main repository again, it is trivial to
merge your changes back into the mainline:

    baz switch arch@example.org/modulename--devel--0
    baz merge joe@example.com/modulename--devel--0
    fix conflicts, if any exist, and mark them resolved
    baz commit -s 'merge changes from joe@example.com/modulename--devel--0'

You can then ignore the branch in the `joe@example.com` archive, or
continue to use it. If you want to continue working on the branch in
that module, it is a simple matter to merge from the `arch@example.org`
archive first to pick up the changes made while you were disconnected.

**Distributed Development**

In a distributed development environment, there is no main branch.
Instead, each developer maintains their own branch, and pulls changes
from other developers\' archives. A few things fall out from this model:

-   To start working on a distributed project, you need to branch off
    from another developer\'s archive. This can be achieved using the
    same instructions as found in the \"disconnected development\"
    section above.
-   In order for other developers to pull changes from your archive,
    they will need to be able to access it. This isn\'t possible if it
    only exists in your home directory.
-   If you never merge from a particular developer, you don\'t even need
    to know they exist.
-   Conversely, you don\'t need to ask for permission to work on a
    module (however, if you want your changes to appear in the other
    developers\' archives, you\'ll need to ask them to merge from you).

So assuming you\'ve branched off an existing developer\'s branch of a
module, and want other developers to merge your changes. Assuming they
can\'t access your local computer, it will be necessary to create a
mirror of the archive. To make the archive most widely available, you
should mirror it to a directory that is published by a web server. The
following command will create a mirror of the local archive:

    baz make-archive --signed --listing --mirror joe@example.com \
            sftp://hostname/home/joe/public_html/joe@example.com

Once the archive is created, you can mirror all the changes in the local
archive to the remote one using the following command:

    baz archive-mirror joe@example.com

If you always have access to the mirror host, it is possible to set up a
hook script that mirrors after every commit. However, if you often make
changes while offline you might decide to mirror manually.

Now that the archive has been mirrored, other developers can merge your
changes into their working copy using the following command:

    baz merge http://hostname/~joe/joe@example.com/modulename--devel--0

(after they\'ve used your archive once, they can use the short name for
the archive, and it will use the same location as last time).

**Conclusion**

While Arch allows full distributed development, most projects don\'t use
it in a fully distributed manner. Often there will be a central archive
that is the \"official\" one, which tarball releases are made from. The
exact policies can differ from project to project. Some possible
policies are:

-   A core of developers have commit access to an \"official\" archive,
    which releases are made from. Developers generally commit directly
    to this archive (this is the default CVS/Subversion model). External
    developers follow the distributed development model, and get core
    developers to merge their changes.
-   As above, but the core developers usually develop their changes on
    separate branches (usually in their own archives), and only merge
    them when ready. This is how some projects currently use CVS, but
    has the benefit of allowing disconnected development.
-   Control of the official archive is managed by
    [arch-pqm](http://web.verbum.org/arch-pqm/). Authorized developers
    can send merge requests to PQM (using PGP for authentication). When
    a merge request is received, the branch is merged into the mainline.
    If there are no conflicts and the test suite runs successfully, the
    changes are committed.

I\'m not sure which model would work best for
[Gnome](http://www.gnome.org/). At least initially, one of the first two
models would probably be a good choice. If you have good test coverage,
PQM can help ensure that the mainline stays buildable, and changes
don\'t destabilise things.

As has been mentioned elsewhere, regularly updated mirrors of various
CVS repositories are being set up at
[`arch.ubuntu.com`](http://arch.ubuntu.com/). You can find out whether a
mirror has been created for a module by looking it up on
[Launchpad](https://launchpad.ubuntu.com/products/). If a branch exists,
you can check it out or branch it by prepending
\"`http://arch.ubuntu.com/`\" to the full branch name (e.g.
`http://arch.ubuntu.com/‌imendio@projects.ubuntu.com/‌gossip--MAIN--0`).
