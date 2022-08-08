---
title: '17 February 2004'
slug: 17-february-2004
date: 2004-02-18T01:24:20+08:00
tags: ['JHBuild']
---

**Weather**

It has been really hot and humid here for the past few days. While it is
not uncommon to have hot weather in Perth, high humidity is quite
unusual. It seems to be due to the floods up in the north of the state
(they had a report on the news about an 18 person town that had been
without a pub for 3 days).

There was a big thunder storm last night, so hopefully things will get
back to normal. Unfortunately, it is still quite hot (9:20am at the
moment, and its 33°C with 62% relative humidity) and there has been an
order preventing people from using air conditioners due to supply
problems at the power company.

On another note, if you are using [Gnome
2.5.x](http://www.gnome.org/start/2.5/), the weather applet will now
display forecasts for most of the Australian locations, downloaded from
[BOM](http://www.bom.gov.au/). You can also get it to display a radar
image by manually entering in the URL in the preferences (the one for
Perth is [here](http://mirror.bom.gov.au/radar/IDR123.gif)).

**jhbuild**

jhbuild now does syntax highlighting of cvs output. In particular, it
will display conflicts in red. It also repeats the list of conflicts
when the checkout is complete (a useful idea I stole from Mozilla\'s
`client.mk`), which is very useful for large modules when you have
modified a few files.

To get CVS to output in line buffered mode while passing its output to
me, I needed to use a pseudo terminal, at which point I found a few bugs
and annoyances in the Python standard library `pty.spawn` function:

1.  It leaks the pty master fd on each run.
2.  It doesn\'t return the exit status of the child.
3.  It doesn\'t provide a way to stick the pty connection into
    non-blocking mode, which is needed if you want to read lines from
    the child as they are produced.

I reported it as [bug 897935](http://www.python.org/sf/897935), so
hopefully it will be fixed in a future version. For now, I have my own
private copy of the function.
