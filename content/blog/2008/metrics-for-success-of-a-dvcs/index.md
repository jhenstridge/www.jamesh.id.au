---
title: 'Metrics for success of a DVCS'
slug: metrics-for-success-of-a-dvcs
date: 2008-07-31T17:40:32+08:00
tags: ['Bazaar', 'Gnome']
---

One thing that has been
[mentioned](http://blogs.gnome.org/xclaesse/2008/07/14/back-from-istanbul/)
in the GNOME DVCS debate was that it is as easy to do \"git diff\" as it
is to do \"svn diff\" so the learning curve issue is moot.  I\'d have to
disagree here.

**Traditional Centralised Version Control**

With traditional version control systems  (e.g. CVS and Subversion) as
used by Free Software projects like GNOME, there are effectively two
classes of users that I will refer to as \"committers\" and \"patch
contributors\":

{{< figure src="centralised-vcs.png" width="250" height="168"
        alt="Centralised VCS Users" >}}

Patch contributors are limited to read only access to the version
control system.  They can check out a working copy to make changes, and
then produce a patch with the \"diff\" command to submit to a bug
tracker or send to a mailing list.  This is where new contributors
start, so it is important that it be easy to get started in this mode.

Once a contributor is trusted enough, they may be given write access to
the repository moving them to the committers group. They now have access
to more functionality from the VCS, including the ability to checkpoint
changes into focused commits, possibly on branches.  The contributor may
still be required to go through patch review before committing, or may
be given free reign to commit changes as they see fit.

Some problems with this arrangement include:

-   New developers are given a very limited set of tools to do their
    work.
-   If a developer goes to the trouble of learning the advanced features
    of the version control system, they are still limited to the read
    only subset if they decide to start contributing to another project.

**Distributed Workflow**

A DVCS allows anyone to commit to their own branches and provides the
full feature set to all users.  This splits the \"committers\" class
into two classes:

{{< figure src="distributed-vcs.png" width="239" height="170"
        alt="Distributed VCS Users" >}}

The social aspect of the \"committers\" group now becomes the group of
people who can commit to the main line of the project -- the core
developers. Outside this group, we have people who make use of the same
features of the VCS as the core developers but do not have write access
to the main line: their changes must be reviewed and merged by a core
developer.

I\'ve left the \"patch contributor\" class in the above diagram because
not all contributors will bother learning the details of the VCS.  For
projects I\'ve worked on that used a DVCS, I\'ve still seen people send
simple patches (either from the \"xxx diff\" command, or as diffs
against a tarball release) and I don\'t think that is likely to change.

**Measuring Success**

Making the lives of core developers better is often brought up as a
reason to switch to a DVCS (e.g. through features like offline commits,
local cache of history, etc).  I\'d argue that making life easier for
non core contributors is at least as important.  One way we can measure
this is by looking at whether such contributors are actually using VCS
features beyond what they could with a traditional centralised setup.

By looking at the relative numbers of contributors who submit regular
patches and those that either publish branches or submit changesets we
can get an idea of how much of the VCS they have used.

It\'d be interesting to see the results of a study based on
contributions to various projects that have already adopted DVCS. 
Although I don\'t have any reliable numbers, I can guess at two things
that might affect the results:

1.  Familiarity for existing developers.  There is a lot of cross
    pollination in Free Software, so it isn\'t uncommon for a new
    contributor to have worked on another project before hand.  Using a
    VCS with a familiar command set can help here (or using the same
    VCS).
2.  A gradual learning curve.  New contributors should be able to get
    going with a small command set, and easily learn more features as
    they need them.

I am sure that there are other things that would affect the results, but
these are the ones that I think would have the most noticeable effects.

---
### Comments:
#### [xclaesse](http://blogs.gnome.org/xclaesse/) - <time datetime="2008-07-31 18:35:42">4 Jul, 2008</time>

In my opinion DVCS gives the exact same workflow than VCS, you can just
use the diff command of your tool and attach the patch on bugzilla. DVCS
gives more power to contributors/commiters that wants/need more complex
things. So that\'s a 100% gain and nothing is lost\... There is nothing
to study, discuss, troll, etc. DVCS is simply better and it\'s obviously
a shame that GNOME still use the worst system ever (equality with CVS).

Any DVCS can do the job, all we need is an admin that pick a random one
and make the move without asking what the community wants because the
community will never agree.

---
#### Hal - <time datetime="2008-07-31 19:41:50">4 Jul, 2008</time>

CVS vs SVN vs DVCS is really a non-issue for me as a \"patch
contributor\"\
The big win would be if maintainers of GNOME packages actually opened
bugzilla, reviewed and then either rejected with reasons or applied the
multitude of patches there. Patches that represent rather a lot of work
done by volunteers who are not being treated with basic politeness when
the patches are just ignored. Right now patch review isn\'t happening.
Why not? Fixing that is the win. Without fixing that you\'re just
pissing into the wind. I don\'t want to fix more GNOME bugs and waste
more of my time if this is the attitude of GNOME devs. DVCS will not fix
that and will yield zero benefit as far as getting more people more
involved. As ever the start would be treating people with the proper
respect, which is not at all a function of their patch quality. Are you
with me on this?

BTW hope all is well with you in the west and this rubbish of you being
a proprietary software developer nowadays ends with a proper release
under and OSI license. Maybe catch you for a beer at the next LCA.

---
#### [jldugger](http://jldugger.livejournal.com) - <time datetime="2008-08-01 01:31:16">5 Aug, 2008</time>

The question is, do we have any evidence that the VCS Users group has
any members outside \"core devel\"?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-08-02 19:26:49">6 Aug, 2008</time>

xclaesse: I agree that almost any use of DVCS is a gain. The question is
how much gain the various tools give, which I think would be worth
investigating as there are some objective metrics that can be checked.

Hal: I didn\'t mean \"patch contributor\" as a negative. Many people who
submit plain patches simply have better things to do than learn about
DVCS features. I think a good DVCS is one that makes it easy for such a
person to start using just the features that make them more productive
without needing to invest a large amount of time.

jldugger: I don\'t have any evidence, but I believe that it should be
possible to gather such evidence (either for or against).

---
#### Hal - <time datetime="2008-08-03 01:13:08">0 Aug, 2008</time>

James, I have better things to do than contribute patches when they will
be totally ignored, regardless of whether they fix actual bugs for which
bugzilla entries existed prior to my attaching a patch. Now I don\'t
mind if after review the maintainer says this isn\'t the way forward,
but why should I spend 5 or 6 hours coming to grips with some part of a
codebase to fix a known bug in GNOME if GNOME maintainers can\'t be
bothered to look at bugzilla then apply or reject the patch?\
Seriously how on earth does the choice of revision control system used
affect me in this situation? It would be the same with source tarballs
as with the funkiest DVCS imaginable. Ignored work is ignored.\
So please don\'t use \"patch contributor\" efficiency as an argument for
anything unless you\'re going to actually do something about getting the
patches, whatever method is used to generate them, reviewed. Reviewing
the patches is the win, VCS is just NOT REMOTELY interesting AT ALL to
\"patch contributors\" until that happens. Changing which Editor I use
won\'t help me write better code. DVCS won\'t get patches reviewed. If
it did, many of us would even use visual source safe if that would help.
Oh by the way I can generate patches with cvs, svn, git, baz, bzr, hg
and diff. Just about any \"patch contributor\" will be in the same boat.
At the risk of labouring \"labouring the point\" the VCS I prefer is the
one used by the project that reviews the patches submitted in bugzilla.

---
