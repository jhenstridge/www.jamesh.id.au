---
title: 'PSP'
slug: psp
date: 2005-11-28T12:51:52+08:00
---

On my way to UBZ, I bought a PlayStation Portable at the airport duty
free store. It was being sold as the value pack and [Ridge
Racer](http://www.gamespot.com/psp/driving/ridgeracer/) game together,
which came out at roughly the retail price of the two individual items
minus 10% GST.

As well as playing games it can be used as a portable audio or video
player and photo viewer, using memory stick duos as storage. As the
device doesn\'t come with any computer software, the manual provides all
the details about what formats to use for audio/video and where to put
the files on the memory stick. This is quite useful for people using
minority operating systems like Linux `:)`.

I wrote a little [FDI
file](https://bugs.freedesktop.org/show_bug.cgi?id=5137) for the PSP to
expose the `portable_audio_player` capability via HAL, but there
doesn\'t seem to be any standard properties to expose the other
capabilities.

One of the more annoying aspects of the PSP is text entry. It seems as
if they looked at the text entry used by consoles and mobile phones and
combined the worst aspects of both:

-   There is a grid of buttons, each of which corresponds to 3 or 4
    letters which can be selected by pressing the button multiple times.
-   You use the direction pad to select the button to press.
-   No predictive text input or similar.

For games this isn\'t that big a problem, since they don\'t generally
require much text entry. It is more of a problem for the web browser
where it is a lot more important. Something like
[Dasher](http://www.inference.phy.cam.ac.uk/dasher/) might have been a
much more useful text entry system, but I guess they decided to go with
a more conventional approach.

---
### Comments:
#### [Damon Brodie](http://none) - <time datetime="2005-11-29 01:06:21">29 Nov, 2005</time>

Actually most games supply their own text input system. Socom for
example provides a full onscreen keyboard.

---
#### Anonymous - <time datetime="2005-11-29 07:27:19">29 Nov, 2005</time>

Wow, that\'s annoying. Using a grid of letters is relatively
conventional when you only have a direction pad and some buttons, but
using a grid of telephone-style keys is insane.

And yeah, dasher would be more useful; perhaps you should port it. :)

---
#### James Henstridge - <time datetime="2005-11-30 01:58:10">30 Nov, 2005</time>

Damon: my sample size was pretty small: the only game I\'ve played that
required text entry so far was Ridge Racer, which used the horrible
phone style interface from the firmware. I\'m not surprised that third
party developers decided not to use it.

---
