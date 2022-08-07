---
title: '13 September 2004'
slug: 13-september-2004
date: 2004-09-14T03:05:30+08:00
draft: false
tags: ['Gnome']
---

**Foundation Elections**

There has been talk on the foundation list about changing the vote
counting procedure to something more fair. The method being proposed is
[Single Transferable
Vote](http://en.wikipedia.org/wiki/Single_Transferable_Vote), which is
the same system used within a single electorate for the senate vote in
the [Australian Federal
Election](http://www.aec.gov.au/election2004/index.htm). As with the
Australian elections, some people have some trouble understanding
exactly how it works, so here is a description.

1.  Each voter orders every candidate on their ballot in order of
    preference. Each ballot is assigned a weight of 1.
2.  The ballots are grouped by the first preference.
3.  If any candidate\'s total reaches the quota, then they get in. The
    quota is chosen such that if there are *s* seats, then at most *s*
    candidates can reach the quota. So a candidate must get more than
    *n*/(*s* + 1) first preference votes in order to reach the quota.
4.  If any candidate gets over the quota, then the highest vote getter
    is elected, and their votes are redistributed at a reduced strength.
    If *x* people voted for the candidate, then the weighting of each of
    the votes is scaled by (*x* - *q*)/*x* where *q* is the quota (*x* -
    *q* is the number of votes over the quota). The winning candidate\'s
    name is removed from all ballots and we go back to step 2 and repeat
    to find the next winner.
5.  If no candidate reaches the quota, then the candidate with the least
    first preference votes is removed from the election. Their name is
    removed from all ballots, and we go back to step 2. The votes for
    the removed candidate are redistributed at the same strength, since
    they didn\'t help elect a candidate.

Note that this vote counting system is identical to [Instant-runoff
voting](http://en.wikipedia.org/wiki/Instant-runoff_voting) when there
is only a single seat. The quota calculation shows that the winning
candidate needs to get more than 50% of the votes to win, as expected.

Some of the nice properties of this system include:

-   If you vote for a losing candidate, your vote is transfered at the
    same strength, so is not wasted. This reduces the risk of voting for
    a candidate that is unlikely to win.
-   Voting for a popular candidate doesn\'t waste your vote. The portion
    of your vote that wasn\'t needed to elect the candidate is
    redistributed to the next preference. For example, if 50% of people
    vote for dcamp, but the quota is 10% of the votes, then all his
    votes will be redistributed to second preference at 80% strength.
-   If there are two similar candidates, they shouldn\'t split the vote
    in such a way that neither wins. If one candidate gets knocked out,
    their votes will transfer to the other.

There are some differences between what I described and what is used in
the Australian elections. This seems to be to make the process more
discrete and easier to count (mostly rounding the various quotas and
transfer values). For the foundation election though, I can\'t see any
reason not to use a more exact version.

**Zenity Notification Icon**

Yesterday Glynn posted about [notification icon support in
Zenity](http://www.gnome.org/~gman/blog/13092004). His current
implementation really only handles one-shot notifications, since the
icon disappears and zenity exits when you click the icon.

I talked with him on IRC about adding support for a different mode where
you send commands to zenity via stdin, similar to the [jhbuild
notification icon
prototype](http://www.livejournal.com/users/davyd/114890.html) Davyd
did. This would allow you to write bash scripts like this:

> `exec 3> >(zenity --notification) echo "icon: someicon" >&3 echo "tooltip: doing some important work" >&3 # do stuff echo "icon: someothericon" >&3 # do some more stuff exec 3>&-`

This could be very useful for many scripts in addition to jhbuild, which
is why I suggested adding it to zenity. Now it just needs implementing
\...
