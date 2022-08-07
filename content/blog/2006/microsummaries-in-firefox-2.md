---
title: 'Microsummaries in Firefox 2'
slug: microsummaries-in-firefox-2
date: 2006-09-08T17:27:16+08:00
tags: ['Launchpad']
---

One of the new features in [Firefox
2](http://www.mozilla.org/projects/bonecho/) is
[Microsummaries](http://wiki.mozilla.org/Microsummaries), which
essentially allows dynamic bookmark titles. This is useful when
bookmarking volatile pages, since the title can reflect the current
state of the document rather than the state when the bookmark was
created.

The system works by registering XSLT transformations that generate a
simple text string from the page content. The registrations are either
done via a \<link\> element, or matched via regular expressions. The
system is designed to target users (who can register their own
microsummary generators), website owners (who can suggest a generator
through a \<link\> tag) and 3rd parties (who can provide generators for
other sites to users).

For [Launchpad](https://launchpad.net), I\'d fall into the second
category. It would be nice to provide microsummary generators for bug
pages, so you\'d get an indication of the status of the bug, plus an up
to date bug title. Now while all this information is available in the
page content, we can provide it in a much more efficient manner (if we
know the user is only interested in generating a microsummary, why send
them the 100 comments on the bug every time the bookmark title is to be
updated?).

Being able to specify a transformation for the bookmarked URL that would
be used instead for generating the summary would be one way of solving
this. This would reduce the bandwidth requirements and processing time
on our end. Another way would be for Firefox to include something in its
request that would allow a site to know that the page was being
retrieved for microsummary generation so it could ommit information.

Overall it looks like a useful feature, but I do wonder if it will
suffer from the \"RSS effect\" and cause lots of needless traffic to web
sites until people work out how to achieve the same effects in a less
resource intensive fashion.

---
### Comments:
#### xxx - <time datetime="2006-09-09 08:37:38">6 Sep, 2006</time>

It\'s pity one cannot specify separate microsummary page (like you RSS
channels - you don\'t create them using XSLT from the appropriate
page!), it would be very small compared with downloading each time the
page and then extracting microsummaries from it.

---
#### mk - <time datetime="2006-09-09 16:28:00">6 Sep, 2006</time>

I don\'t know, this sounds like a rather useless feature to me. Most of
the time, I give custom names to my bookmarks anyway; if they would
constantly change, how can I find something in this mess?

Thinking of bookmars, the first and most annoying thing which comes to
my mind is that Firefox doesn\'t natively support to store them on a
remote server and thus share them with other browser installations.

They should have focused on those features which increase, not decrease
usability\...

---
#### xxx - <time datetime="2006-09-09 23:35:39">6 Sep, 2006</time>

mk: well, it is because FF\'s concept of bookmark is somewhat broader
than the normal one. You can put \"bookmarks\" onto special toolbar and
here the microsummaries DO make sense. (It would however make even more
sense if one could put \"microsummaries\" - or even something like
\"nanosummaries\" or \"picosummaries\" on gnome-pannel for example;).

james henstridge: fortunatelly you don\'t have to use generators, you
can just create very simple (i.e. small) web page, that produces
one-line text/plain with a summary. (I\'ve implemented this on
<http://www.evangnet.cz/> and it works just fine).

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2006-09-11 11:21:04">1 Sep, 2006</time>

xxx: that\'s interesting. The spec on wiki.mozilla.org only mentions
using a \<link\> element to link to a microsummary generator.

If I can link directly to a microsummary, then that solves my problem.
I\'d feel safer if they included this feature in the spec though.

Thanks.

---
