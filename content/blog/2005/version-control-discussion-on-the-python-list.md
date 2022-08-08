---
title: 'Version control discussion on the Python list'
slug: version-control-discussion-on-the-python-list
date: 2005-08-15T12:29:35+08:00
tags: ['Bazaar', 'Launchpad', 'Python']
---

The Python developers have been discussing a migration off CVS on the
python-dev mailing list. During the discussion,
[Bazaar-NG](http://www.bazaar-ng.org/) was mentioned. A few posts of
note:

-   Mark Shuttleworth provides some [information on the Bazaar
    roadmap](http://mail.python.org/pipermail/python-dev/2005-August/055372.html).
    Importantly, Bazaar-NG will become Bazaar 2.0.
-   Steve Alexander describes [how we use Bazaar to develop
    Launchpad](http://mail.python.org/pipermail/python-dev/2005-August/055376.html).
    This includes a description of the branch review process we use to
    integrate changes into the mainline.

I\'m going to have to play around with `bzr` a bit more, but it looks
very nice (and should require less typing than `baz` \...)

---
### Comments:
####  - <time datetime="2005-08-15 18:56:36">15 Aug, 2005</time>

Been on the Ubuntu site some mins ago and been readin\' about Bazaar. I
wonder why Bazar if we have fine things like SVN. What\'s wrong with
SVN? Because it\'s not written in Python?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-08-15 20:04:22">15 Aug, 2005</time>

Bazaar supports distributed development, while Subversion does not.

If you want to create a branch of a subversion repository, you need
write access to the repository. With a distributed system, I can branch
off from someone else\'s codebase without requiring their permission and
be able to make use of the same features as the main developers.

If you\'ve ever worked on a patch for some software managed in CVS or
Subversion where you have no write access, then you\'ll know what I mean
\-- you have no way to make incremental commits, add new files, do a
partial rollback, etc.

---
