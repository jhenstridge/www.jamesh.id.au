---
title: 'SSL caching on Firefox 3'
slug: firefox-ssl
date: 2008-05-01T17:57:44+08:00
---

Since upgrading to [Ubuntu
Hardy](http://www.ubuntu.com/products/whatisubuntu/804features/), I\'ve
been enjoying using [Firefox 3](http://wiki.mozilla.org/Firefox3).  The
reduced memory usage has made a lot of other things nicer to use (I
don\'t feel like I need to buy more memory now).  One thing that is nice
to see fixed is caching of SSL content.

In previous versions of Firefox, SSL content was never cached to disk
with the default settings.  While you certainly don\'t want all SSL
content to be written to disk, a lot of it can be cached without
problem.  For example, it is important that the CSS and JavaScript for a
page be served via SSL to avoid man in the middle attacks (injecting
arbitrary active content into a secure page is bad), but there isn\'t
much harm in caching them to disk: if the attacker can modify the disk
cache then SSL probably doesn\'t matter much.

Now it was possible to turn on disk caching in Firefox 2 through the
[browser.cache.disk\_cache\_ssl](http://kb.mozillazine.org/Browser.cache.disk_cache_ssl)
hidden option, but it had a serious drawback: the security information
for resources was not saved in the disk cache so you\'d get a broken
padlock if resources were loaded from the cache.

Firefox 3 fixes up the disk cache to record the security information
though, so turning on disk\_cache\_ssl setting no longer results in a
broken padlock.  But what about all the people using Firefox with its
default settings (or those who do not want all SSL content cached to
disk)?  For these users, the web server can still cause some content to
be cached.

By sending the
\"[Cache-Control](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9):
public\" response header, the server can say that a resource can be
stored in the disk cache.  Firefox 3 will respect this irrespective of
the disk\_cache\_ssl setting.  This should bring Firefox back into
parity with Internet Explorer with respect to network  performance on
SSL web sites.
