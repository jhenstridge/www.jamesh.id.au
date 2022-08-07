---
title: 'Nautilus Extensions'
slug: nautilus-extensions
date: 2004-12-03T12:26:49+08:00
draft: false
tags: ['Gnome']
---

One of the changes in the Gnome 2.9 development series is the removal of
most of the Bonobo code from Nautilus, which results in a speed boost
due to lower complexity and less IPC overhead. This had the effect of
breaking existing bonobo based context menus, property pages and views.
The first two can be converted to the Nautilus extension interface, but
the second has no equivalent in the new code (partly because Nautilus is
concentrating on being a file manager these days rather than a universal
component shell like it was in the early days).

Two of the casualties of the change were `gnome-control-center`\'s font
and theme code, and `nautilus-media`. Since I wrote the font browser
code in `gnome-control-center`, I updated it to work again. It isn\'t
clear whether `nautilus-media` will be updated, since the view was a
major component of it, and most of the remaining functionality is
provided by `totem`.

> **Context Menus**
>
> If you are looking at updating a Nautilus context menu to use the new
> extension interface,
> [`fontilus-context-menu.c`](http://cvs.gnome.org/viewcvs/gnome-control-center/vfs-methods/fontilus/fontilus-context-menu.c?view=markup)
> is a pretty good example to model your code on.
>
> One of the big differences is the way Nautilus extensions are loaded
> compared to the old context menu API. With the old API, you would
> provide a Bonobo component and set a number of properties in the
> `bonobo-activation` server file listing a menu label, the list of mime
> types the context menu applies to, what URI schemes it supports and
> whether it supports multiple files. Nautilus could then do a single
> `bonobo-activation` query to find out what context menu items
> correspond to the current selection, and add them to the menu. If the
> user selected one of the items, the corresponding component would be
> activated, and an event sent to its `Bonobo::EventListener` interface.
>
> In contrast, Nautilus extensions are initialised on Nautilus startup.
> They indicate that they provide context menu items by implementing the
> `NautilusMenuProvider` interface. When the user brings up the context
> menu, the `get_file_items` method will be called on all extensions
> that implement that interface. A list of `NautilusFileInfo` objects is
> passed in, and the method returns a list of `NautilusMenuItem`
> objects. Also, Nautilus extensions are run in-process while Bonobo
> components could be written for in-process or out of process use.
>
> One of the benefits of this system is the added control of when to
> display a menu item, and what to use as the label. If you want to only
> display your context menu item when 42 `text/html` files and one
> `image/png` file are selected you can. However it does mean that each
> new extension causes some code to be run before popping up a context
> menu. I have no idea how this compares time wise to the time taken for
> the previous `bonobo-activation` query though.
>
> **Property Pages**
>
> The interface for property pages is quite similar to the context menu
> interface. As with context menus, you have an imperative
> `NautilusPropertyPageProvider::get_pages` interface rather than a
> declaritive interface based on activation properties. This has the
> benefit that you can simply not provide the page when the properties
> in question are not available for the file (with the old setup, you\'d
> end up providing a properties page stating that there is nothing to
> display).

The other interesting parts of the extension interface is the
`NautilusInfoProvider` interface that lets you attach extra information
to files, such as extra emblems or custom attributes, and
`NautilusColumnProvider`, which lets you provide additional columns for
the list view that map to custom file attributes. One example of this is
[`nautilus-vcs`](http://cvs.gnome.org/viewcvs/nautilus-vcs/), which can
show revision numbers for files in CVS working copies and adds emblems
indicating the file state.

Of course, there are downsides to the extension interface too --- since
extensions are always in process, they can crash Nautilus or leak
memory. However, it was already possible for Bonobo based extensions to
do this if they were designed as in-process components and badly written
\...

Another issue is that language bindings might find it more difficult to
support the extension interface where the language runtime would have to
cooperate with Nautilus, compared to out of process Bonobo components
where they have more control. I guess we\'ll see what happens.
