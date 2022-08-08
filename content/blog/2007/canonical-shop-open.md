---
title: 'Canonical Shop Open'
slug: canonical-shop-open
date: 2007-08-22T15:32:32+08:00
tags: ['Launchpad', 'OpenID', 'Ubuntu']
---

The new [Canonical Shop](https://shop.canonical.com/) was opened
recently which allows you to buy anything from Ubuntu tshirts and DVDs
up to a 24/7 support contract for your server.

One thing to note is that this is the first site using our new
[Launchpad](https://launchpad.net/) single sign-on infrastructure. We
will be rolling this out to other sites in time, which should give a
better user experience to the existing shared authentication system
currently in place for the wikis.

---
### Comments:
#### [sourcecode.de](http://www.sourcecode.de/node/906) - <time datetime="2007-08-22 16:09:34">22 Aug, 2007</time>

**Ubuntus Shop**

---
#### [pvandewyngaerde](http://pvandewyngaerde.myopenid.com/) - <time datetime="2007-08-22 16:18:29">22 Aug, 2007</time>

why not openID authentication ??

---
#### [Wolfger](http://wolfger.wordpress.com/) - <time datetime="2007-08-22 19:50:15">22 Aug, 2007</time>

I second the \"why not OpenID?\" question. For an Open solution, it sure
seems to be underutilized by FOSS websites.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-08-22 21:13:09">22 Aug, 2007</time>

If you look closely, you\'ll see that OpenID is being used under the
hood to authenticate to the shop. As for accepting external OpenIDs as a
form of identification, I can\'t give a time line for that becoming
available.

Note that we are depending on a little more than a simple identity URL
here though. A Launchpad ID also means we have a verified email address
for the account, and don\'t need to redo that validation when using the
shop.

---
