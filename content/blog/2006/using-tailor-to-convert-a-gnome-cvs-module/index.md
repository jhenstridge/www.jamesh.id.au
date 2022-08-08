---
title: 'Using Tailor to Convert a Gnome CVS Module'
slug: using-tailor-to-convert-a-gnome-cvs-module
date: 2006-02-20T09:53:45+08:00
tags: ['Bazaar', 'Gnome', 'JHBuild']
---

In my [previous post](../revision-control-migration-and-history-corruption.md),
I mentioned using [Tailor](http://www.darcs.net/DarcsWiki/Tailor) to
import jhbuild into a Bazaar-NG branch. In case anyone else is
interested in doing the same, here are the steps I used:

**1. Install the tools**

First create a working directory to perform the import, and set up
tailor. I currently use the nightly snapshots of bzr, which did not work
with Tailor, so I also grabbed bzr-0.7:

    $ wget http://darcs.arstecnica.it/tailor-0.9.20.tar.gz
    $ wget http://www.bazaar-ng.org/pkg/bzr-0.7.tar.gz
    $ tar xzf tailor-0.9.20.tar.gz
    $ tar xzf bzr-0.7.tar.gz
    $ ln -s ../bzr-0.7/bzrlib tailor-0.9.20/bzrlib

**2. Prepare a local CVS Repository to import from**

The import will run a lot faster with a local CVS repository. If you
have a shell account on `window.gnome.org`, this is trivial to set up:

    $ mkdir cvsroot
    $ cvs -d `pwd`/cvsroot init
    $ rsync -azP window.gnome.org:/cvs/gnome/jhbuild/ cvsroot/jhbuild/

**3. Check for history inconsistency**

As I discovered, Tailor will bomb if time goes backwards at some point
in your CVS history, and will probably bomb out part way through. The
quick fix for this is to directly edit the RCS `,v` files to correct the
dates. Since you are working with a copy of the repository, there isn\'t
any danger of screwing things up.

I wrote a small program to check an RCS file for such discontinuities:

> [`backward-time.py`](backward-time.py)

When editing the dates in the RCS files, make sure that you change the
dates in the different files in a consistent way. You want to make sure
that revisions in different files that are part of the same changeset
still have the same date after the edits.

**4. Create a Tailor config file**

Here is the Tailor config file I used to import jhbuild:

    #!
    """
    [DEFAULT]
    verbose = True
    projects = jhbuild
    encoding = utf-8

    [jhbuild]
    target = bzr:target
    start-revision = INITIAL
    root-directory = basedir/jhbuild.cvs
    state-file = tailor.state
    source = cvs:source
    subdir = .
    before-commit = remap_author
    patch-name-format =

    [bzr:target]
    encoding = utf-8

    [cvs:source]
    module = jhbuild
    repository = basedir/cvsroot
    encoding = utf-8
    """

    def remap_author(context, changeset):
        if '@' not in changeset.author:
            changeset.author = '%s <%s@cvs.gnome.org>' % (changeset.author,
                                                          changeset.author)
        return True

The `remap_author` function at the bottom maps the CVS user names to
something closer to what bzr normally uses.

**5. Perform the conversion**

Now it is possible to run the conversion:

    $ python tailor-0.9.20/tailor -vv --configfile jhbuild.tailor

When the conversion is complete, you should be left with a bzr branch
containing the history of the HEAD branch from CVS. Now is a good time
to check that the converted bzr looks sane.

**6. Use the new branch**

Rather than using the converted branch directly, it is a good idea to
branch off it and do the development there:

    $ bzr branch jhbuild.cvs jhbuild.dev

The advantage of doing this is that you have the option of rsyncing in
new changes to the CVS repository and running tailor again to
incrementally import them. You can then merge those changes to your
development branch.

---
### Comments:
####  - <time datetime="2006-02-21 07:41:11">21 Feb, 2006</time>

I have some vague memories that tailor wasn\'t able to deal with CVS
branches. Has that been fixed?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-02-21 11:10:43">21 Feb, 2006</time>

From what I can tell, it has no automatic support for branches. If you
wanted to convert a branch as well as the mainline, it would be
necessary to do something like:

1\. convert mainline

2\. figure out where the branchpoint is.

3\. take a copy of the converted mainline, and uncommit up to the branch
point.

4\. create a new tailor config to convert the branch, telling it to
start at the first revision on that branch.

Pretty ugly, but should work. As I said in my previous post: I was only
interested in converting the mainline, so that\'s all I\'ve described.

---
