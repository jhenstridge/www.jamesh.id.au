---
title: 'jhbuild'
slug: jhbuild
date: 2004-02-05T05:37:10+08:00
draft: false
tags: ['JHBuild']
---

Checked in a fairly big set of modifications to jhbuild, designed to
make it a bit more modular and the code less messy. I had been working
on these changes for a while now, and had been keeping track of them on
the `jhbuild-ng` branch.

Here are a few of the main changes:

**Code reorganised into a package**

:   The code has been reorganised into a Python package. Unfortunately
    this means that the old shell script used to start jhbuild won\'t
    work. Rerunning \"make install\" will fix this though. This will
    make it easier to extend things in the future.

**AMD64 support**

:   If you are running on an AMD64 Linux machine, the libraries
    jhbuild builds will end up in `${prefix}/lib64`, as they should.
    If you really want your 64-bit libraries to go in `${prefix}/lib`
    still, you can add \"`use_lib64 = False`\" in your config file.

    The code is set up to try and set `use_lib64` correctly for the
    machine it is running on. If you find a case where `use_lib64` is
    set incorrectly, please file a bug report.

**Unattended build with reporting**

:   Based on a suggestion from someone in the audience at
    [Gnome.conf.au](http://www.gnome.org/~jdub/2004/gnome.conf.au/), I
    implemented a new non-interactive mode that redirects all output
    to a bunch of files in a directory, along with an HTML page giving
    a summary of how the build went.

    An example of the output can be seen
    [here](http://www.daa.com.au/~james/files/jhbuild-tbox/)
    (generated from a run on an Opteron system). This functionality is
    available through the `jhbuild tinderbox` command.

    It would be nice to get some of the Gnome companies (eg. Sun) to
    set up some build boxes running something like this on uncommon
    hardware to help test Gnome builds.

**Build environment sanity check**

:   A `jhbuild sanitycheck` command. This is intended to be used as a
    way of checking that the build environment is sane. I plan on
    changing `jhbuild bootstrap` to be a script intended for
    installing all the build tools in the build prefix. This way, if
    you use the build tools provided by your distro, you can simply
    run `sanitycheck` to make sure everything is okay and omit
    `bootstrap`.

    This command should become more useful as I extend it (most likely
    in response to bug reports).

**Load module sets from web servers**

:   Previously, all the build information in jhbuild was maintained
    with the code in Gnome CVS. This worked pretty well for building
    Gnome, since people who were able to check code in that would
    break the build could also fix the build instructions in jhbuild.

    Since then jhbuild has become less Gnome specific, and includes
    rules for building a number of non-Gnome packages including a lot
    of stuff from [freedesktop.org](http://www.freedesktop.org), such
    as the [X server](http://www.freedesktop.org/Software/xserver).
    Having the build rules stored in Gnome CVS isn\'t anywhere near as
    convenient for them, which was the reason for this new feature.

    Now it is possible to specify a full URL as the module set in the
    config file. Jhbuild will then download the module definition file
    from the web server and use that. There is code to check whether
    the modules file has changed if the cached copy is too old too
    (these checks use various HTTP features to keep the bandwidth
    usage to a minimum). Hopefully this feature will be useful for
    other large projects looking for a build tool.

I have tested the code a bit, but I wouldn\'t be too surprised if one or
two bugs have been introduced. If you find a regression, make sure you
report it in bugzilla.

It should now be a lot easier to add new features, which is a good
thing.
