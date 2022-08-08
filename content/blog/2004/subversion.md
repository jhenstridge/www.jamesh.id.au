---
title: 'Subversion'
slug: subversion
date: 2004-07-29T16:47:12+08:00
---

Have been looking at the [Subversion 1.1 release
candidate](http://subversion.tigris.org/svn_1.1_releasenotes.html), and
it looks pretty good. This could be the point where more people start to
seriously look at using Subversion as a CVS replacement.

This would be largely due to the new
[fsfs](http://web.mit.edu/ghudson/info/fsfs) repository backend. This
new backend doesn\'t use berkeley db, and shouldn\'t ever wedge like the
BDB backend does occasionally. Furthermore, you don\'t need write access
to the repository to perform read only operations. This should make it a
lot easier to set up systems where you have multiple ways of accessing
the repository (eg. svnserve/ssh for write access, DAV and viewcvs for
read access).

The fsfs backend stores each revision of the repository as two files in
the repository (one for changes to the files/properties, and one to
store revision properties), and doesn\'t modify the files associated
with previous revisions when performing a commit. This means that the
the existing backup and mirror infrastructure that projects have set up
for CVS repositories should work equally well for Subversion.

The \"new file for each revision\" policy also has some nice features.
In the case of svn+ssh access where each committer can directly access
the repository files, it means that the existing revisions in the
repository can be made readonly without preventing people from
committing new revisions (something that can\'t really be done with
CVS).

These administrative improvements should make it a lot easier to deploy
Subversion, which in turn let more developers take advantage of its
features.
