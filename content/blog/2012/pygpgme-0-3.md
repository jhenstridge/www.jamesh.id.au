---
title: 'pygpgme 0.3'
slug: pygpgme-0-3
date: 2012-03-11T23:04:20+08:00
tags: ['Python']
---

This week I put out a new release of pygpgme: a Python extension that
lets you perform various tasks with OpenPGP keys via the [GPGME
library](http://www.gnupg.org/related_software/gpgme/).  The new release
is available from both
[Launchpad](https://launchpad.net/pygpgme/trunk/0.3) and
[PyPI](http://pypi.python.org/pypi/pygpgme/0.3).

There aren\'t any major new extensions to the API, but this is the first
release to support Python 3 (Python 2.x is still supported though).  The
main hurdle was ensuring that the module correctly handled text vs.
binary data.  The split I ended up on was to treat most things as text
(including textual representations of binary data such as key IDs and
fingerprints), and treat the data being passed into or returned from the
encryption, decryption, signing and verification commands as binary
data.  I haven\'t done a huge amount with the Python 3 version of the
module yet, so I\'d appreciate [bug
reports](https://bugs.launchpad.net/pygpgme/+filebug) if you find
issues.

So now you\'ve got one less reason not to try Python 3 if you were
previously using pygpgme in your project.
