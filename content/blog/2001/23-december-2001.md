---
title: '23 December 2001'
slug: 23-december-2001
date: 2001-12-23T10:38:17+08:00
---

More investigation of the slow processing speed for my\
document. It seems like the slowdown is somewhere in\
libxslt\'s chunking code.

With chunking turned on, xsltproc took 4 minutes to\
process the document, while without chunking (ie. producing\
one large file), it only took 1:30 minutes (less than half\
the processing time).

In comparison, using Jade to process the document took\
about 2 minutes with chunking turned on. With chunking\
turned off, it took 4 minutes.

I wonder if this means that xsltproc\'s performance with\
chunking turned on can be improved to be faster than its\
nochunks performance? Either that, or the DSSSL stylesheets\
for Jade can be optimised for the non chunked case `:-)`
