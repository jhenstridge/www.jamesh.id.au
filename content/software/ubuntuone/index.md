---
title: "Ubuntu One"
date: 2012-11-01T00:00:00+08:00
draft: false
keywords: ["ubuntu"]
---

[Ubuntu One](https://en.wikipedia.org/wiki/Ubuntu_One) was a set of
online services provided by Canonical for Ubuntu users.  It provided
cloud hosted storage for files and structured data, synchronised to
the user's local machine.  The Ubuntu One service was discontinued in
2014.

<!--more-->

There were other services built around this core, including a digital
music store that would deliver MP3s to the user's cloud storage (which
would then be synchronised locally), and smart phone integration for
contact synchronisation and music streaming.

## django-openid-auth

The main Ubuntu One web site and service was built using the
[Django](https://www.djangoproject.com/) framework.  As we wanted to
integrate with Ubuntu/Launchpad's existing user account
infrastructure, one of the first things I worked on was a package to
bridge it to Django's standard `django.contrib.auth` system.

The result was the
[`django-openid-auth`](http://launchpad.net/django-openid-auth)
package: an OpenID relying party implementation that allows users to
authenticate via OpenID and creates linked Django user records.  This
made it trivial to add OpenID support to essentially any Django
application that used the standard authentication framework.

## CouchDB

The structured data storage and synchronisation system was built on
top of [CouchDB](https://couchdb.apache.org/): a "NoSQL" JSON document
database.  In the Ubuntu One system, the user ran an instance of
CouchDB on their desktop, which would use the standard CouchDB
replication protocol to synchronise the user's databases with a
CouchDB instance running in the cloud.

This gave the user full offline access to their data, with the ability
to synchronise any changes when they reconnect.  A number of
applications were modified to use or back up their data to this
system.  I worked on a number of projects using this system, including:

[Bindwood](https://launchpad.net/bindwood)
: Bindwood was an extension for the Firefox web browser that provided
  bi-directional sync of bookmarks with the local CouchDB
  instance.  I worked on a rewrite of the extension to get it working
  with Firefox >= 3.5.

Google Contacts Sync
: I worked on some code to implement bi-directional sync of Google
  Contacts with a CouchDB instance.  The plan had been to run this
  against the cloud instance of CouchDB as a better way to provide
  contacts integration on Android and iOS phones than the SyncML
  solution we had been using.  Unfortunately, the service did not make
  it out of beta before Ubuntu One's data sync service was shut down.

## File Storage

I worked on a few projects related to the file storage side of Ubuntu One:

[u1ftp](https://launchpad.net/u1ftp)
: While Ubuntu One had full sync clients for Ubuntu, Windows, and
  MacOS, this was intended as a light weight method of accessing a
  user's files on other systems.  It was a custom FTP server that
  could run on locally and bridge requests to the Ubuntu One REST API.
  The user could then use their file manager to upload and download
  their files through the local FTP server.

Thunderbird Filelink
: [Filelink](https://support.mozilla.org/en-US/kb/filelink-large-attachments)
  is a feature of the Thunderbird mail client that gives users an
  option to upload large files to a file storage service instead of
  attaching them to a message.  I worked on [an Ubuntu One
  backend](https://bugzilla.mozilla.org/show_bug.cgi?id=744037) for
  the feature.
