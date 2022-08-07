---
title: 'DVCS talks at GUADEC'
slug: dvcs-guadec
date: 2008-07-09T05:04:01+08:00
tags: ['Bazaar', 'Gnome', 'GUADEC']
---

Yesterday, a BoF was scheduled for discussion of distributed version
control systems with GNOME.  The BoF session did not end up really
discussing the issues of what GNOME needs out of a revision control
system, and some of the examples Federico used were a bit snarky.

We had a more productive meeting in the session afterwards where we went
over some of the concrete goals for the system.  The list from the
blackboard was:

-   Contributor collaboration (i.e. let anyone use the tool rather than
    just core developers).
-   Distro ⇔ distro and distro ⇔ upstream collaboration.
-   Host GNOME source code repositories
-   Code review
-   Server side hooks
-   Translators: what to do?
-   Enforced checks
-   Offline operations
-   Documentation authors?
-   Support Win32/Mac (important for GTK)

The sys admin tasks were broken down to:

-   MAINTAINERS file syntax checking
-   PO file syntax checking
-   [CIA](http://cia.vc/) integration.
-   Commits mailing list
-   Check that commit messages are not empty
-   Trigger updates from commits (e.g. the web site module).
-   Release notes tarballs
-   [Damned Lies](http://l10n.gnome.org/) support

It was clear from the discussion that neither Git or Bazaar satisfied
all of the criteria.

**The Playground**

[John Carr](http://blogs.gnome.org/johncarr) did a great job setting up
Bazaar mirrors of all the GNOME modules.  This provided an easy way for
people to see play around with Bazaar.  However, it only gave you half
the experience since it didn\'t provide a way to publish code and
collaborate.

To aid in this, we have set up the `bzr-playground.gnome.org` machine,
which any GNOME developer should be able to use to publish branches
based on John\'s imports.  Instructions on getting set up can be found
[on the wiki](http://live.gnome.org/Bazaar/DemoMachine).  I hope that we
will get a lot of people trying out this infrastructure.

We gave a presentation today on some of the things Bazaar provides that
could be useful when hacking on GNOME.  Demoing `bzr-playground` was a
bit problematic due to the internet connection problems at the venue,
but I think we still showed some useful tools for local collaboration,
searching and code review.

Meanwhile, [Robert Collins](http://www.advogato.org/person/robertc/) has
been working on some of the GNOME sysadmin features that Bazaar was
lacking.  Among other things, he got Damned Lies working with both
Subversion and Bazaar, with a test installation [on the playground
machine](http://bzr-playground.gnome.org/damned-lies/).

---
### Comments:
#### [Kristian H](http://hoegsberg.blogspot.com/) - <time datetime="2008-07-09 05:46:08">3 Jul, 2008</time>

Do we honestly think that at this point there\'s a killer
feature/showstopper bug that\'s going to decide which DVCS GNOME goes
with? The debate has detoriated to an emacs vs vi type discussion where
all that\'s left is personal preference and mudslining (typically based
on the state of the tools 3 years ago). There\'s nothing that any of
these tools can\'t do that any of the other tools can\'t do (possibly
with a little effort).

It\'s time to admit that the choice is going to be based on fiat or vote
and then just make a decision instead of endless BOFs, test migrations,
workshops, feature matrices, work flow analysis.

Thank you. I like git, btw ;)

---
#### Vadim P. - <time datetime="2008-07-09 06:57:43">3 Jul, 2008</time>

Great, I\'d be interested to read what comes out of \'Support Win32\'.
I\'ve started to use GTK for Windows for cross-platform, and while it\'s
dead easy to setup and use, it would be nice if there were official
standards on this.

---
#### Rob - <time datetime="2008-07-09 16:19:32">3 Jul, 2008</time>

Is it possible to publish bzr branches for experimental modules that are
not yet in gnome svn? That\'d be great \...

---
