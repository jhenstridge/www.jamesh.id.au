---
title: 'First Thoughts on NewsBruiser'
slug: first-thoughts-on-newsbruiser
date: 2005-05-19T06:36:30+08:00
---

I\'ve moved my diary over to `blogs.gnome.org`, which offers a few extra
features over advogato (the main ones I\'m interested in are more
control over the layout, and the ability to embed images). Overall it
seems pretty good, although I have a few gripes:

-   The login cookie gets set for the path `/nb.cgi/` only, so when I go
    to the front page of my diary, which is not under that path due to
    some `mod_rewrite` magic, it never thinks I\'m logged in.
-   My login cookie gets sent to all pages under `/nb.cgi/`, including
    other hosted blogs. Given that I can put arbitrary HTML in the
    templates for my blog, it would be possible to capture the passwords
    of other NewsBruiser users on the system without much trouble (it\'s
    a good thing we all trust each other). This one is a bit difficult
    to fix because of the URI structure for newsbruiser pages, which
    look like \"`/nb.cgi/verb/username/...`\". If they were structured
    with the username first, it would be trivial to set up the cookie so
    it only gets sent when viewing one particular blog.

Overall though, it seems quite nice.
