---
title: 'Getting "bzr send" to work with GMail'
slug: bzr-send-gmail
date: 2009-01-16T18:19:31+09:00
tags: ['Bazaar', 'Python']
---

One of the nice features of [Bazaar](http://bazaar-vcs.org/) is the
ability to send a bundle of changes to someone via email. If you use a
supported mail client, it will even open the composer with the changes
attached. If your client isn\'t supported, then it\'ll let you compose
a message in your editor and then send it to an SMTP server.

GMail is not a supported mail client, but there are a few work arounds
[listed on the wiki](http://bazaar-vcs.org/BzrSendWithGmail). Those
really come down to using an alternative mail client (either the editor
or Mutt) and sending the mails through the GMail SMTP server. Neither
solution really appealed to me. There doesn\'t seem to be a programatic
way of opening up GMail\'s compose window and adding an attachment (not
too surprising for a web app).

What is possible though is connecting via IMAP and adding messages to
the drafts folder (assuming IMAP support is enabled). So I wrote a
small plugin to do just that. It can be installed with the following
command:

    bzr branch lp:~jamesh/+junk/bzr-imapclient ~/.bazaar/plugins/imapclient

And then configure the IMAP server, username and mailbox according to
the instructions in the README file. You can then use \"bzr send\" as
normal and then complete and send the draft at your leisure.

One nice thing about the plugin implementation is that it didn\'t need
any GMail specific features: it should be useful for anyone who has
their drafts folder stored on an IMAP server and uses an unsupported
mail client.

The main area where this could be improved would be to open up the
compose screen in the web browser. However, this would require knowing
the internal message ID for the new message, which I can\'t see how to
access via IMAP.

---
### Comments:
#### [Jeremy](http://jeremy.visser.name/) - <time datetime="2009-01-16 19:50:18">16 Jan, 2009</time>

I haven\'t used `bzr send` yet, but I gather that it doesn\'t use
`sendmail` to send the mail. That would seem the logical choice, as you
could then configure your MTA to send via Gmail\'s SMTP server.

---
#### James Henstridge - <time datetime="2009-01-16 20:59:20">16 Jan, 2009</time>

Bazaar does have support for sending to an SMTP server, and that is what
the first solution on the wiki page I linked to describes.

But that doesn\'t let you pick recipients from your address book or
defer sending the message in case you want to edit it (in contrast, my
solution always requires additional work to send the message). The
plugin I wrote isn\'t obviously superior to those solutions, but it does
have some benefits.

---
#### LaserJock - <time datetime="2009-01-18 01:53:48">18 Jan, 2009</time>

Thanks for this James, I like it much better than a \"send via Gmail
SMTP\" route. I really like the idea of it showing up as a draft in my
Gmail. In fact, I\'d love to get reportbug to do the same thing so I
could do similar when reporting Debian bugs.

---
#### [Chris Conway](http://procrastiblog.com/) - <time datetime="2009-01-18 02:35:48">18 Jan, 2009</time>

Thanks! I beat my head against to wall trying to figure this out a while
ago and finally gave up when I figured out you can\'t make an attachment
through the GMail \"API\"\...

---
#### [Tom Berger](http://intellectronica.net/) - <time datetime="2009-02-11 02:45:03">11 Feb, 2009</time>

Fantastic!

Note that this doesn\'t work for me (with Gmail) when the mailbox
argument to append is a Unicode string. Converting it to an old-school
string does the trick.

---
