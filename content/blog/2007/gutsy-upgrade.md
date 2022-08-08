---
title: 'Upgrading to Ubuntu Gutsy'
slug: gutsy-upgrade
date: 2007-09-24T16:59:23+08:00
tags: ['Ubuntu']
---

I got round to upgrading my desktop system to
[Gutsy](https://wiki.ubuntu.com/GutsyGibbon) today. I\'d upgraded my
laptop the previous week, so was not expecting much in the way of
problems.

I\'d done the original install on my desktop back in the Warty days, and
the root partition was a bit too small to perform the upgrade. As there
was a fair bit of accumulated crud, I decided to do a clean install.
Things mostly worked, but there were a few problems, which I detail
below:

**Dual Head Configuration**

With previous releases, I was using the Radeon driver\'s MergedFB mode,
as it gives a better user experience than the traditional Xinerama code
(3D acceleration on both heads, better performance, etc). After moving
adding the MergedFB options to xorg.conf, I was just getting the same
image cloned on both displays.

Looking at the X server log file, there was a message saying that
MergedFB support had been removed in favour of RandR 1.2 support. And it
was possible to get dual head working with the `xrandr` command line
tool:

    xrandr --output VGA-0 --right-of DVI-0

It was good to know that dual-head still worked, but I didn\'t want to
reconfigure this every time I restarted the machine. I didn\'t find much
information on how to configure the initial RandR configuration on the
X.org website, but did find a [useful guide on the Intel Linux Graphics
website](http://www.intellinuxgraphics.org/dualhead.html "How to setup Dual Head for Intel Graphics with RandR 1.2").
While the guide was aimed at the Intel driver, it had enough information
to get things configured for the Radeon driver. The main difference was
in the naming of the outputs. Below is a an excerpt of my configuration
file that configures things the way I had them previously:

    Section "Device"
            Identifier      "ATI Technologies Inc RV280 [Radeon 9200 SE]"
            Driver          "ati"
            BusID           "PCI:1:0:0"
            Option          "monitor-DVI-0" "Sony SDM-S74 [1]"
            Option          "monitor-VGA-0" "Sony SDM-S74 [2]"
    EndSection

    Section "Monitor"
            Identifier      "Sony SDM-S74 [1]"
            Option          "DPMS"
            HorizSync       30-65
            VertRefresh     50-75
            Option          "LeftOf"        "Sony SDM-S74 [2]"
    EndSection

    Section "Monitor"
            Identifier      "Sony SDM-S74 [2]"
            Option          "DPMS"
            HorizSync       30-65
            VertRefresh     50-75
    EndSection

    Section "Screen"
            Identifier      "Default Screen"
            Device          "ATI Technologies Inc RV280 [Radeon 9200 SE]"
            Monitor         "Sony SDM-S74 [1]"
            DefaultDepth    16
            SubSection "Display"
                    Modes           "1280x1024" "1024x768" "800x600" "640x480"
                    Virtual         2560 1024
            EndSubSection
    EndSection

I had originally tried setting the VGA monitor to be \"RightOf\" the
monitor connected to the DVI, but that left me with the desktop in clone
mode. The main difference I\'ve noticed with this configuration compared
to my previous one is that the GDM login prompt displays on the right
hand head (VGA) rather than the left hand head (DVI).

**Window Shadows Don\'t Render**

Desktop Effects were enabled by default after the install (and on the
live CD). While some effects seemed to work, the shadows on the panel
and drop down menus were rendered as opaque grey boxes around the
windows. I ended up just disabling the effects to clear up the problem.

This bug had already been reported as [bug
141304](https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-video-ati/+bug/141304 "White boxes instead of shadows on ATI 9600 (radeon driver)")
(which may be the same as [bug
116808](https://bugs.launchpad.net/ubuntu/+source/xserver-xorg-video-intel/+bug/116808 "White boxes instead of shadows on Intel 945 (-intel driver)")).

**Firefox Crashes on Startup**

When I tried to start firefox, it would momentarily display a window and
then crash. This appears to be [bug
133124](https://bugs.launchpad.net/ubuntu/+source/firefox/+bug/133124 "MASTER [GUTSY] firefox crashed [@pixman_compositeGeneral] [@_cairo_pixman_composite] [@_cairo_image_surface_composite] from libcairo"),
and seems to only occur on AMD64 systems. The problem appears to be in
the `ubuntulooks` theme engine, and switching to a different control
theme makes the problem go away, but hopefully it\'ll get fixed for the
final release.

**Problems Rendering Ligatures in Firefox**

The problems rendering ligatures in firefox seem to be back again. This
problem was never really fixed, but was worked around by removing the
ligature table entries from the DejaVu fonts. With the ligature table
entries back, the symptoms have returned. This is [bug
37828](https://bugs.launchpad.net/ubuntu/+source/firefox/+bug/37828 "Text rendered incorrectly in presence of ligatures and justified text").

---
### Comments:
#### Smarter - <time datetime="2007-09-24 18:29:38">24 Sep, 2007</time>

Why didn\'t you just used displayconfig-gtk to configure your dual head?

---
#### James Henstridge - <time datetime="2007-09-24 19:24:09">24 Sep, 2007</time>

I just gave displayconfig-gtk a go, and ran into a few problems:

1\. the configuration it generates caused the X server to crash.

2\. it generated a traditional Xinerama configuration, which is a step
back from merged FB (no OpenGL on second head, drawing operations that
span two heads need to be performed once for each framebuffer, etc).

Using the xrandr \"monitor-\*\" device options gives me a single
framebuffer with each monitor displaying a portion of it (as I had with
MergedFB). As an added bonus, I can reconfigure things at runtime if I
want to.

---
#### James - <time datetime="2007-09-24 22:32:57">24 Sep, 2007</time>

Does
http://weblogs.mozillazine.org/roc/archives/2007/09/textalicious.html
look like it\'ll fix the problem?

---
#### James Henstridge - <time datetime="2007-09-24 23:34:23">24 Sep, 2007</time>

According to the https://bugzilla.mozilla.org/show\_bug.cgi?id=331716,
the firefox rendering problem should get fixed in Firefox 3.0 (and other
Gecko 1.9 based applications). That is a little late for Gutsy though.

---
#### [Tolero](http://tolero.org) - <time datetime="2007-09-25 17:13:58">25 Sep, 2007</time>

I\'m impressed much how well did the [gutsy detected my
card](http://tech.tolero.org/blog/en/linux/review-ubuntu-710-gutsy-features-changes).
But I did a fresh install and I have nvidia card.

---
#### justin - <time datetime="2007-10-18 01:11:22">18 Oct, 2007</time>

I also tried displayconfig-gtk, and no joy. This procedure worked for
me. Thanks for posting it.

---
#### Jaakko - <time datetime="2007-10-18 20:06:47">18 Oct, 2007</time>

I know it\'s possible to use s-video tv-out with radeon(9000) & randr in
Gutsy but does anyone know if overscan is possible with this approach?
Is there a spesific parameter for randr to do this?

---
#### hiredgoon - <time datetime="2007-10-23 08:40:18">23 Oct, 2007</time>

James man I love you. Upgrading to Gutsy broke my fglrx dual-head
display. This got me working again.

-hg

---
