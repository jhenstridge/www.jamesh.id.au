---
title: 'Gnome-gpg 0.4.0 Released'
slug: gnome-gpg-040-released
date: 2006-03-02T12:08:20+08:00
tags: ['Gnome']
---

I put out [a new
release](http://mail.gnome.org/archives/gnome-announce-list/2006-March/msg00000.html)
of gnome-gpg containing the fixes I [mentioned
previously](gnome-gpg-improvement.md).

The internal changes are fairly extensive, but the user interface
remains pretty much the same. The main differences are:

-   If you enter an incorrect passphrase, the password prompt will be
    displayed again, the same as when gpg is invoked normally.
-   If an incorrect passphrase is stored in the keyring (e.g. if you
    changed your key\'s passphrase), the passphrase prompt will be
    displayed. Previously you would need to use the
    `--forget-passphrase` option to tell gnome-gpg to ignore the
    passphrase in the keyring.
-   The passphrase dialog is now set as a transient for the terminal
    that spawned it, using the same algorithm as zenity. This means that
    the passphrase dialog pops up on the same workspace as the terminal,
    and can\'t be obscured by the terminal.

---
### Comments:
#### [Marius Gedminas](http://mg.b4net.lt/) - <time datetime="2006-03-02 23:07:57">4 Mar, 2006</time>

Any ideas how to use it with Mutt?

---
#### [Marius Gedminas](http://mg.b4net.lt/) - <time datetime="2006-03-03 03:31:08">5 Mar, 2006</time>

I got gnome-gpg working with Mutt:

\
\" tell Mutt not to ask for a passphrase (it appears that you need to
have Mutt 1.5.11 for this to work)\
set pgp\_use\_gpg\_agent

\" tell Mutt to use gnome-gpg: I copied the default gpg command, removed
\--batch, and replaced gpg with gnome-gpg\
set pgp\_sign\_command=\"gnome-gpg \--no-verbose \--quiet \--output -
%?p?\--passphrase-fd 0? \--armor \--detach-sign \--textmode %?a?-u %a?
%f\"

\
(Um, where\'s the preview button? What sort of markup can I use in
comments?)

---
#### Tony D - <time datetime="2006-03-19 22:40:44">0 Mar, 2006</time>

Hey James.\
Saw that great stuff you posted about Australia\'s number 1 show,
\"Double the Fist\".\
I just thought you\'d like to know that I\'ve started an online petition
to the ABC to bring the show back. Here\'s the link:

<http://www.petitiononline.com/FullFist/petition.html>

Tell as many people as possible. The more signiatures, the better our
chances.\
Full Fist.

---
