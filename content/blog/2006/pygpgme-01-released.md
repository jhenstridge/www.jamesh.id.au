---
title: 'pygpgme 0.1 released'
slug: pygpgme-01-released
date: 2006-03-29T09:30:22+08:00
tags: ['Launchpad', 'Python']
---

Back in January I started working on a new Python wrapper for the [GPGME
library](http://www.gnupg.org/(en)/related_software/gpgme/index.html). I
recently put out the first release:

> <http://cheeseshop.python.org/pypi/pygpgme/0.1>

This library allows you to encrypt, decrypt, sign and verify messages in
the OpenPGP format, using gpg as the backend. In general, it stays
fairly close to the C API with the following changes:

-   Represent C structures as Python classes where appropriate (e.g.
    contexts, keys, etc). Operations on those data types are converted
    to methods.
-   The `gpgme_data_t` type is not exposed directly. Instead, any Python
    object that looks like a file object can be passed (including
    StringIO objects).
-   In cases where there are `gpgme_op_XXXX()` and
    `gpgme_op_XXXX_result()` function pairs, these have been replaced by
    a single `gpgme.Context.XXXX()` method. Errors are returned in the
    exception where appropriate.
-   No explicit memory management. As expected for a Python module,
    memory management is automatic.

The module also releases the global interpreter lock over calls that
fork gpg subprocesses. This should make the module multithread friendly.

This code is being used inside [Launchpad](https://launchpad.net/) to
verify incoming email and help manage users\' PGP public keys.

In other news, `gnome-gpg` 0.4 [made it into
dapper](https://launchpad.net/distros/ubuntu/dapper/+package/gnome-gpg),
so users of the next Ubuntu release can see the improvements.
