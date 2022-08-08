---
title: 'Re: Pushing a bzr branch with rsync'
slug: re-pushing-a-bzr-branch-with-rsync
date: 2006-12-15T10:10:19+09:00
tags: ['Bazaar']
---

This article responds to some of the points in Andrew\'s post about
[Pushing a bzr branch with
rsync](http://research.operationaldynamics.com/blogs/andrew/software/version-control/bzr-repository-rsync.html).

**`bzr rspush` and shared repositories**

First of all, to understand why `bzr rspush` refuses to operate on a
non-standalone branch, it is worth looking at what it does:

1.  Download the revision history of the remote branch, and check to see
    that the remote head revision is an ancestor of the local head
    revision. If it is not, error out.
2.  If it is an ancestor, use rsync to copy the local branch and
    repository information to the remote location.

Now if you bring shared repositories into the mix, and there is a
different set of branches in the local and remote repositories, then
step (2) is liable to delete revision information needed by those
branches that don\'t exist locally. This is not a theoretical concern if
you do development from multiple machines (e.g. a desktop and a laptop)
and publish to the same repository.

**Storage Formats and Hard linking**

The data storage format used by Bazaar was designed to be cross platform
and compact. The compactness is important for the dumb/passive server
mode, since the on-disk representation has a large impact on how much
data needs to be transferred to pull or update a branch.

The representation chosen effectively has one \"knit\" file per file in
the repository, which is only ever appended to (with deltas to the
previous revision, and occasional full texts), plus a \"knit index\"
file per knit that describes the data stored inside the knit. Knit index
files are much smaller than their corresponding knit files.

When pushing changes, it is a simple matter of downloading the knit
index, working out which revisions are missing, append those to the knit
and update the index. When pulling changes, the knit index is downloaded
and the required sections of the knit file are downloaded (e.g. via an
HTTP range request).

The fact that the knit files get appended to is what causes problems
with hard linked trees. Unfortunately the SFTP protocol doesn\'t really
provide a way to tell whether a file has multiple links or a way to do
server side file copies, so while it would be possible to break the
links locally, it would not be possible when updating a remote branch.

Furthermore, relying on hard links for compact local storage of related
branches introduces platform compatibility problems. ~~Win32 does not
support hard links~~ (**update:** apparently they [are
supported](http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/fsutil_hardlink.mspx),
but hidden in the UI), and while MacOS X does support them its HFS+ file
system has a very inefficient implementation (see [this
article](http://rixstep.com/2/20040621,00.shtml) for a description).

**Rsync vs. The Bazaar smart server**

As described above, Bazaar is already sending deltas across the wire.
However, it is slower than rsync due due to it waiting on more round
trips. The smart server is intended to eventually resolve this
discrepancy. It is a fairly recent development though, so hasn\'t
achieved its full potential (the development plan has been to get Bazaar
to talk to the smart server first, and then start accelerating certain
operations).

When it is more mature, a push operation would effectively work out
which revisions the remote machine is missing, and then send a bundle of
just that revision data in one go, which is about the same amount of
round trips as you\'d get with rsync.

This has the potential to be faster than an equivalent rsync:

-   Usually each revision only modifies a subset of the files in the
    tree. By checking which files have been changed in the revisions to
    be transferred, Bazaar will only need to open those knit files. In
    contrast, rsync will check every file in the repository.
-   In Andrew\'s rsync script, the entire repository plus a single
    branch are transferred to the server. While only one branch is
    transferred, the revision information for all branches will be
    transferred. It is not too difficult to reconstruct the branches
    from that data (depending on what else is in the repository, this
    could be a problem). In contrast, Bazaar only transfers the
    revisions that are part of the branch being transferred.

So it is worth watching the development of the smart server over the
next few months: it is only going to get faster.

---
### Comments:
#### [Juri Pakaste](http://www.iki.fi/juri/blog/) - <time datetime="2006-12-15 17:54:20">15 Dec, 2006</time>

Are you sure about that Win32 and hard links bit? Windows XP and later
ship with a tool called fsutil.exe which claims to create hard links and
the stuff it creates looks exactly like hard links to me.\

---
#### James Henstridge - <time datetime="2006-12-15 18:27:42">15 Dec, 2006</time>

Juri: thanks for pointing that out. I\'ve updated the text to reflect
this.

---
