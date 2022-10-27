---
title: 'Building IoT projects with Ubuntu Core talk'
slug: ubuntu-core-iot
date: 2019-03-20T10:38:53+08:00
tags: ['Linux', 'PLUG', 'snapd', 'Ubuntu']
---

Last week I gave a talk at [Perth Linux Users
Group](http://www.plug.org.au/) about building IoT projects using Ubuntu
Core and Snapcraft. The video is now available online. Unfortunately
there were some problems with the audio setup leading to some background
noise in the video, but it is still intelligible:

{{< youtube "phMWrcGOGJE" >}}

The slides used in the talk can be found
[here](https://docs.google.com/presentation/d/1-obX63OoVCuFBCs3SXhwEk2_BOcGTT8uENFKfrmxanE).

The talk was focused on how Ubuntu Core could be used to help with the
ongoing security and maintenance of IoT projects. While it might be easy
to buy a Raspberry Pi, install Linux and your application, how do you
make sure the device remains up to date with security updates? How do
you push out updates to your application in a reliable fashion?

I outlined a way of deploy a project using Ubuntu Core, including:

1.  Packaging a simple web server app using the `snapcraft` tool.
2.  Configuring automatic builds from git, published to the edge channel
    on the Snap Store. This is also an easy way to get ARM builds for a
    package, rather than trying to deal with cross compilation tool
    chains.
3.  Using the `ubuntu-image` command to create an Ubuntu Core image with
    the application preinstalled

I gave a demo booting such an image in a virtual machine. This showed
the application up and running ready to use. I also demonstrated how
promoting a build from the edge channel to stable on the store would
make it available to the system wide automatic update mechanism on the
device.
