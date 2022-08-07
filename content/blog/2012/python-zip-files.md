---
title: 'Packaging Python programs as runnable ZIP files'
slug: python-zip-files
date: 2012-05-21T15:31:05+08:00
tags: ['Python']
---

One feature in recent versions of Python I hadn\'t played around with
until recently is the ability to package up a multi-module program into
a ZIP file that can be run directly by the Python interpreter.  I
didn\'t find much information about it, so I thought I\'d describe
what\'s necessary here.

Python has had the ability to add ZIP files to the module search path
since [PEP
273](http://www.python.org/dev/peps/pep-0273/ "PEP 273 -- Import Modules from Zip Archives")
was implemented in Python 2.3.  That can let you package up most of your
program into a single file, but doesn\'t help with the main entry point.

Things improved a bit when [PEP
338](http://www.python.org/dev/peps/pep-0338/ "PEP 338 -- Executing modules as scripts")
was implemented in Python 2.4, which allows any module that can be
located on the Python search path can be executed as a script.  So if
you have a ZIP file `foo.zip` containing a module `foo.py`, you could
run it as:

    PYTHONPATH=foo.zip python -m foo

This is a bit cumbersome to type though, so Python 2.6 lets you run
[directories and zip files
directly](http://bugs.python.org/issue1739468 "Issue 1739468: Allow interpreter to execute a zip file"). 
So if you run

    python foo.zip

It is roughly equivalent to:

    PYTHONPATH=foo.zip python -m __main__

So if you place a file called `__main__.py` inside your ZIP file (or
directory), it will be treated as the entry point to your program.  This
gives us something that is as convenient to distribute and run as a
single file script, but with the better maintainability of a
multi-module program.

If your program has dependencies that you don\'t expect to find present
on the target systems, you can easily include them up in the zip file
along side your program.  If you need to provide some data files along
side your program, you could use the
[`pkg_resources`](http://packages.python.org/distribute/pkg_resources.html)
module from `setuptools` or `distribute`.

There are still a few warts with this set up though:

-   If your program fails, the trace back will not include lines of
    source code.  This is a general problem for modules loaded from zip
    files.
-   You can\'t package extension modules into a zip file.  Of course, if
    you\'re in a position where the target platforms are locked down
    tight enough that you could reliably provide compiled code that
    would run on them, you\'d probably be better off using the
    platform\'s package manager.
-   There is no way to tell whether a ZIP file can be executed directly
    with Python without inspecting its contents.  Perhaps this could be
    addressed by defining a new file extension to identify such files.

---
### Comments:
#### [sil](http://www.kryogenix.org/) - <time datetime="2012-06-04 22:28:54">1 Jun, 2012</time>

Interesting discovery: if you just rename the .zip file to whatever.py,
then it works and you can run it with \"python whatever.py\"\...

---
#### [» u1ftp: a demonstration of the Ubuntu One API James Henstridge](http://blogs.gnome.org/jamesh/2012/07/05/u1ftp/) - <time datetime="2012-07-04 16:32:50">3 Jul, 2012</time>

\[\...\] James Henstridge Random stuff Skip to content « Packaging
Python programs as runnable ZIP files \[\...\]

---
