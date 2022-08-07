---
title: 'Playing with Google Maps API'
slug: playing-with-google-maps-api
date: 2005-09-21T15:43:05+08:00
draft: false
tags: ['Gnome']
---

I finally got round to playing with the Google Maps API, and the results
can be seen [here](http://www.gnome.org/~jamesh/maps/gnome.html). I took
data from the [GnomeWorldWide](http://live.gnome.org/GnomeWorldWide)
wiki page and merged in some information from the [Planet
Gnome](http://planet.gnome.org/) FOAF file (which now includes the
nicknames and
[hackergotchis](http://en.wikipedia.org/wiki/Hackergotchi)).

::: {align="center"}
[\
![this Ubuntu guy at OSCON who just wouldn\'t stop
talking](http://blogs.gnome.org/jamesh/files/2005/09/gnome-world-wide.jpg){width="450"
height="350"}\
](http://www.gnome.org/~jamesh/maps/gnome.html)
:::

The code is available
[here](http://www.gnome.org/~jamesh/bzr/mapsworldwide/) (a BZR branch,
but you can easily download the latest versions of the files directly).
The code works roughly as follows:

-   Convert the locations info `GnomeWorldWide` page into an XML file,
    adding information from the Planet Gnome FOAF file using the
    `makexml.py` script.
-   When the main page loads, it requests the XML file previously
    generated. For each person element in the XML file, a marker is
    created on the map.
-   When a marker is clicked, an info window is displayed, which is the
    result of applying an XSLT transformation to the XML node.

---
### Comments:
#### [Ralph](http://ralph-wabel.net) - <time datetime="2005-09-22 03:12:32">4 Sep, 2005</time>

Nice stuff, how about implementing that to the ubuntu WorldWide section.
It would make it much more fun. The german site ubuntuusers has it
already: <http://www.ubuntuusers.de/map.php>

---
#### fatal - <time datetime="2005-09-22 21:50:09">4 Sep, 2005</time>

Found a bug:

ChenYu (jcome)\
Foshan, China

China (as far as I know) is not located in northern Sweden (next to the
Finnish border). :)

---
#### [James Henstridge](http://blogs.gnome.org/jamesh) - <time datetime="2005-09-23 13:21:12">5 Sep, 2005</time>

My code doesn\'t attempt to correct invalid data. It looks like that
person entered his details incorrectly on the wiki page (switching
latitude and longitude by the looks of it).

---
#### [antrix](http://www.antrix.net/) - <time datetime="2005-10-04 13:34:46">2 Oct, 2005</time>

Well.. I made a map of my friends and sent out a link to all of them
only to have them point out that the map doesn\'t work in Internet
Explorer :-(

Now I don\'t even know Javascript, leave alone browser specific js.. any
idea what\'s going wrong?

---
#### [xerxas](http://xerxas@gmail.com) - <time datetime="2005-11-08 05:33:21">2 Nov, 2005</time>

Something new on the IE issue ?

---
