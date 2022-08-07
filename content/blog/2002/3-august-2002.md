---
title: '3 August 2002'
slug: 3-august-2002
date: 2002-08-03T15:38:59+08:00
---

Got the nautilus view up and running. A number of pictures of an early
version are at:

-   [Information
    page](http://www.daa.com.au/~james/images/nautilus-rpm/rpm-view-1.png)
-   [Files
    page](http://www.daa.com.au/~james/images/nautilus-rpm/rpm-view-2.png)
-   [Provides and Requires
    page](http://www.daa.com.au/~james/images/nautilus-rpm/rpm-view-3.png)

In the current version, provides and requires have been split onto
separate pages (and I added conflicts and obsoletes), and they are only
visible if there is anything to show. There is also a changelog page for
information about development of the package.

I added support for looking at info about package files on disk (as
opposed to info about installed packages), which didn\'t take much code.

I turned off the feature where it tries to resolve \"requires\" or
\"provides\" resources (so you could see which packages provided the
resources the current one requires, and what packages depend on it). I
just need to add some code to follow these deps on demand \...
