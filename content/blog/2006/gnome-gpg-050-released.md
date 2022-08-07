---
title: 'Gnome-gpg 0.5.0 Released'
slug: gnome-gpg-050-released
date: 2006-09-04T11:36:41+08:00
tags: ['Bazaar', 'Gnome']
---

Over the weekend, I released [gnome-gpg
0.5.0](http://mail.gnome.org/archives/gnome-announce-list/2006-September/msg00002.html).
The main features in this release is support for running without
`gnome-keyring-daemon` (of course, you can\'t save the passphrase
in this mode), and to use the same keyring item name for the passphrase
as [Seahorse](http://seahorse.sourceforge.net/). The release can be
downloaded here:

> <http://download.gnome.org/sources/gnome-gpg/0.5/>

I also switched over from [Arch](http://www.gnuarch.org/) to
[Bazaar](http://www.bazaar-vcs.org/). The conversion was fairly painless
using `bzr baz-import-branch`, and means that I have both my
revisions and Colins revisions in a single tree. The branch can be
pulled from:

    bzr branch http://www.gnome.org/~jamesh/bzr/gnome-gpg/devel gnome-gpg

All of the converted revisions authored by me have been signed with my
PGP key. As signatures can\'t get moved over in the conversion process,
none of Colin\'s revisions are signed. Note that the signatures in
Bazaar are for particular tree states rather than changes between two
tree states, so it doesn\'t affect the trust of the current revisions.

While I was at it, I also converted the other branches I had in my
`www.gnome.org` Arch archive over to bzr. The only other branch
that people might find useful is the `http-resource` code, which
I\'ve updated to compile with the latest `libsoup`.

---
### Comments:
#### Ross Burton - <time datetime="2006-09-04 18:28:01">1 Sep, 2006</time>

This is very cool, but I think the README should document how to switch
applications over to gnome-gpg. For example, I\'d love to use it with:

\* bazaar/bzr\
\* Evolution\

---
#### Ross - <time datetime="2006-09-04 18:44:57">1 Sep, 2006</time>

For reference, the bzr-ng incantation is:

\~/.bazaar/bazaar.conf:

\[DEFAULT\]\
create\_signatures = (always when-required)\
gpg\_signing\_command = gnome-gpg

I don\'t know how to make a branch require signed revisions, so I\'m
using always.\

---
