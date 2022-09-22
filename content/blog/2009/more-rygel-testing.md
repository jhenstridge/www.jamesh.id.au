---
title: 'More Rygel testing'
slug: more-rygel-testing
date: 2009-06-19T00:06:19+08:00
tags: ['Gnome', 'PlayStation 3', 'Ubuntu', 'UPnP']
---

In my [last post](ubuntu-packages-for-rygel.md "Ubuntu packages for
Rygel"), I said I had trouble getting Rygel\'s tracker backend to
function and assumed that it was expecting an older version of the
API. It turns out I was incorrect and the problem was due in part to
Ubuntu specific changes to the Tracker package and the unusual way
Rygel was trying to talk to Tracker.

The Tracker packages in Ubuntu remove the D-Bus service activation file
for the \"org.freedesktop.Tracker\" bus name so that if the user has not
chosen to run the service (or has killed it), it won\'t be automatically
activated. Unfortunately, instead of just calling a Tracker D-Bus
method, Rygel was trying to manually activate Tracker via a
StartServiceByName() call. This would fail even if Tracker was running,
hence my assumption that it was a tracker API version problem.

This problem will be fixed in the next Rygel release: it will call a
method on Tracker directly to see if it is available. With that problem
out of the way, I was able to try out the backend. It was providing a
lot more metadata to the PS3 so more files were playable, which was
good. Browsing folders was also much quicker than the folder back end.
There were a few problems though:

1.  Files are exposed in one of three folders: \"All Images\", \"All
    Music\" or \"All Videos\". With even a moderate sized music
    collection, this is unmangeable. It wasn\'t clear what order the
    files were being displayed in either.
2.  There was quite a long delay before video playback starts.

When the folder back end fixes the metadata and speed issues, I\'d be
inclined to use it over the tracker back end.

**Video Transcoding**

Getting video transcoding working turned out to require a newer
GStreamer (0.10.23), the \"unstripped\" ffmpeg libraries and the \"bad\"
GStreamer plugins package from multiverse. With those installed, things
worked pretty well. With these dependencies encoded in the packaging,
it\'d be pretty painless to get it set up. Certainly much easier than
setting things up in MediaTomb\'s configuration file.

---
### Comments:
#### Kevin - <time datetime="2009-06-19 00:41:51">19 Jun, 2009</time>

Quick question: Are thumbnails seen when browsing via the PS3?

---
#### Jerome Haltom - <time datetime="2009-06-19 01:13:35">19 Jun, 2009</time>

Is your package set up to run as a system daemon or an instance that has
to be started per-user? Seems tracker would not work in the case of the
former\... but all the other plugins that I can imagine writing would
be. File backend, TV tuner scraper, etc.

---
#### James Henstridge - <time datetime="2009-06-19 09:47:07">19 Jun, 2009</time>

Kevin: no thumbnails yet.

Jerome: Rygel takes its preferences from GConf, so probably wouldn\'t
work as a system daemon at present.

---
#### Zeeshan Ali - <time datetime="2009-06-19 21:50:54">19 Jun, 2009</time>

Thumbnails: This is high on my TODO. I\'ll mostly probaly be using
hildon-thumbnailer for thumbnails simply because it is already available
on/for Maemo.

GConf: I don\'t think use of gconf makes rygel unusable as a
system-daemon but it does make it harder yes. I intend to replace gconf
usage with .ini files soon. :)

---
#### James Henstridge - <time datetime="2009-06-19 22:18:30">19 Jun, 2009</time>

Zeeshan: for the non-Maemo case, gnome-desktop\'s thumbnailer might be
worth a look. That way you\'d have thumbnails for everything Nautilus
can handle (and take advantage of any thumbnails it has already
generated).

---
#### Zeeshan Ali - <time datetime="2009-06-19 23:35:13">19 Jun, 2009</time>

Jim: Sure but isn\'t there a freedesktop spec that these both implement?
If that is the case, we are all good whichever of them I use. :)

---
