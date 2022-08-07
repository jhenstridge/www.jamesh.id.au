---
title: 'Version Control Workflow'
slug: version-control-workflow
date: 2005-08-11T12:34:06+08:00
draft: false
tags: ['Bazaar', 'Launchpad']
---

[Havoc](http://log.ometer.com/2005-08.html#10): we are looking at ways
to better integrate version control in
[Launchpad](https://launchpad.net/). There are many areas that could
benefit from better use of version control, but I\'ll focus on bug
tracking since you mentioned it.

Take the attachment handling in [Bugzilla](http://www.bugzilla.org/),
for instance. In non-ancient versions, you can attach statuses to
attachments such as \"obsolete\" (which has some special handling in the
UI --- striking out obsolete attachments and making it easy to mark
attachments as obsolete when uploading a new attachment). This makes it
easy to track and manage a sequence of patches as a fix for a bug is
developed ([bug
118372](http://bugzilla.gnome.org/show_bug.cgi?id=118372) is a metacity
bug with such a chain of patches).

If you look at this from a version control perspective, this sequence of
patches forms a branch off the mainline of the software, where each
newly attached patch is a new revision. The main differences being:

-   No explicit indication of what the patch was made against (code base
    or revision), or what options were used to create the patch.
-   No linkage between successive patches (can be a bit confusing if
    multiple patch series are attached to the same bug report).

So why not just use real version control to manage patches in the bug
tracker? The big reason for projects using CVS or Subversion is that
only authenticated users can create branches in the repository, and you
don\'t want to require contributors to ask permission before submitting
fixes.

So this is an area where a distributed version control system can help:
anyone can make a branch, so potential contributors don\'t need
permission to begin working on a bug. This also has the benefit that the
contributors get access to the same tools as the developers (which is
also helpful if they ever become a regular developer).

Now if you combine this with history sensitive merging and tell the bug
tracker what the mainline branches of the products are, you can do some
useful things:

-   Try and merge the changes from the bug fix branch onto the mainline,
    and see if it merges cleanly. This can tell a developer at a glance
    whether the patch has bitrotted. This could also be used to produce
    an up to date diff to the mainline, which can aid review of the
    changes.
-   Check if the bug fix branch has been merged into the mainline. No
    need for developers to manually flag the attachment as such.

We discussed some of these features in the context of Launchpad at the
recent Brazil meeting.
