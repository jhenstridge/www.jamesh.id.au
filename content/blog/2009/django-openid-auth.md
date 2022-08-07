---
title: 'django-openid-auth'
slug: django-openid-auth
date: 2009-04-14T16:25:56+08:00
tags: ['Django', 'Launchpad', 'OpenID', 'Python', 'Ubuntu']
---

Last week, we released the source code to
[django-openid-auth](https://launchpad.net/django-openid-auth).  This is
a small library that can add [OpenID](http://openid.net/) based
authentication to [Django](http://www.djangoproject.com/) applications. 
It has been used for a number of internal Canonical projects, including
the sprint scheduler
[Scott](http://www.netsplit.com/ "Scott James Remnant") wrote for the
last Ubuntu Developer Summit, so it is possible you\'ve already used the
code.

Rather than trying to cover all possible use cases of OpenID, it focuses
on providing OpenID Relying Party support to applications using
Django\'s
[django.contrib.auth](http://docs.djangoproject.com/en/dev/topics/auth/ "User authentication in Django")
authentication system.  As such, it is usually enough to edit just two
files in an existing application to enable OpenID login.

The library has a number of useful features:

-   As well as the standard method of prompting the user for an identity
    URL, you can configure a fixed OpenID server URL.  This is useful
    for deployments where OpenID is being used for single sign on, and
    you always want users to log in using a particular OpenID provider. 
    Rather than asking the user for their identity URL, they are sent
    directly to the provider.
-   It can be configured to automatically create accounts when new
    identity URLs are seen.
-   User names, full names and email addresses can be set on accounts
    based on data sent via the [OpenID Simple
    Registration](http://openid.net/specs/openid-simple-registration-extension-1_1-01.html)
    extension.
-   Support for [Launchpad](https://launchpad.net/)\'s Teams OpenID
    extension, which lets you query membership of Launchpad teams when
    authenticating against Launchpad\'s OpenID provider.  Team
    memberships are mapped to Django group membership.

While the code can be used for generic OpenID login, we\'ve mostly been
using it for single sign on.  The hope is that it will help members of
the Ubuntu and Launchpad communities reuse our authentication system in
a secure fashion.

The source code can be downloaded using the following
[Bazaar](http://bazaar-vcs.org/) command:

    bzr branch lp:django-openid-auth

Documentation on how to integrate the library is available in the
`README.txt` file.  The library includes some code written by [Simon
Willison](http://simonwillison.net/) for
[django-openid](http://code.google.com/p/django-openid/), and uses the
same licensing terms (2 clause BSD) as that project.

---
### Comments:
#### [Daniel Watkins](http://blog.daniel-watkins.co.uk) - <time datetime="2009-04-14 20:37:33">2 Apr, 2009</time>

Is Django used for Launchpad at all? Or is it just for other internal
Canonical stuff?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-04-14 22:35:47">2 Apr, 2009</time>

Launchpad is not a Django application \-- it is built on top of Zope 3
and Storm.

Some of the non-internal projects we\'ve got using Django include
summit.ubuntu.com and paste.ubuntu.com.

---
#### [Marius Scurtescu](http://marius.scurtescu.com) - <time datetime="2009-04-14 23:10:43">2 Apr, 2009</time>

Would this also work with Google App Engine?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-04-14 23:47:51">2 Apr, 2009</time>

Marius: I don\'t think there is any code in django-openid-auth that
would be a problem. However, it is built on top of Jan Rain\'s
python-openid which is more likely to have compatibility problems.

At a minimum, you might need to provide a custom URLFetcher class that
uses the appengine HTTP API. It is possible that someone has already
done this work though, so you might want to google it.

---
#### Ivan - <time datetime="2009-04-15 15:18:32">3 Apr, 2009</time>

Hi,

I was looking for an OpenID library to use in our Django application but
when I run \"python manage.py syncdb\" I receive the following error. Am
I missing something?

Creating table django\_openid\_auth\_useropenid

\_mysql\_exceptions.OperationalError: (1170, \"BLOB/TEXT column
\'claimed\_id\' used in key specification without a key length\")

---
#### [Kevin Turner](http://keturn.net/) - <time datetime="2009-04-15 15:27:07">3 Apr, 2009</time>

Looks like the known issues in the googleappengine relating to
python-openid have been fixed in the last few months (i.e. issue \#404).
So it should work!

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-04-15 17:47:11">3 Apr, 2009</time>

Ivan: I can\'t say I tested it on MySQL: the test suite is against
SQLite, and the only other database we use it against is PostgreSQL.

You could try editing django\_openid\_auth/models.py and changing the
claimed\_id definition to a CharField with a shorter maximum length. If
that works for you, please file a bug report in Launchpad.

---
#### [Faruk Akgul](http://faruk.akgul.org/) - <time datetime="2009-04-19 13:20:57">0 Apr, 2009</time>

\@Ivan: It\'s Django\'s fault actually. You need to open
django\_openid\_auth/models.py file and remove unique=True from the
claim\_id which is in the UserOpenID class, then sync. After that you
need ALTER TABLE to create the proper index, then add unique=True option
again in the file. Hope this helps.

Cheers,\
Faruk

---
#### Aaron - <time datetime="2009-04-27 08:55:32">1 Apr, 2009</time>

Thanks for the great app. I and was unclear what the best way is to deal
with user information like a username, email address, etc for an openid
user. Should I just follow
http://docs.djangoproject.com/en/dev/topics/auth/\#storing-additional-information-about-users
and add a profile model? If so, should that model be foreignkeyed to
django\_openid\_auth.openiduser?

Also, is there a way to get extended information like a username from
the openid provider?

---
#### [James Henstridge](http://blogs.gnome.org/jamesh/) - <time datetime="2009-04-28 18:09:45">2 Apr, 2009</time>

Faruk: that column should indeed be unique \-- each identity URL must
only be associated with a single user. As I mentioned above, the column
should probably be changed to CharField with an appropriate length for
MySQL compatibility.

Aaron: django-openid-auth already supports querying the openid provider
for a full name, nickname and email address using the simple
registration extension. It uses these when creating new
django.contrib.auth User objects. As there is already space in the User
object to store them, it doesn\'t use a profile model.

---
#### [Peter Robinett](http://www.bubblefoundry.com) - <time datetime="2009-05-10 17:59:46">0 May, 2009</time>

Has anyone gotten this to work with App Engine and Django 1.0? I\'d love
to use it for my project but I\'m getting the following error:\
ViewDoesNotExist: Could not import django\_openid\_auth.views. Error
was: No module named contenttypes.models

This is peculiar because I don\'t see any reference to contenttypes
except in settings.py. I\'m using google-app-engine-django and
contenttypes is commented out, though uncommenting it doesn\'t help (you
can see my whole process here:
http://www.bubblefoundry.com/blog/2009/05/installing-the-google-app-engine-sdk-and-django-102/).
As you can tell, I\'m quite new to Django and App Engine, so any help
would be appreciated.

Peter

---
