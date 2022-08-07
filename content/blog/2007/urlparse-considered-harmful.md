---
title: 'urlparse considered harmful'
slug: urlparse-considered-harmful
date: 2007-12-10T15:57:20+09:00
tags: ['Python']
---

Over the weekend, I spent a number of hours tracking down a bug caused
by the cache in the Python [`urlparse`
module](http://docs.python.org/lib/module-urlparse.html). The problem
has already been reported as [Python bug
1313119](http://bugs.python.org/issue1313119), but has not been fixed
yet.

First a bit of background. The `urlparse` module does what you\'d expect
and parses a URL into its components:

    >>> from urlparse import urlparse
    >>> urlparse('http://www.gnome.org/')
    ('http', 'www.gnome.org', '/', '', '', '')

As well as accepting byte strings (which you\'d be using at the HTTP
protocol level), it also accepts Unicode strings (which you\'d be using
at the HTML or XML content level):

    >>> urlparse(u'http://www.ubuntu.com/')
    (u'http', u'www.ubuntu.com', u'/', '', '', '')

As the result is immutable, `urlparse` implements a cache of up to 20
previous results. Unfortunately, the cache does not distinguish between
byte strings and Unicode strings, so parsing a byte string may return
unicode components if the result is in the cache:

    >>> urlparse('http://www.ubuntu.com/')
    (u'http', u'www.ubuntu.com', u'/', '', '', '')

When you combine this with Python\'s automatic promotion of byte strings
to unicode when concatenating with a unicode string, can really screw
things up when you do want to work with byte strings. If you hit such a
problem, the code may all look correct but the problem was introduced 20
`urlparse` calls ago. Even if your own code never passes in Unicode
strings, one of the libraries you use might be doing so.

The problem affects more than just the `urlparse` function. The
`urljoin` function from the same module is also affected since it uses
`urlparse` internally:

    >>> from urlparse import urljoin
    >>> urljoin('http://www.ubuntu.com/', '/news')
    u'http://www.ubuntu.com/news'

It seems safest to avoid the module all together if possible, or at
least until the underlying bug is fixed.

---
### Comments:
#### [fraggle](http://www.soulsphere.org/) - <time datetime="2007-12-10 17:29:11">1 Dec, 2007</time>

Looks like a classic case of \"optimisation is the root of all evil\".

---
#### ignacio - <time datetime="2007-12-10 18:50:25">1 Dec, 2007</time>

Or you could consistently use unicode internally.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-12-10 19:48:00">1 Dec, 2007</time>

ignacio: Not everything is defined in terms of unicode. The example I
gave above is the HTTP protocol, which is defined in terms of octets
(bytes) and uses URLs.

If I am processing a redirect in an HTTP client library, I probably want
to stay at the bytes level when constructing the new destination URL.

When processing the data from the HTTP response, I probably will convert
it to unicode while parsing HTML or XML. I\'ll probably need to do some
URL processing there as well.

So I have URL processing at two levels of code. If they happen to
process the same URL, I may end up with my HTTP requests getting
automatically promoted to unicode some of the time.

---
#### [Armin Ronacher](http://lucumr.pocoo.org/) - <time datetime="2007-12-10 22:13:04">1 Dec, 2007</time>

Hoi. As URLs are encodingless you cannot use unicode objects on those.
So \*always\* encode into a charset before using it. If you are passing
unicode objects to it, you\'re doing something wrong.

(Except of unicode strings just containing ASCII data which are coerced
to bytestrings automatically)

The solution is called IRI btw and not that supported so far.

Regards,\
Armin

---
#### Stoffe - <time datetime="2007-12-11 21:43:24">2 Dec, 2007</time>

No Armin, that\'s looking at it from the wrong way (or making an
unnecessary apology for the library). It shouldn\'t be a problem to use
unicode to just parse an url and get it back in unicode strings, as that
may be what you want in HTML/XML and well just about any normal text.
Encoding changes with purpose and URLs are of course always encoded in
the same encoding as the surrounding document\...

The bug is that there is a difference and the library does not take that
in account, returning the wrong cache result. Think hash collision.

If it was a PEBKAC error (it\'s not) it would still be a pretty poor
library that accepted faulty input and silently produced unexpected,
incorrect results. Now it is not a poor library, just one with an
unfortunate bug that should be fixed.

---
#### Gavin Panella - <time datetime="2007-12-15 17:43:36">6 Dec, 2007</time>

James, do you know of an instance where the cache is actually worth it?
Timings for me were \~3.5usec to urlparse the url for this page, with
cache, and 9usec with the caching code removed. It\'s still quick. I
can\'t think of any situation that would need those extra few usecs, but
people who do need to shave them can do caching themselves (and thus be
more efficient with a cache that\'s closer to their code, and needs).

Side-effects like this can be bad news, especially when they\'re
undocumented. I would argue that this cache probably shouldn\'t be in
the standard library.

Someone else (in a thread far far away that you\'ve probably already
read) said that this is fixed in Python now:
http://bugs.python.org/issue1313119. The caching code is still there,
but now it\'s keyed with a 5-tuple, having added the types of url and
scheme to the 3-tuple from before.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2007-12-17 14:38:21">1 Dec, 2007</time>

Gavin: yeah, I saw that. I was going to post a followup on that bug
report but could not recover the password on my account :( An account
was created for me as part of the migration from SourceForge, but it
seems that the password reset emails are getting eaten somewhere.

As for the reasons for the cache, perhaps it\'d be worth checking the
history of the module to see when it was implemented.

---
