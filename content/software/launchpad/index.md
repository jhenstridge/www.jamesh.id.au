---
title: "Launchpad"
date: 2008-07-24T09:43:37+08:00
keywords: ["launchpad", "ubuntu"]
---

From 2004 to 2008, I worked on the [Launchpad](https://launchpad.net)
code hosting site for Canonical.  As well as providing hosting for
third party Open Source projects, the site is central to the Ubuntu
project: doing everything from bug tracking to managing the package
repository.

<!--more-->

Launchpad is written in Python using the Zope 3 component framework,
and backed by a PostgreSQL database.  Over that time, I worked on a
number of areas of the site:

* The [OpenID](https://openid.net/) provider backing on to Launchpad's
  account store.  While it could be used to log in to any
  OpenID-supporting website, it was primarily intended to provide
  unified login for Canonical and Ubuntu community sites.  In
  particular, it gave community-run sites first class integration
  without having to expose user credentials.

  As well as the standard Simple Registration and Attribute Exchange
  extensions, we also implemented a custom "team membership"
  extension.  This allowed relying party sites to ask whether the
  authenticating user was a member of certain groups on Launchpad.
  This has been used by various sites to limit access to certain
  members of the Ubuntu community.

  This was later separated out from Launchpad into its own service
  (`login.ubuntu.com`), and and ported to Django.

* We instituted a policy of pre-merge code reviews, and I was one of
  the members of the code review team.  To help with this, I wrote
  some tools to summarise the list of pending code reviews, including
  checking that branches could still be merged without conflict, and
  producing diffs for the benefit of the code reviewer.

  These tools ended up inspiring the "merge proposal" feature of
  Launchpad's code hosting system.

* I built the original version of Launchpad's "oops" error reporting
  system.  Together with tools to summarise the day's error reports,
  it gave visibility to pages that were causing errors, timing out, or
  coming close to timing out.  It also gave users a simple "oops ID"
  to identify particular failures in bug reports about the site
  itself.

  The error reports also included a log of the database queries
  performed during the request.  This allowed us to track down
  requests that were performing more queries than necessary, or were
  simply executing slow queries.

* Launchpad was originally written using the SQLObject object
  relational mapper.  We made the decision to switch to an in-house
  developed ORM called [Storm](https://storm.canonical.com), and I
  handled migration of the code base.  This involved substantial
  improvements to Storm to cover Launchpad's use case.

* I handled data imports for a number of different project bug
  trackers.  This involved working with the external project to export
  their bug data, write a conversion routine to match Launchpad's data
  model, and perform the import.

  The largest import was Ubuntu's old Bugzilla instance, which at the
  time dwarfed the set of bugs already in Launchpad.

My work on Launchpad also resulted in a few small Python libraries:

[pygettextpo](https://launchpad.net/pygettextpo)
: A small Python extension wrapping the translation message catalog
  parser from the libgettextpo library.

[pygpgme](https://launchpad.net/pygpgme)
: A wrapper for the GPGME library, providing access to various OpenPGP
  crypto operations via [The GNU Privacy Guard](https://gnupg.org/).
