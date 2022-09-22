---
title: 'bzr commit --author'
slug: bzr-commit-author
date: 2008-05-12T17:19:59+08:00
tags: ['Bazaar']
---

One of the features I recently discovered in
[Bazaar](http://bazaar-vcs.org/) is the `--author` option for
\"`bzr commit`\". This lets you make commits to a Bazaar branch on
behalf of another person. When used, the new revision credits two
people: you as the committer and the other person as the author.

While Bazaar does make it easy for non-core contributors to send changes
in a form that correctly attributes them (e.g. by publishing a branch or
sending a bundle), I doubt we\'ll ever see the end of pure patches.
Some cases include:

-   Patches based on a tarball release.  In these cases the contributor
    likely hasn\'t even used the VCS.
-   People send simple diffs from e.g. \"`bzr diff`\" since that is
    sometimes the easiest solution (or what they do by default due to
    having transferred their knowledge from another VCS).
-   Some people use a VCS bridge so they can work with their favourite
    VCS. They might not be able to provide their changes as Bazaar
    commits due to this.

The `--author` option lets you commit these changes in a way that
credits the contributor for their work. The author of the change will
then be displayed in \"`bzr annotate`\" output and credited along with
the you in the \"`bzr log`\" output.

The feature is also used by a number of plugins such as
[bzr-rebase](https://launchpad.net/bzr-rebase): if you replay or rebase
someone else\'s changes, the new revisions will creit you as the
committer and the original committer as the author.

---
### Comments:
#### [ovitters](http://blogs.gnome.org/ovitters/) - <time datetime="2008-05-13 04:04:28">13 May, 2008</time>

Please post more BZR stuff. Especially issues/unique things regarding
bzr vs other DVCS and SVN. This for preparation of the DVCS decision at
GUADEC. Note that I\'ve setup rsync for testing purposes (to get the SVN
repositories). DVCS experts can mail gnome-sysadmin\@gnome.org for the
details.

---
