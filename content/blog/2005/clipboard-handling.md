---
title: 'Clipboard Handling'
slug: clipboard-handling
date: 2005-06-20T15:40:39+08:00
draft: false
tags: ['Gnome']
---

[Phillip:](http://pvanhoof.be/blog/index.php/2005/06/19/38-desktop-integration-tomorrow)
your idea about direct client to client clipboard transfers is doable
with the current X11 clipboard model:

1.  Clipboard owner advertises that it can convert selection to some
    special target type such as \"client-to-client-transfer\" or
    similar.
2.  If the pasting client supports client to client transfer, it can
    check the list of supported targets for the
    \"client-to-client-transfer\" target type and request conversion to
    that target.
3.  The clipboard owner returns a string containing details of how to
    request the data (e.g. hostname/port, or some other scheme that only
    works for the local host).
4.  Pasting application contacts the owner out of band and receives the
    data.

Yes, this requires modifications to applications in order to work
correctly, but so would switching to a new clipboard architecture.

With respect to your no-transfer cut/paste of a movie example, that\'s
more of a component architecture problem than a clipboard issue. In the
context of Bonobo, it can be done provided that the clipboard owner can
provide the data as a Bonobo Embeddable, and the pasting application can
embed Bonobo Embeddables in its documents:

1.  Clipboard owner advertises that it can convert the selection to the
    target \"BONOBO\_EMBEDDABLE\" (or some other agreed upon targer
    name).
2.  Pasting application requests that the selection be converted to
    \"BONOBO\_EMBEDDABLE\", and receives an IOR for the component.
    Pasting application owns a reference on the component due to the
    clipboard transfer.
3.  Pasting application `queryInterface()`\'s the component to the
    `Bonobo::ControlFactory` interface, and calls the `createControl()`
    method to create a control to embed in the document.
4.  When it comes time to save the data, the component can be converted
    to one of the `Bonobo::Persist` interfaces, and written out.

Of course, there are reasons why people don\'t do this (apart from not
liking Bonobo), including:

-   With the classic X selection model, you don\'t need to special case
    local or remote transfer cases.
-   Works in cases where the two applications can only communicate via
    the X connection (e.g. in the presence of transparent X proxies such
    as `ssh`).
-   It delegates all the permissions/authentication issues to the X
    server.
