---
title: 'Comparison of Configs/Aliases in Bazaar, CVS and  Subversion'
slug: comparison-of-configsaliases-in-bazaar-cvs-and-subversion
date: 2005-08-29T20:15:36+08:00
tags: ['Bazaar']
---

When a project grows to a certain size, it will probably need a way to
share code between multiple software packages they release. In the
context of Gnome, one example is the sharing of the `libbackground` code
between Nautilus and gnome-control-center. The simplest way to do this
is to just copy over the files in question and manually synchronise
them. This is a pain to do, and can lead to problems if changes are made
to both copies, so you\'d want to avoid it if possible. So most version
control systems provide some way to share code in this way. As with the
previous articles, I\'ll focus on Bazaar, CVS and Subversion

Unlike the common operations each system implements this feature in a
different way, so I\'ll go over each one in turn and then compare them.

**CVS**

When you run the \"`cvs checkout $module`\" command,
CVS will look in the `CVSROOT/modules` file for the repository. For
example, the file might contain the following:

    module foobar

This would tell CVS to check out the foobar directory from the
repository into a directory named `module` when the user asks
for `module`. If no entry is found for a particular name, the
directory by that name is checked out from the repository.

To compose multiple modules into a single working copy, the ampersand
syntax can be used:

    module foo &bar &baz
    bar othermodule/bar

With this modules file, \"`cvs checkout module`\" would give the
following working copy:

| Working Copy | Repository      |
| ------------ | --------------- |
| module       | foo             |
| module/bar   | othermodule/bar |
| module/baz   | baz             |

Operations like `tag`, `commit`, `update`, etc will descend into
included modules, so for the most part a user can treat the resulting
working copy as a single tree. If a particular branch tag exists on all
the included modules, you can even check out a branch of the combined
working copy. There are some problems with the support though:

-   While \"`cvs update`\" will update the working copy, it won\'t
    take into account any changes in `CVSROOT/modules`.
-   If you\'ve only got write access to part of the repository, and
    can\'t write to `CVSROOT/modules`, then you can\'t change
    configurations.
-   While CVS lets you check out old versions of code, you still use the
    latest version of `CVSROOT/modules`. This can make it difficult to
    check out historical versions of the tree.
-   Since \"`cvs tag`\" descends into included modules, you can
    end up with many branch tags on some modules. For instance, the
    `gnome-common/macros` directory in Gnome CVS has 282 branch tags,
    which makes it almost impossible to feed fixes to all those
    branches.

**Subversion**

