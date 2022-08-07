---
title: 'ViewCVS'
slug: viewcvs
date: 2004-04-19T03:03:03+08:00
draft: false
---

Made a few more changes to the Gnome
[viewcvs](http://cvs.gnome.org/viewcvs/). Pretty much all of the
original ugly colour scheme is gone now, and I got it to pretty print
some more files with gnome specific file extensions.

We are maintaining the modifications in CVS using the standard vendor
branch/main branch setup. Since the `cvs import` command is one that
people screw up the most, I wrote some scripts to help with exporting
viewcvs from upstream CVS and then importing it into our CVS.

When I went to test the script, it worked fairly well, except for the
fact that some of the template files had been moved between the two
pulls. Since there was no link between the two different file names, CVS
wasn\'t able to merge my local changes. Other than that, the merge went
okay.

I wonder if Arch or Subversion would have been able to handle this
situation any better, given that the upstream repository didn\'t record
that the file had been moved?
