---
title: 'Zeroconf Branch Sharing with Bazaar'
slug: bzr-avahi
date: 2008-02-19T16:36:43+09:00
tags: ['Avahi', 'Bazaar', 'Bonjour', 'Hackathon', 'Python', 'Sprint', 'Zeroconf']
---

{{< figure src="bazaar-logo.png" width="94" height="96" class="fl" >}}
At Canonical, one of the approaches taken to accelerate development is
to hold [coding
sprints](http://en.wikipedia.org/wiki/Hackathon#Sprints) (otherwise
known as hackathons, hackfests or similar). Certain things get done a
lot quicker face to face compared to mailing lists, IRC or VoIP.

When collaborating with someone at one of these sprints the usual way to
let others look at my work would be to commit the changes so that they
could be pulled or merged by others. With legacy version control systems
like CVS or Subversion, this would generally result in me uploading all
my changes to a server in another country only for them to be downloaded
back to the sprint location by others.

In contrast, with a modern VCS like [Bazaar](http://bazaar-vcs.org/) we
should be able to avoid this since the full history of the branch is
available locally -- enough information to let others pull or merge the
changes. That said, we\'ve often ended up using a server on the internet
to exchange changes despite this. This is the same work flow we use when
working from home, so I guess the pain of switching to a new work flow
outweighs the potential productivity gains.

**The Solution**

Bazaar makes it easy to run a read only server locally:

    bzr serve [--directory=DIR]

However, there is still the issue of others finding the branch. They\'d
need to know the IP address assigned to my computer at the sprint, and
the path to the branch on the server. Ideally they\'d just need to know
the name of the my branch. As it happens, we\'ve got the technology to
fix this.

{{< figure src="avahi-logo.png" width="90" height="67" class="fl" >}}
[Avahi](http://avahi.org/) makes it trivial to advertise and browse
for services on the local network without having to worry about what
IP addresses have been assigned or what people name their computer.
So the solution is to hook Avahi and Bazaar together. This was fairly
easy due to Avahi\'s DBus interface and the
[dbus-python](http://dbus.freedesktop.org/doc/dbus-python/) bindings.

The result is my [bzr-avahi
plugin](https://launchpad.net/bzr-avahi "Bazaar/Avahi mDNS Plugin"). You
can either [download
tarballs](https://launchpad.net/bzr-avahi/+download) or install the
latest version directly with from Bazaar:

    bzr branch lp:bzr-avahi ~/.bazaar/plugins/avahi

To use the plugin, you must have at least version 1.1 of Bazaar, the
Python bindings for DBus and Avahi, and a working Avahi setup. Once the
plugin is installed, it hooks into the standard \"`bzr serve`\" command
to do the following:

-   scan the directory being served for branches that the user has asked
    to advertise.
-   ask Avahi to advertise said branches

You can ask to advertise a branch using the new \"`bzr advertise`\"
command:

    bzr advertise [BRANCH-NAME]

If no name is specified, the branch\'s nickname is used. The advertise
command sends a signal over the session bus to tell any running servers
about the change, so there is no need to restart \"`bzr serve`\" to see
the change.

At this point, the advertised branches should be visible with a service
browser like avahi-discover, so that\'s half the problem solved. From
the client side two things are provided: a special redirecting transport
and a command to list all advertised branches on the local network.

The transport allows you to access the branch by its advertised name
with most Bazaar commands. For example, merging a branch is as simple
as:

    $ bzr merge local:BRANCH-NAME
    local:BRANCH-NAME is redirected to bzr://hostname.local:4155/path/to/branch
    ...
    All changes applied successfully.
    $

If you want to get a list of all advertised branches on the network, the
\"`bzr browse`\" command will print out a list of branch names and the
URLs they translate to.

I believe using these tools together should offer a low enough overhead
for direct sharing of branches at sprints that people would actually
bother using it. It should be quite useful at the next sprint I go to.

---
### Comments:
#### [Stuart Colville](http://muffinresearch.co.uk/) - <time datetime="2008-02-19 17:28:55">19 Feb, 2008</time>

This is such a brilliant way of taking full advantage of
de-centralisation and perfect for sharing branches between localised
teams. The only downside is that Avahi is Linux only and a cross
platform solution would be even better!

---
#### [Mathieu Cadet](http://athrun.myopenid.com/) - <time datetime="2008-02-19 19:15:07">19 Feb, 2008</time>

Woa! Just tested it. That\'s really awesome. Great job here!\
This should be included by default in bazaar.

---
#### James Henstridge - <time datetime="2008-02-19 19:29:59">19 Feb, 2008</time>

Stuart: Avahi is not Linux only, but I catch your meaning: this isn\'t
going to work with the mDNS responder on MacOS X, and Avahi has not been
ported to Windows.

As there is no standard mDNS API for Python, I programmed to the API of
the responder I could test things on. I am sure that the ideas from my
plugin could be used to write a similar plugin for Apple\'s Bonjour
client library, but I am not sure how much code it would share
(bzr-avahi is almost entirely glue code).

---
#### [Antono Vasiljev](http://antono.info/) - <time datetime="2008-02-19 20:19:17">19 Feb, 2008</time>

Awesome idea! I\'ll try to make something similar for git.

---
#### [Stuart Metcalfe](http://origa.me.uk/openid/) - <time datetime="2008-02-19 21:17:55">19 Feb, 2008</time>

This is an great use of Zeroconf - well done! It\'s worth noting that
Apple\'s mDNS responder has both Mac OSX and Windows versions which
share a common API.

---
