---
title: 'New Default Branch Format in Bzr'
slug: new-default-branch-format-in-bzr
date: 2006-04-27T16:47:34+08:00
tags: ['Bazaar']
---

One of the new features in the soon to be released bzr 0.8 is the new
\"knit\" storage format.

When comparing the size of the repository data for jhbuild with \"knit\"
and \"metadir\" formats (metadir is just the old storage format with
repository, branch and checkout bookkeeping separated), I see the
following:

                    metadir   knit
  ----------------- --------- -------
  Size              9.9MB     5.5MB
  Number of files   1267      307

The reason for the smaller number of files is that information about all
revisions in the repository is now stored together rather than in
separate files. So the file count comes out at a constant plus 2 times
the number of tracked files (a knit index file plus the knit data file).
For comparison, the CVS repository I imported this from was 4.4MB, and
comprised 143 files.

As well as reducing storage requirements, the new knit repository format
is designed to reduce network traffic. With the current weave repository
format, the weave file for each file touched by a commit gets rewritten
to include the contents of the new revision. In contrast to this, the
information about the new revision can simply be appended to the knit
data file and the knit index file updated to match. This means
publishing a branch to a server via sftp mainly involves append
operations, resulting in a nice speed up.

Similarly when pulling new changes from a published branch, bzr only
needs to download a knit index to find out which sections of the knit
data are missing locally. It can then ask for just the changed sections
(by an HTTP range request or a partial read with sftp), rather than
downloading the entire contents of the changed weaves.

Overall, this should make bzr 0.8 a lot more usable than 0.7 for various
network operations.

---
### Comments:
#### Olaf Conradi - <time datetime="2006-04-28 00:33:24">5 Apr, 2006</time>

Hi

A minor (k)nitpick :)

Metadir is the bzrdir format to hold tree, branch and/or repository
formats.

Your comparison was between the weave and knit repository formats. They
both reside in a metadir.

Cheers\
-Olaf

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-04-28 01:21:53">5 Apr, 2006</time>

Olaf: I was comparing a repository created with \"bzr init-repo
\--format=metadir\" with one created using \"bzr init-repo
\--format=knit\". The other value the help mentions is \"weave\", but
that just prints an error stating \"Format shared repository is not
compatible with .bzr version Bazaar-NG branch, format 6.\"

I know that both repository types use the metadir bzr dir layout, but I
decided to use the terminology used in the command line UI.

---
#### Olaf Conradi - <time datetime="2006-04-28 04:48:53">5 Apr, 2006</time>

In latest bzr.dev, the default repository format for metadir changed
from weave to knit.

Creating a repository through \"bzr init-repo \--format=metadir\" will
create a knit repository. Issuing a \"bzr init-repo \--format=weave\"
will create one using weave. The error should actually be a warning, it
does create a valid weave repository.

---
#### michele - <time datetime="2006-04-28 17:20:58">5 Apr, 2006</time>

Hey guys, it would be nice to upload a egg of bzr 0.8 to the cheese shop
\[1\] once released\... so it\'s easy\_installable. ;-)

---
#### wayne - <time datetime="2006-05-06 05:48:06">6 May, 2006</time>

Note that the current development version of bzr has changed the format
name of a weave inside a metadir from \"metadir\" to \"metaweave\". This
new terminology will be included in the 0.8 release.

---
