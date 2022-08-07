---
title: 'Transaction Management in Django'
slug: transaction-management-in-django
date: 2008-09-01T15:42:39+08:00
tags: ['Django', 'Python', 'Storm']
---

In [my previous post about Django](using-storm-with-django.md), I
mentioned that I found the transaction handling strategy in
[Django](http://www.djangoproject.com/) to be a bit surprising.

Like most [object relational
mappers](http://en.wikipedia.org/wiki/Object-relational_mapping), it
caches information retrieved from the database, since you don\'t want to
be constantly issuing SELECT queries for every attribute access.
However, it defaults to commiting after saving changes to each object.
So a single web request might end up issuing many transactions:

|                  |               |
| -----------------|---------------|
| Change object 1  |Transaction 1  |
| Change object 2  |Transaction 2  |
| Change object 3  |Transaction 3  |
| Change object 4  |Transaction 4  |
| Change object 5  |Transaction 5  |

Unless no one else is accessing the database, there is a chance that
other users could modify objects that the ORM has cached over the
transaction boundaries. This also makes it difficult to test your
application in any meaningful way, since it is hard to predict what
changes will occur at those points. Django does provide a few ways to
provide better transactional behaviour.

**The \@commit\_on\_success Decorator**

The first is a decorator that turns on manual transaction management for
the duration of the function and does a commit or rollback when it
completes depending on whether an exception was raised. In the above
example, if the middle three operations were made inside a
`@commit_on_success` function, it would look something like this:

Change object 1

Transaction 1

Change object 2

Transaction 2

Change object 3

Change object 4

Change object 5

Transaction 3

Note that the decorator is usually used on view functions, so it will
usually cover most of the request. That said, there are a number of
cases where extra work might be done outside of the function. Some
examples include work done in middleware classes and views that call
other view functions.

**The TransactionMiddleware class**

Another alternative is to install the `TransactionMiddleware` middleware
class for the site. This turns on transaction management for the
duration of each request, similar to what you\'d see with other
frameworks giving results something like this:

Change object 1

Transaction 1

Change object 2

Change object 3

Change object 4

Change object 5

**Combining \@commit\_on\_success and TransactionMiddleware**

At first, it would appear that these two approaches cover pretty much
everything you\'d want. But there are problems when you combine the two.
If we use the `@commit_on_success` decorator as before and
`TransactionMiddleware`, we get the following set of transactions:

Change object 1

Transaction 1

Change object 2

Change object 3

Change object 4

Change object 5

Transaction 2

The transaction for the `@commit_on_success` function has extended to
cover the operations made before hand. This also means that operations
\#1 and \#5 are now in separate transactions despite the use of
`TransactionMiddleware`. The problem also occurs with nested use of
`@commit_on_success`, as reported in [Django bug
2227](http://code.djangoproject.com/ticket/2227).

A better behaviour for nested transaction management would be something
like this:

1.  On success, do nothing. The changes will be committed by the outside
    caller.
2.  On failure, do not abort the transaction, but instead mark it as
    uncommittable. This would have similar semantics to the Zope
    `transaction.doom()` function.

It is important that the nested call does not abort the transaction
because that would cause a new transaction to be started by subsequent
code: that should be left to the code that began the transaction.

**The \@autocommit decorator**

While the above interaction looks like a simple bug, the `@autocommit`
decorator is another matter. It turns autocommit on for the duration of
a function call, no matter what the transaction mode for the caller was.
If we took the original example and wrapped the middle three operations
with `@autocommit` and used `TransactionMiddleware`, we\'d get 4
transactions: one for the first two operations, then one for each of the
remaining operations.

I can\'t think of a situation where it would make sense to use, and
wonder if it was just added for completeness.

**Conclusion**

While the nesting bugs remain, my recommendation would be to go for the
`TransactionMiddleware` and avoid use of the decorators (both in your
own code and third party components). If you are writing reusable code
that requires transactions, it is probably better to assert that
`django.db.transaction.is_managed()` is true so that you get a failure
for improperly configured systems while not introducing unwanted
transaction boundaries.

For the [Storm](http://storm.canonical.com/) integration work I\'m
doing, I\'ve set it to use managed transaction mode to avoid most of the
unwanted commits, but it still falls prey to the extra commits when
using the decorators. So I guess inspecting the code is still necessary.
If anyone has other tips, I\'d be glad to hear them.

---
### Comments:
#### Bob Haugen - <time datetime="2008-09-08 13:16:58">1 Sep, 2008</time>

What (if anything) do you think is wrong with Django\'s
\@transaction.commit\_manually decorator?

If anything, would you please post a sample of the code you use to wrap
transactions for managed transaction mode?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2008-09-08 15:57:40">1 Sep, 2008</time>

The problem is with
enter\_transaction\_managemnt/leave\_transaction\_management nesting
rather than with the individual decorators or the middleware class.

My contention is that if you\'re in managed transaction mode and call
enter\_transaction\_management(), it should not be possible to end the
transaction until after calling leave\_transaction\_management() since
doing so will split the transaction that was being managed. So
\@commit\_manually has the same problems as the other decorators.

Concentrating on the database side of things, an equivalent of Zope\'s
transaction.doom() might be enough. If you\'ve got code that has side
effects outside of the database transaction, you need a way for that
code to participate in the transaction commit/rollback (one example is
sending out an email related to some DB changes). At that point you\'ve
essentially got Zope\'s transaction manager and may as well reuse that
code directly.

---
