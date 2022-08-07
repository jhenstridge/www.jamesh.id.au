---
title: '3 August 2004'
slug: 3-august-2004
date: 2004-08-04T04:16:19+08:00
---

**Fahrenheit 9/11**

Went to see [Fahrenheit 9/11](http://www.imdb.com/title/tt0361596/) on
Monday night. It was an interesting movie, but it was clearly aimed at a
US audience. It did have a fair bit of information I hadn\'t heard
before, but in some areas he was obviously choosing which bits of
information to include to increase the effect (eg. when listing the
countries in the \"coallition of the willing\" he didn\'t list Britain).
Other bits seemed particularly relevant like the bit about the Bush
administration playing with the terror alert apparently for political
reasons, given what has happened so far this week.

Overall, I thought it was a good movie.

**Firefox**

Firefox is quite a nice browser, but the toolbars seem to have too much
padding round the buttons in the toolbar. It looks like this is due to
the double padding round the back and forward buttons.

It looks a bit better after creating a `chrome/userChrome.css` file in
the profile directory containing the following:

> `@namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul"); .toolbarbutton-1, .toolbarbutton-menubutton-button {   padding: 5px !important; } .toolbarbutton-menubutton-button {   margin: -1px 0px -1px -1px !important; } .toolbarbutton-1[type="menu-button"] {   padding: 0px !important; }`

You might need to adjust the negative margins to match the
xthickness/ythickness of your GTK theme in order to make it look okay.

The other cool thing is that some people are working on adding [GTK
stock icon support](http://bugzilla.mozilla.org/show_bug.cgi?id=233461)
to the Mozilla code base. While the initial focus of this is to add
stock icons to buttons in the dialogs, it sounds like it could be
extended to toolbar buttons and other places in the future. This would
make it fit in on the Gnome desktop a lot better.
