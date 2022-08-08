---
title: 'Revision Control Migration and History Corruption'
slug: revision-control-migration-and-history-corruption
date: 2006-02-16T15:04:13+08:00
tags: ['Bazaar', 'Gnome', 'JHBuild']
---

As most people probably know, the Gnome project is planning a migration
to [Subversion](http://subversion.tigris.org/). In contrast, I\'ve
decided to move development of jhbuild over to
[`bzr`](http://bazaar.canonical.com/). This decision is a bit easier for
me than for other Gnome modules because:

-   No need to coordinate with
    [GDP](http://developer.gnome.org/projects/gdp/ "Gnome Documentation Project")
    or
    [GTP](http://developer.gnome.org/projects/gtp/ "Gnome Translation Project"),
    since I maintain the docs and there is no translations.
-   Outside of the moduleset definitions, the large majority of
    development and commits are done by me.
-   There aren\'t really any interesting branches other than the
    mainline.

I plan to leave the Gnome module set definitions in CVS/Subversion
though, since many people help in keeping them up to date, so leaving
them there has some value.

I performed a test conversion using
[Tailor](http://www.darcs.net/DarcsWiki/Tailor) 0.9.20. My first attempt
at performing the conversion failed part way through. Looking at what
had been imported, it was apparent that the first few changesets created
*weren\'t the first changesets I\'d created in CVS*. What was weirder
still was the dates on those changesets: they were dated 1997, while I
hadn\'t started jhbuild til 2001.

It turns out that it was caused by clock skew on the CVS server back in
September 2003, so the revision dates for a few files are not monotonic.
I did the quick fix of directly editing the RCS files (I was working off
a local copy of the repo), which allowed the conversion to run through
to completion. The problem has been reported as [bug
\#37](http://progetti.arstecnica.it/tailor/ticket/37) in Tailor\'s bug
tracker.

This made me a bit worried about whether the CVS to Subversion
conversion script being used for the rest of the Gnome modules was also
vulnerable to this sort of clock skew problem. Sure enough it was, and
the first real changeset of jhbuild had been imported as [revision
323](http://svn.gnome.org/viewsvn/jhbuild?view=rev&rev=323).

I did a bit more checking of the CVS repository, and found that there
were [98 other
modules](http://mail.gnome.org/archives/gnome-hackers/2006-February/msg00080.html)
exhibiting clock skew in their revision history, spread over 1245 files
(some files with multiple points of skew). I\'ve only checked the SVN
test conversions of some of these modules, but all the ones I checked
exhibited the same type of corruption.

It is going to be a fair bit of work cleaning it all up before the final
conversion.
