---
title: 'gnome-gpg improvement'
slug: gnome-gpg-improvement
date: 2006-01-13T05:54:49+08:00
tags: ['Gnome']
---

The [gnome-gpg](http://people.redhat.com/~walters/gnome-gpg/) utility
makes PGP a bit nicer to use on Gnome with the following features:

-   Present a Gnome password entry dialog for passphrase entry.
-   Allow the user to store the passphrase in the session or permanent
    keyring, so it can be provided automatically next time.

Unfortunately there are a few usability issues:

-   The anonymous/authenticated user radio buttons are displayed in the
    password entry dialog, while they aren\'t needed.
-   The passphrase is prompted for even if `gpg` does not require it to
    complete the operation.
-   If the passphrase is entered incorrectly, the user is not prompted
    for it again like they would be with plain `gpg`.
-   If an incorrect passphrase is provided by `gnome-keyring-daemon`,
    you need to remove the item using `gnome-keyring-manager` or use the
    `--force-passphrase` command line argument.

I put together a patch to fix these issues by using `gpg`\'s
`--status-fd`/`--command-fd` interface. Since this provides status
information to `gnome-gpg`, it means it knows when to prompt for and
send the passphrase, and when it gave the wrong passphrase.

I also swiped the `zenity_util_show_dialog()` function from Zenity to
make the password dialog a transient of the terminal that ran it, so the
passphrase dialog stays on the same desktop and can\'t be obscured by
that terminal.

The changes can be found here:

> http://www.gnome.org/\~jamesh/arch/james\@jamesh.id.au/gnome-gpg\--devel\--0

(a Bazaar 1.x branch, since Colin was using Arch).

There are still a few issues with handling non-password prompts from
gpg, but it works quite well for the basics.

---
### Comments:
#### Adam Schreiber - <time datetime="2006-01-14 00:34:33">14 Jan, 2006</time>

James,

I was wondering if gnome-gpg\'s functionality shouldn\'t be integrated
with Seahorse in some manner.

Adam

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-01-14 12:55:47">14 Jan, 2006</time>

Adam: gnome-gpg serves a fairly different purpose to Seahorse. It acts
as a wrapper for gpg that lets you store your passphrase in the Gnome
keyring. So if you have a script or program that wants to invoke gpg,
you can drop in gnome-gpg instead.

In contrast, Seahorse is designed as a GUI for performing
encryption/decryption/signing/verification. It doesn\'t really overlap
that much.

The one place where they could cooperate is in the names of the keys
they store in gnome-keyring. If those match, then the user would only
need to type their passphrase in once for both uses.

---
#### Anonymous - <time datetime="2006-01-15 09:09:00">15 Jan, 2006</time>

Any chance of making use of gpg-agent if available? I prefer to store my
GPG passphrase in gpg-agent.

---
