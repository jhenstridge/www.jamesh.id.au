---
title: 'Using OpenSSH with bzr'
slug: using-openssh-with-bzr
date: 2005-11-17T09:19:18+08:00
tags: ['Bazaar']
---

One of the transports available in
[[bzr]{.kbd}](http://www.bazaar-ng.org/) is [sftp]{.kbd}. This is
implemented using the [Paramiko](http://www.lag.net/paramiko/) SSH and
SFTP library. Unfortunately there are a few issues I experienced with
the code:

-   Since it is an independent implementation of SSH, none of my OpenSSH
    settings in `~/.ssh/config` were recognised. The particular options
    I rely on include:
    1.  `User`: when the remote username doesn\'t match my local one.
        One less thing to remember when connecting to a remote machine.
    2.  `IdentityFile`: use different keys to access different machines.
    3.  `ProxyCommand`: access work machines that are behind the
        firewall.
-   Paramiko does not currently support SSH compression. This is a real
    pain for larger trees.

The easiest way to fix all these problems would be to use OpenSSH
directly, so wrote a small plugin to do so. I decided to follow the
model used to do this in `gnome-vfs` and Bazaar 1.x: communicate with an
`ssh` subprocess via pipes and implement the SFTP protocol internally.

Since SFTP is layered fairly cleanly on top of SSH, and the paramiko
code was also quite modular, it was possible to use the paramiko SFTP
implementation with openssh. The result is a small plugin that
monkey-patches the existing SFTP transport:

> <http://people.ubuntu.com/~jamesh/bzr-openssh-plugin/>

Just copy `openssh-sftp.py` into the `~/.bazaar/plugins` directory, and
use `bzr` as normal. The compression seems to make a noticable
difference to performance, but it should be possible to improve things
further with a pipelined SFTP client implementation.

Of course, the biggest performance optimisation will probably come from
the [smart server](http://bazaar.canonical.com/SmartServer), when that
is implemented.

---
### Comments:
#### [Jay R. Wren](http://little.xmtp.net/blog/) - <time datetime="2005-11-18 04:52:58">5 Nov, 2005</time>

Another HUGE (IMO) benefit of your work is the benefits gained by using
OpenSSH and its Connection Caching feature.

<http://little.xmtp.net/blog/2005/11/04/ssh-connection-sharing-c-visibility-share-libraries-and-gcc-attributes-oh-my/>

You can have an ssh connection in the background, and allow all other
ssh connections to use that existing one. No connection build up or tear
down. It is VERY fast.

---
#### [Wouter Bolsterlee](http://uwstopia.nl/) - <time datetime="2005-11-19 01:35:37">6 Nov, 2005</time>

Debian Sarge does not include python-crypto and paramiko packages. These
are needed for ssh/sftp support in bzr. I\'ve created backported
packages for Debian Sarge. See this blog posting for more information:\
<http://uwstopia.nl/blog/2005/11/open-ssh-bazaar-ng-debian-sarge>

---
