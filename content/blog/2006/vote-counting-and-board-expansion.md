---
title: 'Vote Counting and Board Expansion'
slug: vote-counting-and-board-expansion
date: 2006-06-06T19:51:06+08:00
tags: ['Gnome']
---

Recently one of the [Gnome Foundation](http://foundation.gnome.org/)
directors
[quit](http://tieguy.org/blog/2006/06/01/resigning-from-the-board/), and
there has been a proposal to [expand the board by 2
members](http://mail.gnome.org/archives/foundation-list/2006-June/msg00042.html).
In both cases, the proposed new members have been taken from the [list
of
candidates](http://foundation.gnome.org/vote/results.php?election_id=2)
who did not get seats in the last election from highest vote getter
down.

While at first this sounds sensible, the voting system we use doesn\'t
provide a way of finding out who would have been selected for the board
if a particular candidate was removed from the ballot.

The current voting system gives each foundation member N votes to assign
to N candidates (where N is the number of seats on the board). The votes
are then tallied for each candidate, and the N candidates with the most
votes get the seats.

If we look at last year\'s results, there were 119 people who voted for
Luis. If Luis had not been a candidate, then those 119 people would have
used that vote to pick other candidates. The difference in the number of
votes received by Vincent (the board member receiving the least votes)
and Quim (the unsuccessful candidate with the most votes) was just 16,
so those extra 119 votes could easily have affected the ordering of the
remaining candidates.

Furthermore, if the election was for nine seats rather than seven then
each foundation member would have had an additional two votes to cast.

This particular problem would not be an issue with a preferential voting
system where each foundation member lists all the candidates in their
order of preference. If a board member drops out, it is trivial to
recalculate the results with that candidate removed: the relative
orderings of the other candidates on the ballot are preserved. It is
also possible to calculate the results for a larger number of seats.

Of course, all the candidates from the last election would make great
board members so it isn\'t so much of an issue in this case, but it
might be worth considering for next time.

---
### Comments:
#### [Dave neary](http://blogs.gnome.org/bolsh) - <time datetime="2006-06-07 02:33:39">7 Jun, 2006</time>


Hi jamesh,

I actually don\'t like the system \"N votes for N seats\" - it seems
much better to have M votes for N seats, where M \< N - perhaps much
smaller.

Think in terms of preferences - say there are 5 candidates and 3 seats.
You may have 2 candidates you like a lot, and no clear preference for
the other 3 - your 3rd preference gets as much weight as your first two.
If you give everyone fewer choices, then you only get people voting for
the candidates they\'re passionate about - imagine how the election
might have turned out if everyone had only 3 votes for 7 seats. All
totals would have been a lot lower, but we would not have people getting
\"meh\" votes.

STV would work well, IMHO, if we could automate counting properly. And
if we Aussies and Irish could explain it to all the list-voters and
first past the posters :) But in the absence of STV, it seems better to
limit the number of ballots people have to ensure that we get people
voting for the candidates they really like.

---
#### [Quim](http://desdeamericaconamor.org) - <time datetime="2006-06-07 10:04:26">7 Jun, 2006</time>

It\'s easy to end up in endless debates about ways of voting (this
proposal has been half-discussed before).

Instead, we could:

a\) Make sure that there is an interest leaving behing the current
system

b\) ask for alternatives i.e.
<http://en.wikipedia.org/wiki/Instant-runoff_voting>

c\) in case we get more than one alternative, discuss and choose the
right one, based not only on theory but also in practical terms i.e.
free software available, functional and stable.

---
#### James Henstridge - <time datetime="2006-06-07 12:41:05">7 Jun, 2006</time>

David: reducing the number of votes each member gets while keeping the
same voting system would only exacerbate the problem of picking a
replacement when a board member resigns.

When Luis resigned, I effectively lost one seventh of my vote. If I had
less votes to cast, then I\'d have lost even more of my vote.

Quim: you are right. I should get off my arse and follow through about
this.

---
#### mdgeorge - <time datetime="2006-06-08 03:38:41">8 Jun, 2006</time>

You might be interested in the condorcet internet voting service:
<http://www.cs.cornell.edu/andru/civs.html>

---
#### Anonymous - <time datetime="2006-06-09 13:23:24">9 Jun, 2006</time>

Quim: Please don\'t recommend instant runoff voting; it has many
undesirable properties compared to even plain plurality voting, let
alone a full preferential system such as Condorcet.

Regarding availability of software, you might consider looking into
Devotee, the Debian Vote Engine. It supports electronic voting based on
GPG-signed emails, and excellent generation of reports afterward. I
don\'t know if it supports multiple-winner elections, but if not, I
suspect support for such would not prove incredibly difficult to add;
the well-thought-out design makes development quite straightforward.

---
