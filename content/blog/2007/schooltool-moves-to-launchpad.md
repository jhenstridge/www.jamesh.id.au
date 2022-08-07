---
title: 'SchoolTool Moves to Launchpad'
slug: schooltool-moves-to-launchpad
date: 2007-01-18T13:26:35+09:00
draft: false
tags: ['Launchpad']
---

Recently, the [SchoolTool](http://www.schooltool.org/) project has
[migrated to
Launchpad](http://lists.schooltool.org/pipermail/schooltool-dev/2007-January/000916.html)
for their bug tracker.

We performed an import of all their previous bug reports using a new bug
importer I wrote. This was the third Launchpad bug importer I\'d written
(the previous ones being for the Ubuntu Bugzilla import and a
SourceForge importer), so I wanted this one to be the last. So the
design of this importer was to have a simple XML format as an
intermediate step. That way we only need to target the XML format to
support a new bug tracker. This will also make it possible for projects
to provide their bug data in a form we can consume for the cases where
they want to migrate their bugs to Launchpad but Canonical doesn\'t have
the resources to do the migration.

For the SchoolTool migration, Jean-François Roche put together a simple
[Roundup](http://roundup.sourceforge.net/) exporter.

We should have some documentation about the intermediate XML format
available at some point for projects interested in moving to Launchpad.

---
### Comments:
#### [Jelmer Vernooij](http://samba.org/~jelmer/) - <time datetime="2007-01-18 21:53:43">4 Jan, 2007</time>

This sounds very nice. Is this intermediate format generic or
launchpad-specific? It\'d be nice to have some sort of standardized
format that could be used to migrate between BTS\'es (Bugzilla -\> trac,
Bugzilla -\> launchpad, launchpad -\> jitterbug, etc)

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2007-01-18 22:06:54">4 Jan, 2007</time>

Jelmer: it is tailored to the kind of data that you can store in
Launchpad, and uses the bug status and importance names from Launchpad,
so it\'s current form is not generic.

That said, I have no problem with people writing importers that use the
format as input. I\'ve even got code to export a products bugs from
Launchpad in this format (modulo a few bugs that need to be fixed), so
it can be used for migrations in the other direction.

---
