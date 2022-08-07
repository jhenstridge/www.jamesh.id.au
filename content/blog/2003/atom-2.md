---
title: 'Atom'
slug: atom-2
date: 2003-11-03T16:27:51+08:00
tags: ['XML']
---

Have been playing round with
[Atom](http://www.intertwingly.net/wiki/pie/FrontPage), which looks like
a nicer form of RSS. Assuming your content is already in XHTML, it looks
a lot easier to generate an Atom file compared to an RSS file, because
the content can be embedded directly, rather than needing to be escaped
as character data. Similarly, an Atom file is easier to process using
standard XML tools compared to RSS because the document only needs to be
parsed once to get at the content (which is probably what you were after
anyway).

I decided to take a look at what would be necessary to get Advogato to
produce nice Atom feeds. One of the difficulties is that all the content
is stored in plain non XML compatible HTML. After a little bit of head
scratching I realised that libxml can already do this kind of
normalisation without much trouble as it already has an HTML parser that
produces a DOM tree compatible with its XML parser/dumper APIs.

I did some simple test programs in
[Python](http://www.daa.com.au/~james/files/normalise_html.py) and
[C](http://www.daa.com.au/~james/files/normalise_html.c). I wonder
whether code like this could be used directly in the diary posting code?
With some small extensions, it would be pretty easy to implement
tag/attribute sanitisation, and double new line to new paragraph
conversion (the current implementation of this is quite annoying \-- it
still adds extra \<p\> tags for new lines that are clearly outside of a
paragraph).
