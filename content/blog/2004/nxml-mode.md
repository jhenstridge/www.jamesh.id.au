---
title: 'nxml-mode'
slug: nxml-mode
date: 2004-05-04T09:30:36+08:00
draft: false
tags: ['XML']
---

Started playing with
[nxml-mode](http://www.thaiopensource.com/download/), which makes
editing XML much nicer in emacs (psgml-1.3 does an okay job, but the
indenter and tag closer sometimes get confused by empty elements). There
is a [nice article about
nxml-mode](http://www.xmlhack.com/read.php?item=2061) on xmlhack which
gives an introduction to the mode.

The first thing that struck me about nxml in comparison to psgml was the
lack of syntax highlighting. It turned out that the reason for this was
that colours were only specified for the light background case, and I
was using a dark background. After setting the colours appropriately
(customise faces matching the regexp `^nxml-`), I could see that the
highlighting was a lot better than what psgml did.

One of the big differences between nxml and psgml is that it uses
[RELAX-NG](http://www.relaxng.org/) schemas rather than DTDs. It comes
with schemas for most of the common formats I want to edit (xhtml,
docbook, etc), but I also wanted to edit documents in a few custom
formats (the module description files I use for jhbuild being a big
one).

Writing RELAX-NG schemas in the compact syntax is very easy to do ([the
tutorial](http://relaxng.org/compact-tutorial-20030326.html) helps a
lot). I especially like the interleave feature, since it makes certain
constraints much easier to express (in a lot of cases, your code
doesn\'t care what order the child elements occur in, as long as
particular ones appear). While it is possible to express the same
constraint without the interleave operator, you end up with a
combinatorial explosion (I guess that\'s why XML Schema people don\'t
like RELAX-NG people making use of it). For example, `A & B & C` would
need to be expressed as:

> `(A, B, C) | (A, C, B) | (B, A, C) | (B, C, A) | (C, A, B) | (C, B, A)`

(for *n* interleaved items, you\'d end up with *n!* groups in the
resulting pattern).

After writing a schema, it was a simple matter of dropping a
[`schemas.xml`](http://cvs.gnome.org/viewcvs/jhbuild/modulesets/schemas.xml?view=auto)
file in the same directory as my XML documents to associate the schema
with the documents. This is required because RELAX-NG doesn\'t specify a
way to associate a schema with a document, so nxml has its own method.
Matching rules can be based on file extensions, document element names,
XML namespaces or public IDs, but I used the document element name for
simplicity. You can specify other locations for schema locator rules,
but putting it in the same directory is the easiest with multiple
developers.

Once that is done, you get background revalidation of the document, and
highlighting of invalid portions of the document (something that psgml
doesn\'t seem to be able to do). It also says whether the document is
valid or not in the modeline, which is helpful when editing documents.

Now all we need is for [libxml2](http://www.xmlsoft.org/) to be able to
parse RELAX-NG compact syntax schemas \...
