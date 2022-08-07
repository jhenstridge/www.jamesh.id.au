---
title: 'Repositories in Bzr'
slug: repositories-in-bzr
date: 2006-04-24T06:28:48+08:00
tags: ['Bazaar']
---

One of the new features comming up in the next release of
[bzr](http://www.bazaar-vcs.org/) is support for shared repositories.
This provides a way to reduce disk space needed to store multiple
related branches. To understand how repositories work, it helps to know
a bit about how branches are stored by bzr.

[![bzr repository diagram](bzr-repo.png)](bzr-repo.svg)

There are three concepts that make up a bzr branch:

1.  A **checkout** or working tree. This is the source files you are
    working with. It represents the state of the source code at some
    recorded revision plus any local changes you\'ve made. In the
    diagram on the right, it is represented as the red node.
2.  The **branch**, consisting of a linear sequence of revisions. This
    is represented by the blue nodes in the diagram. Note that there may
    be multiple paths from the first revision to the current revision
    due to branching and merging. The branch revision history indicates
    the path that was taken by this particular branch.
3.  The **repository**, being a store of the text of all the revisions
    in the ancestry of the branch, plus metadata about those revisions.
    This essentially stores information about every node and edge in the
    diagram.

In previous versions of bzr, this information was not clearly separated.
However with the new default branch format in bzr 0.8 they are
separated, and a particular directory need not contain all three parts,
which is what makes the space savings and performance improvements
possible.

One of the biggest space savings is achieved from sharing the repository
data between branches. If a particular branch does not contain any
repository information, bzr will recursively check the parent directory
til it finds a repository. If a collection branches share some of their
history, then the single shared repository will be significantly smaller
than the space used if each branch had its own repository data.

Another way to reduce disk usage is to create branches without
checkouts. This is useful when publishing a branch, since people pulling
or merging from that branch don\'t use the checkout files.

Finally, it is possible to create a checkout which does not contain
branch or repository data, instead containing a pointer to where that
data is located. This is quite useful when combined with a central
shared repository.

So how big is this space saving? When I converted
[JHBuild](/software/jhbuild/index.md) to bzr, the
repository data totals to 10MB, the branch data totals 100KB and a
checkout is 1.4MB.

So to publish a second branch without the use of shared repositories
means another 10MB of storage (a bit more if I include a checkout at the
published location). If I use shared repositories, the cost of the
second branch is 100KB plus an amount proportional to the size of the
changes I make on that branch. So for many projects, the cost of
publishing another branch is lost in the noise.
