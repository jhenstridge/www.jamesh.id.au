---
title: 'JHBuild Updates'
slug: jhbuild-updates
date: 2006-06-05T06:53:11+08:00
tags: ['Gnome', 'JHBuild']
---

The progress on JHBuild has continued (although I haven\'t done much in
the last week or so). Frederic Peters of
[JhAutobuild](http://jhbuild.bxlug.be/) fame now has a CVS account to
maintain the client portion of that project in tree.

**Perl Modules**
([\#342638](http://bugzilla.gnome.org/show_bug.cgi?id=342638))

One of the other things that Frederic has been working on is support for
building Perl modules (which use a `Makefile.PL` instead of a configure
script). His initial patchworked fine for tarballs, but by switching
over to the new generic version control code in jhbuild it was possible
to support Perl modules maintained in any of the supported version
control systems without extra effort.

**Speed Up Builds**
([\#313997](http://bugzilla.gnome.org/show_bug.cgi?id=313997))

One of the other suggestions for jhbuild that came up a while ago was to
make it \"eleventy billion times faster\". In essence, adding a mode
where it would only rebuild modules that had changed. While the idea has
merrit, the proposed implementation had some problems (it used the
output of \"cvs update\" to decide whether things had changed).

I\'d like to get something like this implemented, preferably with three
possible behaviours:

1.  Build everything (the current behaviour).
2.  Build only modules that have changed.
3.  Build only modules that have changed, or have dependencies that have
    changed.

The second option is obviously the fastest, and is a useful option for
collections of modules that should be API stable. The third option is
essentially an optimisation of the first option. For both the second and
third option, it is necessary to be able to tell if the code in a module
has been updated. The easiest way to do this is to record an identifier
for the tree state, and the identifier is different after an update.

The identifier should be cheap to calculate too, so will probably be
dependent on the underlying version control system:

-   **CVS** - a hash of the names and versions of all files in the tree.
    Something like
    [this](http://bugzilla.gnome.org/attachment.cgi?id=65483&action=view),
    maybe (can be constructed by reading the `CVS/Root`,
    `CVS/Repository` and `CVS/Entries` files in the tree).
-   **Subversion** - a combination of (a) the repository UUID, (b) the
    path of the tree inside the repository and (c) the youngest revision
    for this subtree in the repository.
-   **Arch** - the output of \"`baz tree-id`\".
-   **Bzr** - the working tree\'s revision ID.
-   **Darcs** - a hash of the sequence of patches representing the tree,
    maybe?
-   **Tarballs** - the version number for the tarball.

On a successful build, the ID for the tree would be recorded. On
subsequent builds, the ID gets recalculated after updating the tree. The
new and old IDs are then used to decide on whether to build the module
or not, according to the chosen policy.

---
### Comments:
#### [Thomas Thurman](http://marnanel.livejournal.com) - <time datetime="2006-06-05 13:37:20">1 Jun, 2006</time>

The state identifiers idea sounds really exciting.

---
#### Josh Triplett - <time datetime="2006-06-05 13:47:15">1 Jun, 2006</time>

For GIT, you can use the sha1sum for the commit or tag. Various GIT
commands will give you this value; for example, git-rev-parse will give
you the sha1sum given the symbolic branch name or tag name.

---
