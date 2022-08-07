---
title: 'Signed Revisions with Bazaar'
slug: signed-revisions-with-bazaar
date: 2007-10-04T00:26:19+08:00
draft: false
tags: ['Bazaar']
---

One useful feature of [Bazaar](http://bazaar-vcs.org/) is the ability to
cryptographically sign revisions. I was discussing this with
[Ryan](http://blogs.gnome.org/desrt/) on IRC, and thought I\'d write up
some of the details as they might be useful to others.

Anyone who remembers the past security of [GNOME](http://www.gnome.org/)
and [Debian](http://www.debian.org/) servers should be able to
understand the benefits of being able to verify the integrity of a
source code repository after such an incident. Rather than requiring all
revisions made since the last known safe backup to be examined, much of
the verification could be done mechanically.

**Turning on Revision Signing**

The first thing you\'ll need to do is get a
[PGP](http://en.wikipedia.org/wiki/Pretty_Good_Privacy) key and
configure [GnuPG](http://www.gnupg.org/) to use it. The [GnuPG
handbook](http://www.gnupg.org/gph/en/manual.html#AEN26 "Generating a new keypair")
is a good reference on doing this. As the aim is to provide some
assurance that the revisions you publish were really made by you, it\'d
be good to get the key signed by someone.

Once that is done, it is necessary to configure Bazaar to sign new
revisions. The easiest way to do this is to edit `~/.bazaar/bazaar.conf`
to look something like this:

    [DEFAULT]
    email = My Name <me@example.com>
    create_signatures = always

Now when you run \"`bzr commit`\", a signature for the new revision will
be stored in the repository. With this configuration change, you will be
prompted for your pass phrase when making commits. If you\'d prefer not
to enter it repeatedly, there are a few options available:

1.  install `gpg-agent`, and use it to remember your pass phrase in the
    same way you use ssh-agent.
2.  install the `gnome-gpg` wrapper, which lets you remember your pass
    phrase in your Gnome keyring. To use `gnome-gpg`, you will need to
    add an additional configuration value:
    \"`gpg_signing_command = gnome-gpg`\".

Signatures are transferred along with revisions when you push or pull a
branch, perform merges, etc.

**How Does It Work?**

So what does the signature look like, and what does it cover? There is
no command for printing out the signatures, but we can access them using
bzrlib. As an example, lets look at the signature on the head revision
of one of my branches:

    >>> from bzrlib.branch import Branch
    >>> b = Branch.open('http://bazaar.launchpad.net/~jamesh/storm/reconnect')
    >>> b.last_revision()
    'james.henstridge@canonical.com-20070920110018-8e88x25tfr8fx3f0'
    >>> print b.repository.get_signature_text(b.last_revision())
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1

    bazaar-ng testament short form 1
    revision-id: james.henstridge@canonical.com-20070920110018-8e88x25tfr8fx3f0
    sha1: 467b78c3f8bfe76b222e06c71a8f07fc376e0d7b
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v1.4.6 (GNU/Linux)

    iD8DBQFG8lMHAa+T2ZHPo00RAsqjAJ91urHiIcu4Bim7y1tc5WtR+NjvlACgtmdM
    9IC0rtNqZQcZ+GRJOYdnYpA=
    =IONs
    -----END PGP SIGNATURE-----

    >>>

If we save this signature to a file, we can verify it with a command
like \"`gpg --verify signature.txt`\" to prove that it was made using my
PGP key. Looking at the signed text, we see three lines:

1.  An identifier for the checksum algorithm. This is included to future
    proof old signatures should the need arise to alter the checksum
    algorithm at a later date.
2.  The revision ID that the signature applies to. Note that this is the
    full globally unique identifier rather than the shorter numeric
    identifiers that are only unique in the context of an individual
    branch.
3.  The checksum, in SHA1 form.

For the current signing algorithm, the checksum is made over the long
form testament for the revision, which can easily be verified:

    $ bzr branch http://bazaar.launchpad.net/~jamesh/storm/reconnect
    $ cd reconnect
    $ bzr testament --long > testament.txt
    $ sha1sum testament.txt
    467b78c3f8bfe76b222e06c71a8f07fc376e0d7b  testament.txt

Looking at the long form testament, we can see what the signature
ultimately covers:

1.  The revision ID
2.  The name of the committer
3.  The date of the commit
4.  The parent revision IDs
5.  The commit message
6.  A list of the files that comprise the source tree for the revision,
    along with SHA1 sums of their contents
7.  Any revision properties

So if the revision testament matches the revision signature and the
revision signature validates, you can be sure that you are looking at
the same code as the person who made the signature.

It is worth noting that while the signature makes an assertion about the
state of the tree at that revision \-- the only thing it tells you about
the ancestry is the revision IDs of the parents. If you need assurances
about those revisions, you will need to check their signatures
separately. One of the reasons for this is that you might not know the
full history of a branch if it has [ghost
revisions](http://bazaar-vcs.org/GhostRevision) (as might happen when
importing code from certain foreign version control systems).

**Signing Past Revisions**

If you\'ve already been using Bazaar but had not enabled revision
signing, it is likely that you\'ve got a bunch of unsigned revisions
lying around. If that is the case, you can sign the revisions in bulk
using the \"bzr sign-my-commits\" command. It will go through all
revisions in the ancestry, and generate signatures for all the commits
that match your committer ID.

**Verifying Signatures in Bulk**

To verify all signatures found in a repository, John Arbash Meinel\'s
signing plugin can be used, which provides a \"bzr verify-sigs\"
command. It can be installed with the following commands:

    $ mkdir -p ~/.bazaar/plugins
    $ bzr branch http://bzr.arbash-meinel.com/plugins/signing/ ~/.bazaar/plugins/signing

When the command is run it will verify the integrity of all the
signatures, and give a summary of how many revisions each person has
signed.

---
### Comments:
#### [Kurt McKee](http://kurtmckee.org/) - <time datetime="2007-10-04 03:29:42">4 Oct, 2007</time>

Fantastic post! This is exactly why I read the planets. Thanks!

---
