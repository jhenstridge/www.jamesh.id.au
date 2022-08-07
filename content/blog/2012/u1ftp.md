---
title: 'u1ftp: a demonstration of the Ubuntu One API'
slug: u1ftp
date: 2012-07-05T16:19:00+08:00
draft: false
tags: ['Launchpad', 'OAuth', 'Python', 'Ubuntu', 'Ubuntu One']
---

One of the projects I\'ve been working on has been to improve aspects of
the [Ubuntu One Developer
Documentation](https://one.ubuntu.com/developer/) web site.  While there
are still some layout problems we are working on, it is now in a state
where it is a lot easier for us to update.

I have been working on updating our
[authentication/authorisation](https://one.ubuntu.com/developer/account_admin/auth/index)
documentation and revising some of the [file
storage](https://one.ubuntu.com/developer/files/store_files/cloud)
documentation (the API used by the mobile Ubuntu One clients).  To help
verify that the documentation was useful, I wrote a small program to
exercise those APIs.  The result is
[u1ftp](https://launchpad.net/u1ftp): a program that exposes a user\'s
files via an FTP daemon running on localhost.  In conjunction with the
OS file manager or a dedicated FTP client, this can be used to
conveniently access your files on a system without the full Ubuntu One
client installed.

You can download the program from:

<https://launchpad.net/u1ftp/trunk/0.1/+download/u1ftp-0.1.zip>

To make it easy to run on as many systems as possible, I packaged it up
as a [runnable zip
file](http://blogs.gnome.org/jamesh/2012/05/21/python-zip-files/) so can
be run directly by the [Python](http://www.python.org/) interpreter.  As
well as a Python interpreter, you will need the following installed to
run it:

-   On Linux systems, either the gnomekeyring extension (if you are
    using a GNOME derived desktop), or PyKDE4 (if you have a KDE derived
    desktop).
-   On Windows, you will need
    [pywin32](http://sourceforge.net/projects/pywin32/files/pywin32/).
-   On MacOS X, you shouldn\'t need any additional modules.

These could not be included in the zip file because they are extension
modules rather than pure Python.

Once you\'ve downloaded the program, you can run it with the following
command:

    python u1ftp-0.1.zip

This will start the FTP server listening at `ftp://localhost:2121/`. 
Pointing a file manager at that URL should prompt you to log in, where
you can use your standard Ubuntu One credentials and start browsing your
files.  It will verify the credentials against the Ubuntu SSO service
and issue an [OAuth](http://oauth.net/) token that it stores in the
keyring.  The OAuth token is then used to authenticate requests to the
file storage REST API.

While I expect this program to be useful on its own, it was also
intended to act as an example of how the Ubuntu One API can be used. 
One way to browse the source is to simply unzip the package and poke
around.  Alternatively, you can check out the source directly from
Launchpad:

    bzr branch lp:u1ftp

If you come up with an interesting extension to u1ftp, feel free to
upload your changes as a branch on Launchpad.

---
### Comments:
#### jmaspons - <time datetime="2012-07-05 18:20:20">4 Jul, 2012</time>

This means that finally there is a Ubuntu One client for KDE?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2012-07-05 21:48:35">4 Jul, 2012</time>

\@jmaspons: The standard Ubuntu One client should work with Kubuntu.
This is more of a demonstration application rather than an official
client, but if it is still useful to you then that\'s great.

---
#### Flup - <time datetime="2012-07-07 02:11:52">6 Jul, 2012</time>

Hey, one question:\
Will this new U1DB replace the DBUS API ??\
Or will both stay avaiable?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2012-07-07 08:29:24">6 Jul, 2012</time>

\@Flup: U1DB is not a replacement for the file storage \"syncdaemon\",
if that is what you\'re asking. Instead, it is intended for use cases
similar to what we used to use DesktopCouch/CouchDB for where you want
to store structured data (e.g. contacts, bookmarks, notes, etc).

---
#### Marco Parillo - <time datetime="2012-07-09 01:20:28">1 Jul, 2012</time>

\> The standard Ubuntu One client should work with Kubuntu.

Yes it does. But if this is your first Gnome app, you bring in a whole
ton of dependencies.\
https://bugs.launchpad.net/ubuntuone-client/+bug/375145/comments/114

For some KDE users, if they cannot get a KDE app, they would prefer a
bare-bones approach, like:\
\~/.dropbox-dist/dropboxd\
A daemon that \'just works\', albiet with some limitations not present
in the fat client.

Maybe your FTP approach can be extended to be like the dropbox daemon
approach?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2012-07-09 12:50:10">1 Jul, 2012</time>

\@Marco Parillo: as you can see from further comments on that bug, not
all of those are needed to run the file storage syncdaemon: some are for
the GTK version of the control panel and SSO client (it seems both the
GTK and Qt versions are being pulled in by the apt-get command you
issued, which shouldn\'t be necessary).

As for Dropbox, if you\'re talking about the \"Install Dropbox via
command line\" instructions at https://www.dropbox.com/install?os=lnx,
that involves downloading and installing a 19MB archive. Is that really
much better than downloading 20MB of packages that may be reused by
other applications you later install? (an amount that may go down if the
dependency issue gets improved)

Given the amount of work that has gone into the current Ubuntu One
client, it seems silly to throw that away if you\'re after a proper
synchronisation solution (which u1ftp certainly isn\'t: it will be
useless if you go off line).

---