Rather than a single repository-wide file describing the module
configuration for checkouts, Subversion makes use of the
[`svn:externals`](http://svnbook.red-bean.com/nightly/en/svn.advanced.externals.html)
property on directories.

Any directory can have such a property attached. Each line in the
property is of the form:

    subdir [-rrevnum] absolute-uri-of-tree-to-include

This will check out each the given tree at the given sub dir when ever
\"`svn checkout`\" or \"`svn update`\" are used. However unlike CVS,
\"`svn commit`\" will not descend into the included modules.

Some of the benefits of this approach include:

-   Inclusions can be placed close to the location they are included.
-   It reduces the permissions problems: if you can commit to the
    directory where the inclusion will occur, you can add the inclusion.
-   Can include modules from other repositories. In this case, it is
    actually useful that \"`svn commit`\" doesn\'t descend into the
    included module because it is likely that the user won\'t have
    write access to the external modules.
-   When checking out a historic version of the module, the historic
    version of the `svn:externals` properties get used.

Some of the down sides to the approach include:

-   Module inclusion directives can be scattered throughout the tree.
    There isn\'t a single place to look for such directives.
-   When including something from the same repository, you still need to
    use an absolute URI to identify the module. It is not uncommon for
    committers to use a different URI to access the repository to those
    who only have read access (e.g. `svn+ssh://hostname` for committers,
    `svn://hostname` or `http://hostname` for read-only users). So which
    URI do you use in the `svn:externals` property? You\'ll need to
    choose between a tree that read-only users can\'t check out or a
    tree that committers can\'t commit to \...
-   If you want to branch a set of related modules in the repository,
    you\'ll need to alter the `svn:externals` properties to point at the
    branched versions of the modules. When performing merges back to the
    mainline, you need to make sure you don\'t merge the `svn:externals`
    property changes.
-   When checking out historic versions, although historic
    `svn:externals` definitions get used, you will get the up-to-date
    versions of the included modules unless a particular revision of the
    included module was specified in the property.
-   If the hosting arrangements for an included module change, the
    historical values of `svn:externals` properties will be invalid.

**Bazaar**

The module inclusion system in Bazaar is handled through
\"configurations\". These are simple files stored in a branch with lines
of the form:

    subdirectory archivename/branchname[--patch-NNNN]

After checking out a branch, you can check out the various included
modules by running the following command from the base of the working
copy:

    baz build-config file-name

To update a working copy and all the included modules, you need two
commands:

    baz update
    baz build-config -u file-name

(the `-u` flag is only available in the 1.5 prereleases.
Previously you needed a command like \"`baz cat-config
$filename | xargs -n2 baz update -d`\").

The name of the configuration file is not special, and it is possible to
have multiple configurations stored in a single branch. In fact it is
common to have a branch that stores nothing but configurations, and
assemble the source tree in a subdirectory.

One common use of multiple configs is similar to the use of non-branch
tags in CVS: recording a particular configuration used for a particular
release. This can be done by taking a snapshot of the configuration,
which adds fixed revision numbers to the branches checked out:

    baz cat-config --snap development.config > release-0.42.config

If anyone builds this configuration, they will see the tree as it was
when that snapshot was taken. Some benefits of this system include:

-   It is easy to maintain multiple configurations for a set of
    branches.
-   Since configurations are stored in the same way as other files on
    the branch, anyone can modify them (either by committing to the
    branch, or by creating a new branch and making the change there).
-   Use of the arch namespace to identify branches, so is somewhat
    immune to branch location changes (it is still vulnerable to
    referenced branches disappearing altogether).

Some of the down sides of the approach include:

-   Requires the user to run a second command after checking out the
    branch containing the configuration.
-   No standard name for configurations, so the user needs to know the
    config file name in addition to the branch name when checking things
    out.

**Summary**

Here is a summary of how the three systems stand up against each other
in this respect:

|  | CVS | Subversion | Bazaar |
|--| --- | --- | --- |
| Who can change configs? | Committers to `CVSROOT` | Committers | Anyone |
| Build historic configs? | No | Yes | Sort of (snapshot configs) |
| Supports multiple parallel configurations of same code? | Yes | Yes | Yes |
| `commit` command crosses module inclusion boundaries? | Yes | No | No |
| Configs built by `checkout` command? | Yes | Yes | No |
| Configs built by `update` command? | No | Yes | No |
| Resistant to project hosting changes? | Yes | No | Yes |
| Same config usable for committers and read-only users? | Yes | Yes for DAV access, No for `svn+ssh://` access | Yes |

Each system is slightly different with its benefits and problems. It
isn\'t particularly surprising then that configs are not handled well by
the various version control migration scripts. For example, the
`cvs2svn` script doesn\'t handle them at all (e.g. the KDE Subversion
repository doesn\'t contain any `svn:externals` properties in historic
versions migrated from CVS).

---
### Comments:
#### [Erich Schubert](http://blog.drinsama.de/erich/) - <time datetime="2005-08-30 07:38:33">30 Aug, 2005</time>

Hi, since you apparently are quite an expert on revision management - do
you have a hint for my \"CoW\" problem?\
Basically I\'d like to have copy-on-write branches.\
Meaning that I want files by default to follow the trunk branch, only if
I modify the file it gets \"locked\" to the current branch. So that by
running \"foo update\" I get all the updates, except for where I decided
to diverge?

using svn:externals was suggested to me, but it doesn\'t do the trick, I
need it on a per-file basis. And I\'d like to have it automatically, so
I can just commit my changes and they\'ll end up in my \"overlay\"
repository by default\...

Two blog entries, where I asked for advice for this usage:\
<http://blog.drinsama.de/erich/en/linux/2005082601-server-management.html>\
<http://blog.drinsama.de/erich/en/linux/2005082501-revision-management.html>

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-08-30 11:54:00">30 Aug, 2005</time>

With Bazaar, the way you\'d handle this would be by branching the
upstream. Now rather than running \"update\", you\'d \"merge\" from the
upstream branch, fix conflicts (if there are any), and \"commit\".

To see what your local changes are, just diff your branch against the
upstream one.

This is not quite the same as you asked for, since you will get updates
to files you have modified (hence the possibility of conflicts on
merge). However, this is usually considered a better system, since using
some files from one version and other files from another version could
easily cause problems.

---
#### Sean Kelley - <time datetime="2005-08-30 15:15:59">30 Aug, 2005</time>

Very interesting. I\'ve not used CVS since University. I must confess
that in my job I\'ve been using Borland\'s StarTeam and love it.It is
really hard to go back to the command line again.

Sean

---
#### [fraggle](http://www.soulsphere.org/) - <time datetime="2005-08-30 18:28:11">30 Aug, 2005</time>

Sounds like incredibly useless and confusing functionality and that a
common shared library would be a much better solution.

---
