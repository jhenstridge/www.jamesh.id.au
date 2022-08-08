---
title: 'Bazaar Bundles'
slug: bazaar-bundles
date: 2007-07-31T13:51:51+08:00
tags: ['Bazaar', 'Launchpad']
---

This article follows on from the series of tutorials on using
[Bazaar](http://bazaar-vcs.org/) that I have neglected for a while. This
article is about the bundle feature of Bazaar. Bundles are to Bazaar
branches what patches are to tarballs or plain source trees.

Context/unified diffs and the patch utility are arguably one of most
important inventions that enable distributed development:

-   The patch is a self contained text file, making it easy to send as
    an email attachment or attach to a bug report.
-   The size of the patch is proportional to the size of the changes
    rather than the size of the source tree. So submitting a one line
    fix to the Linux kernel is as easy as a one line fix for a small one
    person project.
-   Even if the destination source tree has moved forward since the
    patch was created, the [patch
    utility](http://www.gnu.org/software/patch/patch.html) does a decent
    job of applying the changes using heuristics to match the
    surrounding context. Human intervention is only needed if the edits
    are to the same section of code.
-   As patches are human readable text files, they are a convenient form
    to review the code changes.

Of course, patches do have their limitations:

-   The unified diff format doesn\'t convey file moves, instead showing
    the entire file content being removed and then added again. If the
    file was changed in addition to being moved, the change can easily
    be missed when reviewing the patch.
-   Changes to binary files are omitted from the patch. While we can\'t
    expect such changes to be represented in a human readable form,
    it\'d be nice for them to be represented in a way that they can be
    applied at the other end.
-   The patch doesn\'t record any intermediate steps in the creation of
    the change. This can be worked around by sending a sequence of
    patches that each build on the previous one, but this requires a
    fair bit of attentiveness on the part of the patch creator.
-   If the project in question is using some form of version control,
    the changes in the patch will likely be attributed to the person who
    applied the patch rather than the person who made the patch.

Using distributed version control solves these limitations, but simply
publishing a branch and telling someone to pull from it does not provide
all the benefits of a patch. For one, the person reviewing the changes
needs to be online to merge the branch and evaluate the changes.

Second, the contributor of the change needs somewhere to host the
branch. Even though finding a place to host the branch may not be
difficult (for example, anyone can host their branches on
[Launchpad](https://code.launchpad.net/)), uploading the branch may be
more effort than the contributor cares for (uploading a branch the size
of the Linux kernel will take a while, for instance). That branch would
need to remain available until the changes were accepted.

For Bazaar, bundles provide a solution to this problem. A bundle is
effectively a \"branch diff\", which can then be used to integrate a set
of revisions into a repository assuming it contains the revisions from
the target branch. At this point, those changes can be merged or pulled.

So how do we produce a bundle? Lets start by creating a branch of the
project we want to contribute to. For this example, we\'ll create a
branch of [Mailman](http://www.list.org/) to make our changes. As
Mailman is using Launchpad to host its branches, I can use the shorthand
implemented by the Launchpad Bazaar plugin to create my branch:

    bzr branch lp:mailman mailman.jamesh
    cd mailman.jamesh
    # make my changes here
    bzr commit

After I am happy with my changes, I can create a bundle of those
changes:

    bzr bundle > my-changes.diff

As mentioned earlier, a bundle is essentially a diff between two
branches. As I did not specify any branch in the above command, Bazaar
uses the parent branch, which in this case will be the upstream Mailman
branch. If we look at `my-changes.diff`, we will see a text file with
three general sections:

1.  A short header identifying the file as a bundle and giving the last
    commit message, author and date
2.  A unified diff made between the last common revision with the parent
    and the head of our branch (this bit is also convenient to review).
3.  Some extra book keeping data. If I\'d made multiple commits, this
    would include data needed to reconstruct the other revisions in the
    bundle.

I can now submit this bundle in the same way that I\'d submit a patch:
as an email attachment or in the bug tracker.

To merge the bundle, a developer simply needs to save the bundle to disk
and use \"`bzr merge`\" on it:

    bzr merge my-changes.diff
    bzr commit

This will have the same effect as if they merged a branch with those
changes. The \"`bzr log`\" output will show the merged revisions and
\"`bzr annotate`\" will credit the changes to the person who made them
rather than the person who merged it.

So next time you want to submit a patch to a project that uses Bazaar,
consider submitting a bundle instead.

---
### Comments:
#### [Eric Florenzano](http://www.eflorenzano.com) - <time datetime="2007-07-31 15:00:48">31 Jul, 2007</time>

What is the recommended file extension for a bundle? In your example, it
looks like you used .diff, but I imagine that using .diff could get
confusing if you need to know at a glance whether it\'s a udiff or a
bundle.

I think that I\'ve seen a few people using .bundle as the extension, but
I am in no way sure if that\'s standardized in any way.

---
#### [bzr bundles &raquo; Blog of Anders Rune Jensen](http://people.iola.dk/arj/2007/07/31/bzr-bundles/) - <time datetime="2007-07-31 19:16:17">31 Jul, 2007</time>

\[\...\] upon this guide today for how to create better patches when the
project in question is using bzr (such as MMS :)). \[\...\]

---
#### [Daniel Lin](http://ephemient.livejournal.com/) - <time datetime="2007-07-31 21:57:54">31 Jul, 2007</time>

Good advice that isn\'t specific to one revision control system.

darcs send -o my-changes\
darcs send -o my-changes \--context ctx \# even if you can\'t see the
target repository online

darcs apply my-changes

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-07-31 23:33:23">31 Jul, 2007</time>

Eric: I know some of the Bazaar developers prefer that bundles sent to
the Bazaar mailing list use \".patch\" or \".diff\" as extensions since
they generally get sent with a text mime type, making it easier to
display in their mail client.

As for distinguishing bundles, this isn\'t particularly difficult: just
look at the first line.

Daniel: it is good to hear that you can do something similar with Darcs
(I wasn\'t claiming that this feature is unique). Your second example
sounds similar to the \"bzr bundle-revisions\" command, which can also
be used from a single branch or offline. I only described the use of
\"bzr bundle\" since it is less likely to create a bundle that the
recipient can\'t use.

---
#### [Daniel Lin](http://ephemient.livejournal.com/) - <time datetime="2007-08-02 03:09:54">2 Aug, 2007</time>

I\'m not trying to push Darcs \-- Mercurial has \"hg bundle\" as well
\-- I just would like to let people stumbling across this post to come
away with useful knowledge regardless of which distributed VCS they
happen to be using.

In fact, git is the only popular DVCS I know of without support for this
sort of operation\...

---
#### [James Henstridge &raquo; Bazaar bundles as part of a review process](bazaar-bundles-as-part-of-a-review-process.md) - <time datetime="2007-08-16 13:36:13">16 Aug, 2007</time>

\[\...\] James Henstridge Random stuff Skip to content « Bazaar Bundles
\[\...\]

---
