---
title: 'Ubuntu Bugzilla Migration Comment Cleanup'
slug: ubuntu-bugzilla-migration-comment-cleanup
date: 2006-09-05T07:07:41+08:00
tags: ['Launchpad', 'Ubuntu']
---

Earlier in the year, we [migrated the bugs from `bugzilla.ubuntu.com`
over to Launchpad](bugzilla-to-malone-migration.md). This process
involved changes to the bug numbers, since the
[Launchpad](https://launchpad.net/) is used for more than just
[Ubuntu](http://www.ubuntu.com/) and already had a number of bugs
reported in the system.

People often refer to other bugs in comments, which both Bugzilla and
Launchpad conveniently turn into links. The changed bug numbers meant
that the bug references in the comments ended up pointing to the wrong
bugs. The bug import was done one bug at a time, so if bug A referred to
bug B but bug B hadn\'t been imported by the time we were importing bug
A, then we wouldn\'t know what bug number it should be referring to.

The solution we used was to just insert a link to the bug watch URL
(e.g.
`https://launchpad.net/malone/bugtrackers/ubuntu-bugzilla/$BUGID`),
which allowed people to find the referenced bug, but was a bit ugly.

Today we ran a fixup script to remove these bug watch URLs from comments
and rewrite the old Bugzilla bug numbers to the current Launchpad bug
numbers. This cleans up the old imported bugs a bit so they fit in
better with the bugs entered directly into Launchpad.

---
### Comments:
#### [Rudd-O](http://rudd-o.com/) - <time datetime="2006-09-05 14:33:07">5 Sep, 2006</time>

Wasn\'t it easier to perform a topological sort before doing the import?
A bit of Python grease would have done it ;-)

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-09-05 17:46:35">5 Sep, 2006</time>

Rudd-O: That wouldn\'t be possible with a one-bug-at-a-time conversion.
Consider the following chain of events:

1\. Alice files bug 42\
2. Bob files bug 43 about the same issue\
3. Charles adds a comment to bug 42 saying that bug 43 looks like a
duplicate\
4. Alice closes bug 43 making a comment that it is a duplicate of bug
42.

Which order do you import the two bugs?

---
