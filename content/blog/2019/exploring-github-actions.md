---
title: 'Exploring Github Actions'
slug: exploring-github-actions
date: 2019-09-06T13:17:08+08:00
tags: ['Continuous Integration', 'Gnome', 'Python', 'Ubuntu']
---

To help keep myself honest, I wanted to set up automated test runs on a
few personal projects I host on Github. At first I gave
[Travis](https://travis-ci.org/) a try, since a number of projects I
contribute to use it, but it felt a bit clunky. When I found Github had
a new [CI system in beta](https://github.com/features/actions/), I
signed up for the beta and was accepted a few weeks later.

While it is still in development, the configuration language feels lean
and powerful. In comparison, Travis\'s configuration language has
obviously evolved over time with some features not interacting properly
(e.g. matrix expansion only working on the first job in a workflow using
build stages). While I\'ve never felt like I had a complete grasp of
the Travis configuration language, the single page description of
Actions configuration language feels complete.

The main differences I could see between the two systems are:

1.  A Github workflow is composed of multiple jobs right from the start.
2.  All jobs run in parallel by default. It is possible to serialise
    jobs (similar to Travis\'s stages) by declaring dependencies between
    jobs.
3.  Each job specifies which VM image it will run on, with a choice of
    Ubuntu, Windows, or MacOS versions. If you choose Ubuntu, you can
    also specify a Docker container to run your build in, giving access
    to other Linux build environments.
4.  Each job can have a matrix attached, allowing the job to be
    duplicated according to a set of parameters.
5.  Jobs are composed of a sequence of steps. Unlike Travis\'s fixed
    set of build phases, these are generic.
6.  Steps can consist of either code executed by the shell or a
    reference to an external action.
7.  Actions are the primary extension mechanism, and are even used for
    basic tasks like checking out your repository. Actions are either
    implemented in JavaScript or as a Docker container. Only JavaScript
    actions are available for Windows and MacOS jobs.

The first project I converted over was asyncio-glib, where I was using
Travis to run the test suite on a selection of Python versions. My old
Travis configuration [can be seen
here](https://github.com/jhenstridge/asyncio-glib/blob/b63b11b92369fe77cd31f99a74413ab17c716f41/.travis.yml),
and the new Actions workflow [can be seen
here](https://github.com/jhenstridge/asyncio-glib/blob/154c7cbfafb10b3dc9dbef05088b7600b0289f4d/.github/workflows/run-tests.yml).
Both versions are roughly equivalent, although the
`actions/setup-python@v1` action doesn\'t currently make beta releases
of Python available. The result of a run of the workflow [can be seen
here](https://github.com/jhenstridge/asyncio-glib/runs/212801738).

For a second project (videowhisk), I am [running the
tests](https://github.com/jhenstridge/videowhisk/blob/d6cc27766f0dead1b5cbd0e5800b21d24cfa2b84/.github/workflows/run-tests.yml)
against the VM\'s default Python image. For this project, I\'m more
interested in compatibility with the distro release\'s GStreamer
libraries than compatibility with different Python versions. I suppose
I could extend this using the matrix feature to test on multiple Ubuntu
versions, or containers for other Linux releases.

While I\'ve just been using this to run the test suite, it looks like
Actions can be used for a lot more. A project can have multiple
workflows with different triggers, so it can also be used for automated
triage of bugs or pull requests (e.g. request a review from a specific
developer when a pull request is created that modifies files in a
specific directory). It also looks like I could create a workflow to
automatically publish to PyPI when I push a new tag to the repository
that looks like a version number.

It will be interesting to see what this does to the larger ecosystem of
\"CI as a service\" products built to work with Github. On the one hand
having a choice is nice, but on the other hand it\'s nice to have
something well integrated. I really like Gitlab\'s integrated CI system
for projects I have hosted on various Gitlab instances, for example.
