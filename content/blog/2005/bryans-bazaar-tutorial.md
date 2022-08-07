---
title: 'Bryan''s Bazaar Tutorial'
slug: bryans-bazaar-tutorial
date: 2005-07-08T10:22:00+08:00
tags: ['Bazaar', 'Gnome']
---

[Bryan](http://www.gnome.org/~clarkbw/blog/GNOME/how_i_used_baz_to_start_my_little_project):
there are a number of steps you can skip in your little tutorial:

1.  You don\'t need to set `my-default-archive`. If you often work with
    multiple archives, you can treat working copies for all archives
    pretty much the same. If you are currently inside a working copy,
    any branch names you use will be relative to your current one, so
    you can still use short branch names in almost all cases (this is
    similar to the reason I don\'t set `$CVSROOT` when working with
    CVS).

2.  If you have a directory which contains only the files you want to
    import into your Bazaar archive, the following command will add them
    all, and convert the directory into a Bazaar working copy:\

        cd background-channels
        baz import -a bclark@redhat.com--gnomearchive/background-channels--dev--0.1

    No need for `init-tree`, `add` or `commit`.

3.  Running `archive-mirror` in your working copy will mirror that
    archive, so doesn\'t need `my-default-archive` set.

4.  Other people probably don\'t want to set your archive as their
    default. Also, they can ommit the `register-archive` call entirely:\

        baz get http://gnome.org/~clarkbw/arch/background-channels--dev--0.1

    This checks out the branch, and registers the archive as a side
    effect.

5.  If you want to find out what is inside an archive, the following
    command is quite convenient:\

        baz abrowse http://gnome.org/~clarkbw/arch

Some things you might want to do:

1.  If you have a PGP key, create a signed archive. This will
    cryptographically sign all revisions. When people checkout your
    branches, the signatures get checked automatically (this is useful
    [if the server hosting your mirror gets broken
    into](http://mail.gnome.org/archives/gnome-announce-list/2004-March/msg00113.html)
    and you need to verify that nothing has been tampered with). If you
    have already created the archive, you can turn on signing with
    `baz change-archive` (remember to update the mirror archive too).

2.  If you turn on signing, consider using a PGP agent like
    [gnome-gpg](http://people.redhat.com/~walters/gnome-gpg/). You can
    configure it in `~/.arch-params/archives/defaults`.

3.  It is customary to name the archive directory the same as the
    archive name. This has the benefit that the branch name matches the
    last portion of the URL.

4.  If you haven\'t set up a revision library, you should do so:\

        mkdir ~/.arch-revlib
        baz my-revision-library ~/.arch-revlib
        baz library-config --greedy --sparse ~/.arch-revlib

---
### Comments:
####  - <time datetime="2005-07-09 01:56:47">6 Jul, 2005</time>

Reverse the order of those last two revlib commands:\
baz my-revision-library \~/.arch-revlib\
baz library-config \--greedy \--sparse \~/.arch-revlib

---
