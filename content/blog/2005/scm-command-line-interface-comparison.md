---
title: 'SCM Command Line Interface Comparison'
slug: scm-command-line-interface-comparison
date: 2005-05-12T08:01:03+08:00
draft: false
tags: ['Bazaar']
---

With the current discussion on
[gnome-hackers](http://mail.gnome.org/archives/gnome-hackers/2005-May/thread.html)
about whether to switch Gnome over to
[Subversion](http://subversion.tigris.org/), it has been brought up a
number of times that people can switch from CVS to Subversion without
thinking about it (the implication being that this is not true for
Arch). Given the improvements in [Bazaar](http://bazaar.canonical.com/),
it isn\'t clear that Subversion is the only system that can claim this
benefit.

For the sake of comparison, I\'m considering the case of a shared
repository accessed by multiple developers over SSH. While this doesn\'t
exploit all the benefits of Arch, it gives a better comparison of the
usability of the different tools.

**Setup**

Before using any of CVS, Subversion or Arch, you\'ll need a repository.
This can be done with the following commands (run on the repository
server):

    cvs init /cvsroot
    svnadmin create --fs-type=fsfs /svnroot
    baz make-archive --signed arch@example.org /archives/arch@example.org

(the `--signed` flag can be omitted if you don\'t want to
cryptographically sign change sets)

Once the archive is created, you\'d need to make sure that everyone has
write access to the files, and new files will be created with the
appropriate group ownership. This procedure is the same for each system.

Now before users of the arch archive can start using the archive, they
will need to tell baz what user ID to associate. Each user only needs to
do this once. The email address used should match that on your PGP key,
if you\'re using a signed archive.

    baz my-id "Joe User <joe@example.com>"

Next you\'ll want to import some code into the repository. This will be
done from one of the client machines, from the source directory:

    cvs -d :ext:user@hostname:/cvsroot import modulename vendor-tag release-tag
    svn import . svn+ssh://user@hostname/svnroot/modulename/trunk
    baz import -a sftp://user@hostname/archives/arch@example.org/modulename--devel--0

In the subversion case, we\'re using the standard convention of putting
the main branch in a trunk/ subdirectory. In the arch case, you need a
three-level module name, so I picked a fairly generic one.

**Working with the repository**

The first thing a user will want to do is to create a working copy of
the module:

    cvs -d :ext:user@hostname:/cvsroot get modulename
    svn checkout svn+ssh://user@hostname/svnroot/modulename/trunk modulename
    baz get sftp://user@hostname/archives/arch@example.org/modulename--devel--0 modulename

The user can then make changes to the working copy, adding new files
with the `add` sub-command, and removing files with `rm` sub-command.
For Subversion there are also `mv` and `cp` sub-commands. For Arch, the
`mv` sub-command is supported.

To bring the working copy up to date with the repository, all three
systems use the `update` sub-command. The main difference is that CVS
and Subversion will only update the current directory and below, while
Arch will update the entire working copy.

If there are any conflicts during the update, you\'ll get standard
three-way merge conflict markers in all three systems. Unlike CVS, both
Subversion and Arch require you to mark each conflict resolved using the
`resolved` sub-command.

To see what changes you have in your working copy, all three systems
support a `diff` command. Again, this works on the full tree in Arch,
while only working against a subtree in CVS and Subversion. In all three
systems, you can request diffs for individual files by passing the
filenames as additional arguments. Unfortunately `baz` requires you to
pass \"`--`\" as an argument before the filenames, but hopefully
that\'ll get fixed in the future.

When it is time to commit the change, all three systems use the `commit`
sub-command. This command also works on a full tree with Arch.

**Branching and Merging**

Creating a branch is relatively easy in all three systems:

    cvs tag foo-anchor . ; cvs tag -b foo .
    svn cp . svn+ssh://user@host/svnroot/modulename/branches/foo
    baz branch modulename--foo--0

Unlike CVS and Subversion, the `baz` command will also switch the
working copy over to the new branch. By default it will create a branch
in the same repository, but can just as easily create a branch in
another location.

To switch a working copy between branches, the following commands are
used:

    cvs update -r foo
    svn switch svn+ssh://user@host/svnroot/modulename/branches/foo
    baz switch modulename--foo--0

If we switch the working copy back to the trunk, we can merge the
changes from the branch you\'d do the following:

    cvs tag -r foo foo-DATE .; cvs update -j foo-anchor -j foo-DATE .
    svn merge -r branch-rev:HEAD svn+ssh://user@host/svnroot/modulename/branches/foo
    baz merge modulename--foo--0

This is where Arch\'s history sensitive merging starts to shine. Since
the working copy retains a record of what changes it is composed of, the
merge operation simply pulls over the changes that exist in the branch
but not in the working copy \-- there is no need to tell it what range
of changes you want to apply.

To merge more changes from the branch, the CVS and Subversion commands
change, while the Arch one remains constant:

    cvs tag -r foo foo-DATE .; cvs update -j foo-LAST-DATE -j foo-DATE .
    svn merge -r last-merge-rev:HEAD svn+ssh://user@host/svnroot/modulename/branches/foo
    baz merge modulename--foo--0

**Conclusion**

The current Bazaar command line interface isn\'t that different from CVS
and Subversion (it\'s definitely worth a second look if
[`tla`](http://www.gnu.org/software/gnu-arch/) scared you off). The main
difference is that some of the operations work on the whole working copy
rather than a subset by default. In practice, this doesn\'t seem to be
much of a problem.

The history sensitive merge capabilities would probably be quite useful
for Gnome. For example, it would make it trivial to merge bug fixes made
on the stable branch to the head branch.

Disconnected development is a natural extension to the branching and
merging support mentioned earlier. The main difference is that you\'d
have to make a local archive, and then create your branch of the code in
that archive instead of the main one. The rest is handled the same.
