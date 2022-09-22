---
title: '21 December 2001'
slug: 21-december-2001
date: 2001-12-22T00:24:31+08:00
---

I was updating my documentation generator for pygtk (the
one that tries to make the C reference docs for GTK look
like docs for Python). It was taking a while to process
with db2html (which uses Jade to convert from SGML to HTML),
so I thought I would look at using DocBook/XML and
[DV](http://www.advogato.org/person/DV/)\'s xsltproc, which I had heard
ran a lot
quicker.

Unlike other people\'s experiences, the docs ended up
taking over twice as long to process with xsltproc compared
to jade! I suppose this was to do with the size (about
1.9MB of of XML source), and the number of cross references
(the doc generation script added a lot of xrefs). On other
docs I tried, xsltproc seemed noticably better.

I also found out that White Christmas made with coco pops
tastes pretty good.
