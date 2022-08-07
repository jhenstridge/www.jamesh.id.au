---
title: '--create-prefix not needed with bazaar.launchpad.net'
slug: create-prefix-not-needed-with-bazaarlaunchpadnet
date: 2006-09-06T08:08:27+08:00
tags: ['Bazaar', 'Launchpad']
---

When [outlining the use of team branches on
Launchpad](http://blogs.gnome.org/view/jamesh/2006/08/17/1) previously,
I used the [\--create-prefix]{.kbd} option when pushing the branch to
[sftp://bazaar.launchpad.net]{.kbd}. This was to make sure the initial
push would succeed, even if the [/\~username/product]{.kbd} directory
the branch would be created in didn\'t exist.

To simplify things for users, we made a change to the SFTP server in the
latest release, so that [\--create-prefix]{.kbd} is no longer necessary.
This does not affect the allowed branch directories though: the
structure is used to associate the branches with products, and decide
who can write to the branches.

Another change included in the rollout is the ability to rename branches
and reassign them to different owners through the web interface. So for
instance, you can give ownership of a personal branch to a team your
project grows to multiple developers. This should be used sparingly,
since it will change the published branch URLs which can confuse people
using your branch.
