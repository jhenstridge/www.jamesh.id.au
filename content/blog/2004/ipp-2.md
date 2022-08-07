---
title: 'IPP'
slug: ipp-2
date: 2004-03-18T06:20:50+08:00
draft: false
---

Did a little more hacking on my IPP client library, and wrote a small
[PyGTK](http://www.pygtk.org/) program that lets you do simple
management tasks (view all print queues/classes, view queued and
completed jobs for printers, stop and start print queues, etc).

If you want to try it out, grab
[ipplib.py](http://www.daa.com.au/~james/files/ipplib.py) and
[printerlist.py](http://www.daa.com.au/~james/files/printerlist.py). Put
them in the same directory and run \"`python printerlist.py`\". Seems to
work pretty well for less than a thousand lines of code.

To get things working with CUPS\'s authentication, I do the following
for operations like `Pause-Printer`:

1.  Submit request to the HTTP URI corresponding to the IPP one.
2.  If the response has an IPP status code of
    `client-error-not-authorized`, then resubmit the request to the URI
    `/admin/` relative to the previous URI (not changing the IPP
    message).
3.  Return the IPP response message.

This seems to work quite reliably, so I might add the fallback to all
the IPP requests.
