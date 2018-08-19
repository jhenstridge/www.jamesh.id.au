---
title: "Integrating SpamAssassin with Mailman"
date: 2003-04-14T00:00:00+08:00
draft: false
type: article
toc: true
---

If you run a moderately popular mailing list, you will have to address
the spam problem at some point.  Many spammers actively target mailing
lists, because if the spam doesn't get caught it will be forwarded to
many recipients.  The first step is usually to hold non-subscriber
posts for moderation.  This is good for the list users, but adds a
significant burden to the list administrators.  It also makes it
difficult to approve legitimate non-subscriber posts.

To handle this problem, I wrote some patches to integrate the
[SpamAssassin](http://www.spamassassin.org/) spam filtering software
with [Mailman](http://www.list.org/).  With this patch, the majority
of the spam sent to the list can be discarded without intervention by
the moderator.

For some lists, the filter may reduce spam enough that
non-subscriber posting can be turned back on.  For closed lists,
it will be easier to moderate, as there will be a higher signal to
noise ratio on the moderation screen, making it less likely that a
legitimate post will be discarded.

With the release of SpamAssassin 2.50, you can even customise
the filters on a per-mailing list basis through the use of
Bayesian analysis of messages.


## Installation

### Installing Mailman

It is assumed that you already have a copy of Mailman installed on
your system.  The current version of my patches are designed to work
with Mailman >= 2.1, so you should upgrade to 2.1.x if you haven't
already.

If you are using 2.1, you may want to upgrade to 2.1.1, as it fixes a
number of cross site scripting vulnerabilities.  New releases are
available from the [Mailman website](http://www.list.org/) or on
Sourceforge:

 * http://sourceforge.net/project/showfiles.php?group_id=103

Consult the documentation included in the source tarball for
instructions on building and installing Mailman.


### Installing SpamAssassin

SpamAssassin is available from the [SpamAssassin
website](http://www.spamassassin.org/).  Follow the installation
instructions included in the tarball, or just install the RPMs (or
rebuild the SRPM first).

You should install SpamAssassin >= 2.50, but more recent versions are
preferable.


### Configuring spamd

The Mailman patches make use of the <tt>spamd</tt> daemon included in
SpamAssassin, so it will be necessary to configure it to run at
startup.

First create a new user account to run spamd as.  The home directory
for the user should be set to something like `/var/lib/spamassassin`.
On most Linux distros, this can be done with the following
command:

    mkdir /var/lib/spamassassin
    useradd -r -d /var/lib/spamassassin -M -s /sbin/nologin \
        -c 'SpamAssassin' spamassassin
    chown spamassassin.spamassassin /var/lib/spamassassin

The exact details will depend on your OS.  We need to pass a
number of arguments to spamd to get it to run in a locked down
mode.  The arguments I use are:

    spamd -d -u spamassassin -x -a -P --virtual-config-dir=/var/lib/spamassassin/%u.prefs

These meanings of these arguments are:

`-d`
: fork spamd on startup

`-u spamassassin`
: run as the `spamassassin` user account.

`-x`
: don't create `user_prefs` files for individual users

`-a`
: create automatic whitelists, to smooth out the scores that
  individuals receive.

`-P`
: paranoid mode

`--virtual-config-dir=/var/lib/spamassassin/%u.prefs`
: create per-user configuration directories under the `spamassassin`
  user's home directory.  This way we can maintain separate automatic
  whitelists and Bayes databases for each mailing list.


If you are using the RPMs, you can put these options in a
`/etc/sysconfig/spamd` file so that they will be passed to spamd when
it is started:

    # Options to spamd
    OPTIONS="-d -u spamassassin -x -a -P --virtual-config-dir=/var/lib/spamassassin/%u.prefs"

    # don't bother with UTF-8 mode
    export LANG=en_AU

Next, you will want to set up your init scripts to start `spamd` when
your system starts up.  If you are using the RPMs, this is trivial:

    chkconfig --level 345 spamassassin on
    service spamassassin start


### Adding the SpamAssassin Filter to Mailman

First you will need to download the filter, which is comprised of the
following two files:

* [spamd.py](spamd.py) (updated 6-June-2003)
* [SpamAssassin.py](SpamAssassin.py) (updated 14-April-2003)

Both files should be installed into the `Mailman/Handlers/`
subdirectory under the Mailman install directory.  You will then need
to edit the `Mailman/mm_cfg.py` file to enable the filter:

    GLOBAL_PIPELINE.insert(1, 'SpamAssassin')

After making the changes to `Mailman/mm_cfg.py`, you will need to
restart the `qrunner` process.  This can be achieved with the
mailmanctl program:

    mailmanctl restart

At this point, the SpamAssassin filter should operational.


## Configuration

With the mailman filter in place, every incoming message will be
passed off to SpamAssassin's `spamd` daemon for scoring.  The mailing
list name will be sent as the user name.  This allows us to maintain
separate SpamAssassin data files for each list.

After scoring, a message can be discarded if the score is over a
certain threshold (defaulting to 10), or held for moderation if it the
score is over another threshold (defaulting to 5).  Additionally, a
"bonus" can be subtracted from the scores of messages sent by list
subscribers (defaulting to 2) to reduce the chance that subscriber
posts are held or discarded.

These settings can be tuned by editing the `Mailman/mm_cfg.py` file
and adding the following variables:

`SPAMASSASSIN_HOST`
: The host spamd is running on.  A string in *hostname:port* format.

`SPAMASSASSIN_DISCARD_SCORE`
: If a message receives a score above this limit, the message will be
  discarded without moderation.  The default value for this variable
  is 10.

`SPAMASSASSIN_HOLD_SCORE`
: If a message receives a score above this limit, the message will be
  held for moderation.  The default value for this variable is 5.

`SPAMASSASSIN_MEMBER_BONUS`
: If the message was sent by a member of the list, an adjustment can
  be performed on the score.  This makes it less likely that a message
  claiming to come from a list member will be held for moderation.
  The default value for this variable is 2.

As before, you will need to restart `qrunner` with `mailmanctl` after
modifying the config file.

For the PyGTK mailing list, I use a discard score of 7.5 and a hold
score of 5.


## Feeding the Bayes Database

By itself, SpamAssassin will filter the majority of spam directed at
the lists.  For better results, you should look at seeding the Bayes
database for your list.  This will customise the filter based on
traffic to your list, which makes it more difficult for spammers to
produce messages that get through.  In turn, the amount of
administration required for the list will be reduced.

To seed the Bayes database, you will need to feed it a corpus of spam
and a corpus of "ham" (non-spam).  This is used to help it
differentiate spam from normal list postings.  It is a good idea to
use recent messages if possible, as they will better reflect the
typical list traffic.

If you run a closed list, your list archives should make a pretty good
"ham" corpus.  Simply trim a few months off the bottom of the archive
mbox (found in `archives/private/listname.mbox`), and pass them
to `sa-learn`:

    HOME=/var/lib/spamassassin/<i>listname</i>.prefs \
      sa-learn --showdots --ham --mbox filename.mbox

If you don't have a collection of recent spam messages, an
other option is to train the database on messages that get held in
the moderation queue.  To help with this, I wrote a small script
called [`mmlearn`](mmlearn).  After removing all
legitimate messages from the moderation queue, you can run it on
the remaining spam:

    mmlearn <i>listname</i>

Training the filter based on false negatives is a fairly effective way
of improving the filter.


## The Future

In the future, it would be nice to add support for passing messages to
the Bayes database directly from the moderation web page.  I am not
sure how hard it would be to implement this.
