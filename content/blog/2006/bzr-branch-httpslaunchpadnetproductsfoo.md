---
title: 'bzr branch https://launchpad.net/products/foo'
slug: bzr-branch-httpslaunchpadnetproductsfoo
date: 2006-10-10T15:29:09+08:00
draft: false
tags: ['Bazaar', 'Launchpad']
---

One of the things we\'ve been working on for
[Launchpad](https://launchpad.net/) is good integration with
[Bazaar](http://bazaar-vcs.org/). Launchpad provides a way to register
or host Bazaar branches, and nominate a Bazaar branch as representing a
particular product series.

For each registered branch, there is a branch information page. This
leads to a bit of confusion since Bazaar uses URLs to identify branches,
so people try running `bzr branch` on a branch information page. We also
get people trying to branch the product or product series pages.

There were two ways we could address this problem: (1) do more to
encourage people not to do this, or (2) make `bzr branch` do what the
user meant it to do. The second option is the more user friendly, so
that\'s what we chose. This just left the problem of how to implement it
efficiently.

The obvious way to get this to work is with a simple HTTP redirect for
files under the `.bzr/` directory. Unfortunately this would result in
Bazaar hitting the Launchpad webapp for every file in the branch which
is not desirable (each request results in a number of database accesses,
which would add unnecessary load to the system). There is a [Bazaar
bug](https://launchpad.net/bugs/36004) about improving this so that it
would use the new location after the first redirect. This bug was the
main reason for not implementing the feature previously.

While playing around with things a bit, I realised that Bazaar already
had the features needed to implement the redirects and they have been
there since 0.8.

In Bazaar 0.8, the concept of a *lightweight checkout* was introduced.
This is just a working tree plus a reference to a branch stored
elsewhere. You can perform most operations on the branch from the
checkout directory that you can do from the real branch directory. So
what happens if you publish the \"branch reference\" part of a
lightweight checkout on the web? It turns out that they work fine, so
that\'s what I used for `launchpad.net`.

So with the change in place, the following commands will all give you a
copy of the Bazaar webserve plugin:

    bzr branch http://bazaar.launchpad.net/~bzr/bzr-webserve/webserve-dev
    bzr branch https://launchpad.net/people/bzr/+branch/bzr-webserve/webserve-dev
    bzr branch https://launchpad.net/products/bzr-webserve/trunk
    bzr branch https://launchpad.net/products/bzr-webserve

Furthermore, they will all record the `http://bazaar.launchpad.net/` URL
as the parent branch, so future `bzr pull` commands will go directly to
the branch.
