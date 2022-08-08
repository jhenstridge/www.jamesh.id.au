---
title: 'Bazaar bundles as part of a review process'
slug: bazaar-bundles-as-part-of-a-review-process
date: 2007-08-16T13:36:08+08:00
tags: ['Bazaar']
---

In [my previous
article](bazaar-bundles.md "Bazaar Bundles"),
I outlined [Bazaar](http://bazaar-vcs.org/)\'s bundle feature. This
article describes how the Bazaar developers use bundles as part of their
development and code review process.

Proposed changes to Bazaar are generally posted as patches or bundles to
the development mailing list. Each change is discussed on the mailing
list (often going through a number of iterations), and ultimately
approved or rejected by the core developers. To aide in managing these
patches Aaron Bentley (one of the developers wrote a tool called [Bundle
Buggy](http://bundlebuggy.aaronbentley.com/).

Bundle Buggy watches messages sent to the mailing list, checking for
messages containing patches or bundles. It then creates an entry on the
web site displaying the patch, and lets developers add comments (which
get forwarded to the mailing list).

Now while Bundle Buggy can track plain patches, a number of its time
saving features only work for bundles:

1.  **Automatic rejection of superseded patches:** when working on a
    feature, it is common to go through a number of iterations. When
    going through the list of pending changes, the developers don\'t
    want to see all the old versions. Since a bundle describes a Bazaar
    branch, and it is trivial to check if one branch is an extension of
    another though, Bundle Buggy can tell which bundles are obsolete and
    remove them from the list.
2.  **Automatically mark merged bundles as such:** the canonical way to
    know that a patch has been accepted is for it to be merged to
    mainline. Each Bazaar revision has a globally unique identifier, so
    we can easily check to see if the head revision of the bundle is in
    the ancestry of mainline. When this happens, Bundle Buggy
    automatically marks them as merged.

Using these techniques the list of pending bundles is kept under
control.

**Further Possibilities**

Of course, these aren\'t the only things that can be done to save time
in the review process. Another useful idea is to automatically try and
merge pending bundles or branches to see if they can still be merged
without conflicts. This can be used as a way to put the ball back in the
contributors court, obligating them to fix the problem before the branch
can be reviewed.

This sort of automation is not only limited to projects using a mailing
list for code review. The same techniques could be applied to a robot
that scanned bug reports in the bug tracker (e.g.
[Bugzilla](http://bugzilla.gnome.org/)) for bundles, and updated their
status accordingly.

---
### Comments:
#### [Stewart Smith](http://www.flamingspork.com) - <time datetime="2007-08-17 07:44:59">17 Aug, 2007</time>

world of awesome

---
