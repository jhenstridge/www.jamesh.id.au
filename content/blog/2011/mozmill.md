---
title: 'Using Mozmill to Test Firefox Extensions'
slug: mozmill
date: 2011-02-20T09:30:01+08:00
draft: false
tags: ['firefox', 'mozilla', 'testing', 'Ubuntu One']
---

Recently I\'ve been working on [a Firefox
extension](https://launchpad.net/bindwood), and needed a way to test the
code.  While testing code is always important, it is particularly
important for dynamic languages where code that hasn\'t been run is more
likely to be buggy.

I had not experience in how to do this for Firefox extensions,
so [Eric](http://thisfred.posterous.com/) suggested I try out
[Mozmill](https://developer.mozilla.org/en/Mozmill). which has been
quite helpful so far.  There were no Ubuntu packages for it, so I\'ve
put some together in my PPA for anyone interested:

-   <https://launchpad.net/~jamesh/+archive/python>

The packages are not quite up to the standard needed to go into Ubuntu
yet (among other things, there are no man pages for the various
commands), but they do work and shouldn\'t eat your system.

Running mozmill tests is pretty easy, and can be done with a command
like the following:

    mozmill --addons=$PATH_TO_YOUR_EXTENSION \
        --show-errors --test=$PATH_TO_YOUR_TESTS

This will launch an instance of Firefox using a temporary scratch
profile that loads your extension, and then run your tests.  The tests
will run inside the Firefox instance with the results fed back to the
mozmill utility.  When the tests complete, the Firefox instance will
exit and the scratch profile deleted.

While many of the mozmill tests that Mozilla has written are relatively
high level, essentially treating it as an user input automation system,
you have full access to Mozilla\'s component architecture, so the
framework seems well suited to lower level unit testing and functional
tests.

Tests are structured as simple javascript modules, and uses conventions
similar (although not identical) to many other xUnit frameworks.  Any
function whose name starts with \"`test`\" is a test.  If the module
contains \"`setupTest`\" or \"`teardownTest`\" functions, they will be
called before and after each test respectively.  If the module contains
\"`setupModule`\" or \"`teardownModule`\" functions, they will be called
before and after all the tests in the module run, respectively.

There is a
\"[jumlib](https://developer.mozilla.org/en/Mozmill/Mozmill_Unit_Test_Framework)\"
module that you can import into your tests that provides familiar
helpers like `assertEquals()`, etc.  One difference in their behaviour
to what I am used to is that they don\'t interrupt the test on failure.
 On the plus side, if you\'ve got a bunch of unrelated assertions at the
end of your test, you will see all the failures rather than just the
first.  On the down side, you don\'t get a stack trace with the failure
so it can be difficult to tell which assertion failed unless you\'ve
provided a comment to go with each assertion.

The framework seems to do the job pretty well, although the output is a
little cluttered.  It has the facility to publish its test results to a
special [dashboard web
application](https://wiki.mozilla.org/QA/Mozmill_Test_Automation/Dashboard),
but I\'d prefer something easier to manage on the command line.
