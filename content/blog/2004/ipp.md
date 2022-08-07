---
title: 'IPP'
slug: ipp
date: 2004-03-12T10:49:01+08:00
---

Out of curiosity, I decided to write a little
[IPP](http://www.pwg.org/ipp/) client library in Python. An\
in-progress version can be found
[here](http://www.daa.com.au/~james/files/ipplib.py).

In less than 500 lines of Python, I have an IPP message\
encoder/decoder, and some higher level classes to perform a few\
operations on printers and jobs. I\'ve been able to successfully talk
to\
the following IPP servers:

-   CUPS (I\'ve also got a little code to perform some of the CUPS\
    proprietary operations).
-   an HP LaserJet 5100 and a 2300 \-- both with JetDirect 615n\
    (J6057A) cards.
-   a Lexmark Optra C710.

The following didn\'t want to talk to me:

-   an HP LaserJet 4V with a JetDirect 400n (J4100A) card (it seems\
    to always give me a client-error-bad-request response).
-   a Canon iR C3200. (incidentally, this printer/copier apparently\
    runs an embedded version of SunOS 4.1.4)

I\'m probably doing something wrong for these last two, although it\
is a bit difficult to work out what.

When talking to CUPS, I can use the proprietary CUPS-Get-Printers\
operation to list all the printers it knows about which would make it\
pretty easy to provide functionality of something like
`gnome-print-manager`:

    >>> import ipplib
    >>> cups = ipplib.CUPSServer('ipp://localhost/')
    >>> for info in cups.get_printer_info():
    ... print info['printer-name'], '-', info['printer-uri-supported']
    ...
    harryplotter - ipp://hostname/printers/harryplotter
     ...
    >>>

Similarly, it is easy to list the jobs (pending or completed) for a\
printer. I still haven\'t tried out any of the operations that can\
change a printer or job\'s status, but in theory that should all work
`:)`.

**Thoughts on the protocol**

While IPP uses HTTP as a transport, there is a fair bit of overlap\
between what the two protocols do, such as:

-   request methods/operations and response status codes.
-   identification of the resource the operation is being performed\
    on.
-   IPP attributes seem quite similar to HTTP headers.
-   message body mime type declarations
-   compression of message bodies

Other things serve no purpose when tunneled through HTTP, such as\
message sequence numbers. Apparently the reason for this is so that IPP\
could in the future be sent directly using a custom protocol (in that\
case, the sequence numbers would allow for pipelining of requests, and\
out of order responses). However, I would be surprised if such a\
protocol ever gets developed. IPP will probably continue to use HTTP as\
its transport.

This does lead to complications though:

-   The URI you do an HTTP POST to may differ from the URI specified\
    inside the IPP message. The spec says that the HTTP level URI should
    be\
    ignored. If you have ever looked at the CUPS log files, you might
    have\
    noticed that it almost always posts to \"/\" rather than the
    resource it\
    is acting on. To make matters more complex, [some of the proprietary
    CUPS\
    operations](http://www.cups.org/ipp.html#4_7) require that you post
    to a different HTTP URI to the one\
    in the IPP message.
-   A request can fail at one of two levels. An IPP client will need\
    to detect and handle both HTTP level and IPP level error responses.
    In\
    fact, most IPP error messages will come back as \"HTTP/1.1 200 OK\".

Apart from the few warts, IPP seems like a pretty nice protocol. It\
is fairly easy to parse (assuming you have an http client library to\
use), and is very extensible. A lot nicer than LPR `:)`.
