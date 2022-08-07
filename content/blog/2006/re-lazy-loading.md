---
title: 'Re: Lazy loading'
slug: re-lazy-loading
date: 2006-03-31T13:56:43+08:00
tags: ['Gnome', 'Python']
---

[Emmanuel:](http://log.emmanuelebassi.net/archives/2006/03/lazy-loading/)
if you are using a language like [Python](http://www.python.org/), you
can let the language keep track of your state machine for something like
that:

    def load_items(treeview, liststore, items):
        for obj in items:
            liststore.append((obj.get_foo(),
                              obj.get_bar(),
                              obj.get_baz()))
            yield True
        treeview.set_model(liststore)
        yield False

    def lazy_load_items(treeview, liststore, items):
        gobject.idle_add(load_items(treeview, liststore, item).next)

Here, `load_items()` is a generator that will iterate over a sequence
like `[True, True, ..., True, False]`. The `next()` method is used to
get the next value from the iterator. When used as an idle function
with this particular generator, it results in one item being added to
the list store per idle call til we get to the end of the generator
body where the \"`yield False`\" statement results in the idle
function being removed.

For a lot of algorithms, this removes the need to design and debug a
state machine equivalent. Of course, it is
[possible](http://www.chiark.greenend.org.uk/~sgtatham/coroutines.html)
to do similar things in C but that\'s even more obscure `:)`.

---
### Comments:
#### [Nikos Kouremenos](http://members.hellug.gr/nkour) - <time datetime="2006-03-31 23:12:02">5 Mar, 2006</time>

Yes this way of doing time-bound stuff, R O C K S

---
#### anonymous - <time datetime="2006-04-01 01:43:21">6 Apr, 2006</time>

I use that thechnique too, but if the obj.get\_\* functions in your
example are not too expensive, the call overhead really slows things
down. this can be fixed again by adding like 10 items or so in one go.
replace \"yield True\" with something like:\
i += 1\
if not i % 10:\
yield True\
and feel the difference.

---
