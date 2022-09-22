---
title: 'Psycopg migrated to Bazaar'
slug: psycopg-migrated-to-bazaar
date: 2008-04-28T22:07:50+08:00
tags: ['Bazaar', 'Launchpad', 'PostgreSQL', 'Python']
---

Last week we moved psycopg from
[Subversion](http://subversion.tigris.org/) to
[Bazaar](http://bazaar-vcs.org/). I did the migration using [Gustavo
Niemeyer](http://blog.labix.org/)\'s
[svn2bzr](https://launchpad.net/svn2bzr) tool with a few tweaks to map
the old Subversion committer IDs to the email address form
conventionally used by Bazaar.

The tool does a good job of following tree copies and create related
Bazaar branches. It doesn\'t have any special handling for stuff in the
tags/ directory (it produces new branches, as it does for other tree
copies). To get real Bazaar tags, I wrote a [simple post-processing
script](http://people.ubuntu.com/~jamesh/add-tags.py) to calculate the
heads of all the branches in a tags/ directory and set them as tags in
another branch (provided those revisions occur in its ancestry). This
worked pretty well except for a few revisions synthesised by a previous
cvs2svn migration. As these tags were from pretty old psycopg 1
releases I don\'t know how much it matters.

As there is no code browsing set up on initd.org yet, I set up mirrors
of the 2.0.x and 1.x branches on [Launchpad](https://launchpad.net/) to
do this:

-   <http://bazaar.launchpad.net/~psycopg/psycopg/2.0.x/>
-   <http://bazaar.launchpad.net/~psycopg/psycopg/1.x/>

It is pretty cool having access to the entire revision history locally,
and should make it easier to maintain full credit for contributions from
non-core developers.
