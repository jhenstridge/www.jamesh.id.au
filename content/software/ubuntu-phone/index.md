---
title: "Ubuntu Phone and Unity"
date: 2017-04-05T00:00:00+08:00
tags: ["ubuntu"]
---

At the end of 2012, I moved from Ubuntu One to the Unity API Team at
Canonical.  This team was responsible for various services that
supported the Unity desktop shell: most noticeably the search
functionality.  This work initially focused on the Unity 7 desktop
shipping with Ubuntu, but then changed focus to the Unity 8 rewrite
used by the Ubuntu Phone project.

<!--more-->

## Scopes

The Unity dash was driven by search plugins known as "scopes".  For
Unity 7, the scopes framework and the majority of scopes themselves
were written in Vala.  For the Unity 8, a new version of the framework
was written in C++ that simplified parts of the data model and added
features to support the phone's user interface.

With the rest of the team, I helped maintain the set of core scopes
and provided support for third party scope developers.  This support
included developing a package that allowed people to write scopes in
the [Go programming language](https://golang.org/).

## Media Scanner

On the desktop, the music scope relied on the song index created by
the media player (either Rhythmbox or Banshee).  We didn't have
anything equivalent on the phone, so we needed something to fill that
gap.

The first attempt was to reuse some code from the old Ubuntu TV
project, but ended up needing something with more stable dependencies.
The result was `mediascanner2`: a session service that watches for
changes in a set of directories and then extracts metadata from the
contained files using a combination of
[libexif](https://libexif.github.io/), [TagLib](https://taglib.org/)
and [gstreamer](https://gstreamer.freedesktop.org/).  The results were
stored in a [SQLite database](https://www.sqlite.org/) to take
advantage of its full text indexing.

While the Unity 8 music and video scopes were the original users of
the mediascanner2 index, we later added a Qt/QML interface that acted
as the data source for the phone's music app.

The media scanner source code can be found here:

* https://github.com/unity8-team/mediascanner2

## Thumbnailer

Related to the media scanner, we needed a fast cache of scaled images
displayed on the phone's dash.  The result was a service that could
produce thumbnails for photos, videos, and music (provided the file
had embedded cover art), and manage a disk cache to store them in.

On the client side, a QML plugin plugged into the
`QQuickImageProvider` system, allowing the thumbnails to be displayed
using the standard QML Image component.

The thumbnailer source code can be found here:

* https://github.com/unity8-team/thumbnailer

## Online Accounts

The online accounts system used by Unity 7 and the phone originated in
the Maemo project's [`accounts-sso`
framework](https://en.wikipedia.org/wiki/Accounts_%26_SSO).  While it
worked well on the desktop, it wasn't designed with application
isolation in mind: in order for an application to use the framework,
they needed read access to a database enumerating all of the user's
configured accounts.

To remedy this, I helped design a new D-Bus API for clients to use
instead of `libaccounts-glib`/`libsignon-glib`.  As the new API was
only intended for use by clients (i.e. not the accounts control
panel), we were able to greatly simplify it down to three method calls
and a signal.  Together with the AppArmor confinement used on the
phone, it meant that applications would only see accounts the the user
had granted access to.

## Storage Framework

The last major project I worked on for was a generic API for access to
cloud storage services.  The system consisted of a client library that
would talk to a backend provider over D-Bus.  Each supported cloud
service was implemented as a separate daemon (the intention being to
make it possible to sandbox them from the rest of the system), all
making use of a common library implementing the D-Bus protocol.

The initial use case for this system was a data backup tool for the
phone called Keeper.  Backend providers were written for local
storage, webdav services like ownCloud/Nextcloud, OneDrive, and China
Mobile's Mcloud.

I personally worked on the central storage framework libraries and the
webdav based providers.  The source code can be found here:

* https://github.com/unity8-team/storage-framework
* https://github.com/unity8-team/storage-provider-webdav
