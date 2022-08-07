---
title: 'XSLT'
slug: xslt
date: 2002-06-02T16:31:24+08:00
---

Been playing with XSLT a bit recently. It is quite a\
nice transformation language. I have been porting the [gtk-doc\
DocBook -\> HTML conversion
program](http://mail.gnome.org/archives/gtk-doc-list/2002-June/msg00002.html)
to use xsltproc (with\
a customisation layer over Norman Walsh\'s XSL stylesheets),\
rather than Jade (with a customisation layer over his DSSSL\
stylesheets). Took a little while to learn what I needed,\
but the end result looked fairly elegant.

While working on the customisation layer, I even found a\
simple
[bug](http://sourceforge.net/tracker/index.php?func=detail&aid=563473&group_id=21935&atid=373747)\
in the base stylesheets.
