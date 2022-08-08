---
title: '14 February 2002'
slug: 14-february-2002
date: 2002-02-14T15:23:05+08:00
---

**linux.conf.au**

Went to [linux.conf.au](http://linux.conf.au/)\
in Brisbane last week, which was a lot of fun. I went a few\
days early to see what was going on at the debian mini\
conference, and got roped into giving a small demonstration\
of gnome 2.0 stuff at about 30 seconds notice. I am not\
very good at doing presentations with no preparation `:(`

Met up with [gman](http://www.advogato.org/person/gman/), who was at
the\
conference as part of his holiday over here. The talks were\
very interesting. Sounds like Samba 3.0 will rock (does\
win2k domain client RPCs), and it may not take long after\
that to become a win2k PDC.

On the last day, among other things, I went to the\
Portable.NET work in process talk. The guy giving it seemed\
really bitter about Mono. He didn\'t seem to be giving any\
real reasons for it, but didn\'t give any real reasons for it.

Looks like the next linux.conf.au is going to be in\
Perth, so I hope everyone is going to turn up `:)`.\
Part of what got us the conference was the
[video](http://www.planetmirror.com/pub/lca/2003/movie/)\
some of the PLUG guys did. They showed the video at the end\
of the conference, and it was very good.

**Gnome 2.0**

While at l.c.a, I put out another release of devel\
libglade. This one just stripped out some of the unused\
functions from the module API (which isn\'t used by any\
applications). I also went through and updated a lot of the\
docs. The tutorial section has been updated a lot, and so\
has the API reference section. I started filling out a\
third section of the manual on the actual file format, but\
that isn\'t finished.

**Gnome in the Past**

While talking about the difference between the old gnome\
window hints and the newer window manager spec\
(collaborative effort with KDE and many window manager\
authors). One thing that came up was the colour reactive\
GUI crack in the old spec. I pulled up a few related links\
from the bowels of time:

-   [Bowie\'s\
    original
    proposal](http://mail.gnome.org/archives/gnome-gui-list/1998-May/msg00036.html)
-   [Slashdot\
    story about the
    proposal](http://slashdot.org/article.pl?sid=older/9804200911240&mode=thread)
-   [Slashdot\
    story about the implementation in
    GNOME](http://slashdot.org/article.pl?sid=older/9805311621222&mode=thread)

On one hand, the new API got in a lot quicker than it\
would these days. On the other, it would have taken a lot\
longer to get rid of this kind of crach these days\
(deprecating it for the duration of a major release, etc).\
Maybe I should resurrect GnomeLamp as a bonobo control\
example for gnome-python `:)`
