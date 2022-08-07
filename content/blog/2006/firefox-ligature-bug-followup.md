---
title: 'Firefox Ligature Bug Followup'
slug: firefox-ligature-bug-followup
date: 2006-04-06T20:16:39+08:00
tags: ['Ubuntu']
---

Thought I\'d post a followup on my previous post since it generated a
bit of interest. First a quick summary:

-   It is not an Ubuntu Dapper specific bug. With the appropriate
    combination of fonts and pango versions, it will exhibit itself on
    other Pango-enabled Firefox builds (it was verified on the Fedora
    build too).
-   It is not a [DejaVu](http://dejavu.sourceforge.net/) bug, although
    it is one of the few fonts to exhibit the problem. The simple fact
    is that not many fonts provide ligature glyphs and include the
    required [OpenType](http://www.opentype.org/) tables for them to be
    used.
-   It isn\'t a [Pango](http://www.pango.org/) bug. The ligatures are
    handled correctly in normal GTK applications on Dapper. The bug only
    occurs with Pango \>= 1.12, but that is because older versions did
    not make use of the OpenType tables in the \"basic\" shaper (used
    for latin scripts like english).
-   The bug only occurs in the Pango backend, but then the non-Pango
    renderer doesn\'t even support ligatures. Furthermore, there are a
    number of languages that can\'t be displayed correctly with the
    non-Pango renderer so it is not very appealing.

The firefox bug is only triggered in the slow, manual glyph positioning
code path of the text renderer. This only gets invoked if you have
non-default letter or word spacing (such as justified text). In this
mode, the width of the normal glyph of the first character in the
ligature seems to be used for positioning which results in the
overlapping text.

It seems that the bug may be fixed in the Firefox 1.6 series, but if
that fix can\'t be backported easily in time for Dapper, it might be
easier to switch to a different default font that doesn\'t contain the
ligatures (such as Bitstream Vera). That would certainly reduce the
chance of the bug occurring.

---
### Comments:
#### [Joachim Breitner](http://www.joachim-breitner.de/) - <time datetime="2006-04-07 03:08:53">5 Apr, 2006</time>

Another observervation is that the bug also appears in the galeon
browser\...

BTW the word \"fix\" looks really cool this way\...

---
#### michele - <time datetime="2006-04-07 03:27:01">5 Apr, 2006</time>

Thanks for pointing this bug out James, I\'ve missed the your first
post, this was really bugging me.

Yep, the word \"fix\" looks cool but I prefer it now that I\'ve switched
to Bitstream Vera (thanks for providing a test case Joachim). :D

---
#### Denis Jacquerye - <time datetime="2006-04-10 08:45:25">1 Apr, 2006</time>

The ligatures could also be disabled in free fonts like DejaVu fonts in
distribs that display the bug. I think we even made such a release a few
months back because of this bug.

Bitstream Vera does contain the \'fi\' and \'fl\' ligatures but isn\'t
OpenType so Pango does not perform the substitutions. If Pango starts
doing so\...

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-04-10 19:02:49">1 Apr, 2006</time>

Denis: yeah, I noticed that the Vera font contained a few ligature
glyphs (although not as many as Deja Vu) while investigating the
problem, but did not have the OpenType tables necessary for them to be
used by Pango.

I\'d prefer not to modify the fonts directly, since it affects how
documents using that font display. It would be a lot nicer if the pango
rendering code in Firefox was fixed \...

---
