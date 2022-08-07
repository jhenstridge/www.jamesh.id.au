---
title: 'Running Valgrind on Python Extensions'
slug: python-valgrind
date: 2008-03-24T08:47:29+09:00
tags: ['Python', 'Valgrind']
---

As most developers know, [Valgrind](http://www.valgrind.org/) is an
invaluable tool for finding memory leaks. However, when debugging
[Python](http://www.python.org/) programs the pymalloc allocator gets in
the way.

There is a [Valgrind suppression file distributed with
Python](http://svn.python.org/projects/python/trunk/Misc/valgrind-python.supp)
that gets rid of most of the false positives, but does not give
particularly good diagnostics for memory allocated through pymalloc. To
properly analyse leaks, you often need to recompile Python with
pymalloc.

As I don\'t like having to recompile Python I took a look at Valgrind\'s
client API, which provides a way for a program to detect whether it is
running under Valgrind. Using the client API I was able to put together
a patch that automatically disables pymalloc when appropriate. It can be
found attached to [bug 2422](http://bugs.python.org/issue2422) in the
Python bug tracker.

The patch still needs a bit of work before it will be mergeable with
Python 2.6/3.0 (mainly autoconf foo).  I also need to do a bit more
benchmarking on the patch.  If the overhead of turning on this patch is
negligible, then it\'d be pretty cool to have it enabled by default when
Valgrind is available.

---
### Comments:
#### [Jelmer Vernooij](http://samba.org/~jelmer/) - <time datetime="2008-03-26 23:47:54">3 Mar, 2008</time>

Thanks for this! I can\'t remember how many times I\'ve run valgrind on
python only to find out I forgot to supply the suppressions file.

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-03-27 13:43:16">4 Mar, 2008</time>

Note that even with the suppressions file in effect, Valgrind will miss
many leaks if pymalloc is active. The only difference is that you won\'t
see the uninitialised read warnings that pymalloc generates.

If you allocate a block with pymalloc, it will be carved out of a larger
allocation. If you forget to free that memory, Valgrind doesn\'t notice
because it is only tracking the larger block that pymalloc allocated
(which is properly referenced by pymalloc internals).

By bypassing the pymalloc code, each of the allocations is tracked
separately by Valgrind and the leak is evident. An alternative approach
to the problem would have been to annotate the pymalloc code with
Valgrind\'s memory pools client API so that it knows what Python thinks
is going on inside the larger blocks it allocates. This is a fair bit
more work, and I don\'t know if it is worth the effort (it\'d probably
be useful for debugging pymalloc itself though).

---
