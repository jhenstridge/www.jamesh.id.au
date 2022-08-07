---
title: '17 December 2003'
slug: 17-december-2003
date: 2003-12-17T09:25:07+08:00
---

[**Callum**](http://www.advogato.org/person/Spooky/diary.html?start=24):
the slowness of modular DocBook XSLT stylesheets is in the chunking
code, as I [found out a while
ago](http://www.advogato.org/person/jamesh/diary.html?start=75). You
will find that if you turn off chunking (ie. produce one huge output
file rather than many smaller files), the processing time will be cut in
half. Interestingly, the older DSSSL stylesheets showed the opposite
behaviour.

One thing that might be interesting would be to try porting gtk-doc over
to using Shaun McCance\'s new [XSLT
stylesheets](http://cvs.gnome.org/lxr/source/yelp/stylesheets/) (there
are [more details](http://www.gnome.org/~shaunm/yelp/speed) on his
website). If these are suitable, they could give a significant boost to
building API and user docs.
