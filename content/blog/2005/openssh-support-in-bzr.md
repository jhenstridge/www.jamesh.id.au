---
title: 'OpenSSH support in bzr'
slug: openssh-support-in-bzr
date: 2005-11-30T14:29:12+08:00
tags: ['Bazaar']
---

I updated my [bzr openssh
plugin](http://blogs.gnome.org/view/jamesh/2005/11/17/0) to be a proper
patch against `bzr.dev`, and got it merged. So if you have
`bzr-openssh-sftp.py` in your `~/.bazaar/plugins` directory, you should
remove it when upgrading.

Unfortunately there was a small problem resolving a conflict when
merging it, which causes the path to get mangled a little inside
`_sftp_connect()`. Once this is resolved, the mainline `bzr` should
fully follow settings in `~/.ssh/config`, because it will be running the
same ssh binary as you normally use.

One thing I learnt when adding the support code was a quirk in the [SFTP
URI
spec](http://www.ietf.org/internet-drafts/draft-ietf-secsh-scp-sftp-ssh-uri-03.txt)\'s
interpretation of paths, which differs to gnome-vfs\'s interpretation.
The uri `sftp://remotehost/directory` is interpreted as `/directory` on
`remotehost` by gnome-vfs, while the spec says that it should be
interpreted as `~/directory`.

To refer to `/directory` on `remotehost`, the spec says you should use
`sftp://remotehost/%2Fdirectory`. I filed this as [bug
322394](http://bugzilla.gnome.org/show_bug.cgi?id=322394 "SFTP URLs do not follow specification").
