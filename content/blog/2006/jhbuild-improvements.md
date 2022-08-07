---
title: 'JHBuild Improvements'
slug: jhbuild-improvements
date: 2006-05-01T10:39:45+08:00
draft: false
tags: ['Bazaar', 'Gnome', 'JHBuild']
---

I\'ve been doing most JHBuild development in my
[bzr](http://www.bazaar-vcs.org/) branch recently. If you have bzr
0.8rc1 installed, you can grab it here:

> `bzr branch http://www.gnome.org/~jamesh/bzr/jhbuild/jhbuild.dev`

I\'ve been keeping a regular CVS import going at
`http://www.gnome.org/~jamesh/bzr/jhbuild/jhbuild.cvs` using Tailor, so
changes people make to module sets in CVS make there way into the bzr
branch. I\'ve used a small hack so that merges back into CVS get
recorded correctly in the `jhbuild.cvs` branch:

1.  Apply the diff between `jhbuild.cvs` and `jhbuild.dev` to my CVS
    checkout and commit.
2.  Modify tailor to pause before committing the to `jhbuild.cvs`.
3.  While tailor is paused, run `bzr revert` followed by a merge of the
    same changes from `jhbuild.dev`.
4.  Let tailor complete the commit.

It\'s a bit of a hack, but it allows me to do repeated merges from the
CVS import to my development branch (and back again). It also means that
any file moves I do in my bzr branch are reflected in the CVS import
when merged.

So now when filing bug reports on jhbuild, you can submit fixes in the
form of bzr branches as well as patches.

So, on to the improvements:

**Generic Version Control Interface**

Previously, to add support for a new version control system the
following additions were needed:

-   Some code to invoke the version control utility to make checkouts
    and update working trees.
-   Code to implement the build state machine for modules using the
    version control system (these classes would generally derive from
    `AutogenModule` which implemented most of the build logic).
-   Code to create instances of the above module type when parsing
    `.modules` files.

This was quite a bit of work, and in the end would only help if the code
in question was set up to build the same way as most Gnome modules (i.e.
with a `autogen.sh` script and autotools). If you wanted to build a
module using Python distutils out of Subversion, a new module type would
be needed. If you wanted to build a
[distutils](http://docs.python.org/inst/inst.html) module from a
tarball, that would be another module type again.

With the new system, the different version control support modules
provide a common interface. This means that a single module type is
capable of implementing the build state machine for any version control
system. Similarly, it should now be possible to implement distutils
module support such that it will work with any supported version control
system.

This work is not yet finished though. A bit more work needs to be done
to parse version control system agnostic module definitions from
`.modules` files. When this is done, a fair bit of the current syntax
can be deprecated and eventually removed. When this is done, adding
support for a new version control system shouldn\'t take more than
100-200 lines.

**Module Type Simplifications**

As well as reducing the number of module types that need to be
maintained in JHBuild, I\'ve been working on simplifying the code in
these module types. Previously, each stage of a module build was
represented by a method call on the module type. The return value of the
method was used to say (a) whether the stage succeeded or not, (b) what
the next state would be and (c) if an error occurred some alternative
next states to go to (e.g. offer to rerun `autogen.sh`).

With the new system, the next state and error states are declared as
attributes on the method object. The method can indicate a failure by
raising a particular exception. This greatly simplifies the cases where
a build stage involves a number of separate actions that could each fail
individually, since the exception cuts processing short without the
error checks getting in the way of the code.

There are still a few module build stages not converted to the new
system since their next state depends on various config settings (e.g.
if running \"make check\" has been enabled or not). Since these
generally involve skipping a stage based on some criteria, the plan is
to move the logic to the stage being skipped, which should simplify
things further.

---
### Comments:
#### Anonymous - <time datetime="2006-05-02 16:34:06">2 May, 2006</time>

So, would \"build Debian packages\" also work as a jhbuild module?
Basically, take dist tarball, rename to appropriate .orig.tar.gz name,
copy in debian directory, call dpkg-source to make diff and dsc, call
pdebuild with various arguments to make debs, possibly needing to make
previous debs available to pbuilder as build-depends for subsequent
debs.

---
#### Anonymous - <time datetime="2006-05-02 16:34:24">2 May, 2006</time>

Also, do you have GIT support planned?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-05-03 11:36:43">3 May, 2006</time>

Anonymous \#1: you could probably do up a module type in jhbuild to help
with building debian packages. Hopefully the changes I\'m making should
make this easier if you decide to do such a modification.

Anonymous \#2: already committed, and being used for \"cairo\" in the
gnome-2.16 module set.

---
####  - <time datetime="2006-05-11 05:55:05">4 May, 2006</time>

Since jhbuild supports Arch as a module source, is baz also supported?

Also, is SCons supported as a module type?\

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-05-11 18:52:16">4 May, 2006</time>

JHBuild supports modules that use Arch for version control by using the
baz-1.x client.

There is no support for modules stored in bzr yet, partly because I was
waiting for 0.8 to come out \-- the new checkout feature feels like the
best option for jhbuild setups.

There is no support for the scons build tool at this point, but the
refactoring should make it possible to add support in such a way that it
will work with all supported version control systems (cvs, subversion,
darcs, git, arch and tarballs). Previously you\'d end up writing a fair
bit of boilerplate to support all the VC backends.

---
####  - <time datetime="2006-05-11 21:35:51">4 May, 2006</time>

Thanks for the reply. (I did mean bzr \[not baz\] in my first question.)

Looking forward to the new refactoring.

---
