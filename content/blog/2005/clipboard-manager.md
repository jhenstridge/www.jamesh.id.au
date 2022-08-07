---
title: 'Clipboard Manager'
slug: clipboard-manager
date: 2005-05-25T18:33:02+08:00
draft: false
tags: ['Gnome']
---

[Phillip](http://pvanhoof.be/blog/index.php/2005/05/25/31-the-save_targets-atom):
the majority of applications have no cut and paste code in them --- they
rely on the cut and paste behaviour of the standard widgets. Since the
standard widgets like `GtkEntry` in GTK 2.6 mark their selections as
being savable (in fact, any code that calls `gtk_clipboard_set_text()`
will have its selection marked as savable). Most of the remaining cases
are ones where you\'d want to be selective in what gets saved (e.g.
selecting cell ranges in Gnumeric, or regions of images in Gimp), so
need to be handled specially anyway.

So if you have a desktop running with GTK 2.6 and have a clipboard
manager running, saving of clipboard contents will just work. With
similar changes to Qt, Mozilla and OpenOffice you cover pretty much
everything the user will come into contact with. For extra points, patch
Xt and Xaw, and you\'ll get most of the ancient X programs as well.

As for the use of GTK in Anders\' sample clipboard manager, I\'m not
sure what the problem is here --- the important thing is the protocol,
which is not GTK specific. I would expect that most desktop environments
will provide their own clipboard manager, possibly integrated into some
existing desktop component such as `gnome-settings-daemon`. Then again,
they could just use a standalone clipboard manager like Anders\' one if
they want.

Lastly, you brought up console programs again. I see this as a red
herring for the following reasons:

-   There needs to be a single synchronisation point that states who
    owns the clipboard. This is to ensure that there is at most one
    owner of the clipboard, and allows paste requests get the right
    data.
-   If you want to interoperate with the X clipboard, you\'ll need to
    allow X to control the clipboard ownership. So if some app is
    connected to your clipboard daemon, the daemon will need to assert
    ownership of the X clipboard on behalf of the application.
-   If the console app is going to have to be modified to talk to a
    clipboard server, what is the benefit of making the program depend
    on your clipboard daemon instead of bypassing it and using Xlib?
    Conversely, if the console app doesn\'t want to talk to an X server,
    what makes you think it will want to talk to some other clipboard
    daemon?

The remainder of your points seem to either fall under the subject of
standardisation of clipboard formats (not directly related to clipboard
managers), or things that can be experimented with using the clipboard
manager spec.

---
### Comments:
#### [liljencrantz](http://roo.no-ip.org/fish) - <time datetime="2005-05-26 23:38:10">4 May, 2005</time>

I don\'t understand what the problem is with the current clipboard and
console programs. Any program, including console based ones can just
connect to the X server and use the clipboard. If the issue is
dependance on X headers, you can just use an external application to do
it for you. I have done just that in a shell I have written, called fish
(<http://roo.no-ip.org/fish>). Using \^K and \^Y moves text to the
clipboard and pastes from the clipboard. This is done by calling an
external application called xsel (Not written by me), which is a
commandline based clipboard manipulation tool.

I pointed this out on the xdg mailing list when this exact conversation
was started by Phillip about a month ago, but everyone was to busy
solving the problem to notice that it never existed in the first place.

---
