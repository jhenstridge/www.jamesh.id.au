---
title: 'Recovering a Branch From a Bazaar Repository'
slug: recovering-a-branch-from-a-bazaar-repository
date: 2006-12-19T05:42:10+09:00
tags: ['Bazaar', 'Python']
---

In my [previous entry](re-pushing-a-bzr-branch-with-rsync.md), I
mentioned that Andrew was actually publishing the contents of all his
[Bazaar](http://bazaar-vcs.org/) branches with his rsync script, even
though he was only advertising a single branch. Yesterday I had a need
to actually do this, so I thought I\'d detail how to do it.

As a refresher, a Bazaar repository stores the revision graph for the
ancestry of all the branches stored inside it. A branch is essentially
just a pointer to the head revision of a particular line of development.
So if the branch has been deleted but the data is still in the
repository, recovering it is a simple matter of discovering the
identifier for the head revision.

**Finding the head revision**

Revisions in a Bazaar repository have string identifiers. While the
identifiers can be almost arbitrary strings (there are some restrictions
on the characters they can contain), the ones Bazaar creates when you
commit are of the form \"`$email-$date-$random`\". So if we know the
person who committed the head revision and the date it was committed, we
can narrow down the possibilities.

For these sort of low level operations, it is easiest to use the Python
`bzrlib` interface (this is the guts of Bazaar). Lets say that we want
to recover a head revision committed by `foo@example.com` on 2006-12-01.
We can get all the matching revision IDs like so:

    >>> from bzrlib.repository import Repository
    >>> repo = Repository.open('repository-directory')
    >>> possible_ids = [x for x in repo.all_revision_ids()
    ...                 if x.startswith('foo@example.com-20061201')]

Now if you\'re working on multiple branches in parallel, it is likely
that the matching revisions come from different lines of development. To
help work out which revision ID we want, we can look at the
`branch-nick` revision property of each revision, which is recorded in
each commit. If the nickname hadn\'t been set explicitly for the branch
we\'re after, it will take the base directory name of the branch as a
default. We can easily loop through each of the revisions and print a
the nicknames:

    >>> for rev_id in sorted(possible_ids):
    ...     rev = repo.get_revision(rev_id)
    ...     print rev_id
    ...     print rev.properties['branch-nick']

We can then take the last revision ID that has the nickname we are
after. Since lexical sorting of these revision IDs will have sorted them
in date order, it should be the last revision. We can check the log
message on this revision to make sure:

    >>> rev = repo.get_revision('head-revision-id')
    >>> print rev.message

If it doesn\'t look like the right revision, you can try some other
dates (the dates in the revision identifiers are in UTC, so it might
have recorded a different date to the one you remembered). If it is the
right revision, we can proceed onto recovering the branch.

**Recovering the branch**

Once we know the revision identifier, recovering the branch is easy.
First we create a new empty branch inside the repository:

    $ cd repositorydir
    $ bzr init branchdir

We can now use the pull command with a specific revision identifier to
recover the branch:

    $ cd branchdir
    $ bzr pull -r revid:head-revision-id .

It may look a bit weird that we are pulling from a branch that contains
no revisions into itself, but since the repository for this empty branch
contains the given revision it does the right thing. And since
`bzr pull` canonicalises the branch\'s history, the new branch should
have the same linear revision history as the original branch.

**Recovering the branch from someone else\'s repository**

The above method assumes that you can create a branch in the repository.
But what if the repository belongs to someone else, and you only have
read-only access to the repository? You might want to do this if you are
trying to recover one of the branches from Andrew\'s Java GNOME
repository `:)`

The easy way is to copy all the revisions from the read-only repository
into one you control. First we\'ll create a new repository:

    $ bzr init-repo repodir

Then we can use the `Repository.fetch()` bzrlib routine to copy the
revisions:

    >>> from bzrlib.repository import Repository
    >>> remote_repo = Repository.open('remote-repo-url')
    >>> local_repo = Repository.open('repodir')
    >>> local_repo.fetch(remote_repo)

When that command completes, you\'ll have a local copy of all the
revisions and can proceed as described above.

---
### Comments:
#### John Meinel - <time datetime="2006-12-19 13:27:53">2 Dec, 2006</time>

There is a \'heads\' plugin that lets you do a lot of this:
<https://launchpad.net/products/heads>

Basically, it is just designed to show you what unmerged tips are in
your repository.

Also, an easier way to get someone else\'s revision into your repository
is to do:

bzr init my-copy (this can be in a repo, but doesn\'t have to be)

cd my-copy\
bzr pull -r revid: <http://their/branch>

\"their/branch\" needs to be in the repository. But I don\'t think it
actually needs to be in the history of the branch. It just needs to be
searchable from there.\

---
