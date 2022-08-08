---
title: 'Launchpad code scanned by Ohloh'
slug: launchpad-ohloh
date: 2009-10-27T16:48:18+08:00
tags: ['Bazaar', 'Launchpad', 'Ubuntu']
---

Today [Ohloh](http://www.ohloh.net/) finished importing the Launchpad
source code and produced the first [source code analysis
report](https://www.ohloh.net/p/launchpad/analyses/latest "Launchpad.net Code Analysis"). 
There seems to be something fishy about the reported line counts (e.g.
-3,291 lines of SQL), but the commit counts and contributor list look
about right.  If you\'re interested in what sort of effort goes into
producing an application like Launchpad, then it is worth a look.

---
### Comments:
#### *e* - <time datetime="2009-10-27 20:41:29">27 Oct, 2009</time>

Have you seen the perl language?

3 lines of code -\> 54 lines of comments :-D

---
#### [Andy Wingo](http://wingolog.org/) - <time datetime="2009-10-28 03:22:51">28 Oct, 2009</time>

It\'s a bit belated, but congrats, James, for getting all this code, you
and your colleagues\', out in the open. I\'m sure that was a relief :)

---
#### [Juanjo](http://rambleon.usebox.net/) - <time datetime="2009-10-28 05:41:44">28 Oct, 2009</time>

Interesting\... I wonder, those 3,291 lines of SQL, where did they go?

How awesome it\'s Launchpad that works without them :\'D

---
#### James Henstridge - <time datetime="2009-10-28 10:53:32">28 Oct, 2009</time>

\@Andy Wingo: thanks!

\@Juanjo: If you look at the report, you\'ll see that there is actually
2,610 lines of SQL code. The problem is the large negative amount of
comments and blanks that cancel it out.

On the other hand, Launchpad appears to have a negative amount of HTML
code which is not quite cancelled out by positive quantities of comments
and blanks.

---
