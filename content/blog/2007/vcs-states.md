---
title: 'States in Version Control Systems'
slug: vcs-states
date: 2007-12-04T18:32:05+09:00
tags: ['Bazaar']
---

[Elijah](http://blogs.gnome.org/newren/) has been writing an interesting
series of articles comparing different version control systems. While
the previous articles have been very informative, I think the [latest
one](http://blogs.gnome.org/newren/2007/12/01/the-concepts-a-user-must-learn-to-understand-existing-vcses/)
was a bit muddled. What follows is an expanded version of my comment on
that article.

Elijah starts by making an analogy between text editors and version
control systems, which I think is quite a useful analogy. When working
with a text editor, there is a base version of the file on disk, and the
version you are currently working on which will become the next saved
version.

This does map quite well to the concepts of most VCS\'s. You have a
working copy that starts out identical to a base tree from the branch
you are editing. You make local changes and eventually commit, creating
a new base tree for future edits.

In addition to these two \"states\", Elijah goes on to list three more
states that are actually orthogonal to the original two. These
additional states refer to certain categorisations of files within the
working copy, rather than particular versions of files or trees. Rather
than simplifying things, I believe that mingling the two concepts
together is more likely to cause confusion. I think this is evident from
the fact that the additional states do not fit the analogy we started
with.

**Versioned and Unversioned Files**

If you are going to use a version control system seriously, it is worth
understanding how files within a working copy are managed. Rather than
thinking of a flat list of possible states, I think it is helpful to
think of a hierarchy of categories. The most basic categorisation is
whether a file is versioned or not.

Versioned files are those whose state will be saved when committing a
new version of the tree. Conversely, unversioned files exist in the
working copy but are not recorded when committing new versions of the
tree.

This concept does not map very well to the original text editor analogy.
If text editors did support such a feature, it would be the ability to
add paragraphs to the document that do not get stored to disk when you
save, but would persist inside the editor.

**Types of Versioned Files**

There are various ways to categorise versioned files, but here are some
fairly generic ones that fit most VCS\'s.

1.  unchanged
2.  modified
3.  added
4.  removed

Each of these categorisations is relative to the base tree for the
working copy. The *modified* category contains both files whose contents
have changed and whose metadata has changed (e.g. files that have been
renamed).

The *removed* category is interesting because files in this category
don\'t actually exist in the working copy. That said the VCS knows that
such files did exist, so it knows to delete the files when committing
the next version of the tree.

**Types of Unversioned Files**

There are two primary categories for unversioned files:

1.  ignored
2.  unknown

The *ignored* category consists of unversioned files that the VCS knows
the user does not want added to the tree (either through a set of
default file patterns, or because the user explicitly said the file
should be ignored). Object files and executables built from source code
in the tree are prime examples of files that the user would want to
ignore.

The *unknown* category is a catch-all for any other unversioned file in
the tree. This is what Elijah referred to as \"limbo\" in his article.

**Differences between VCS\'s**

These concepts are roughly applicable to most version control systems,
but there are differences in how the categories are handled. Some of the
areas where they differ are:

-   **Are newly created files in the working copy counted as *added* or
    *unknown*?**\
    Some VCS\'s (or configurations of VCS\'s) don\'t have a concept of
    unknown files. In such a system, newly created files will be treated
    as *added* rather than *unknown*.
-   **Are *unknown* files allowed in the working copy when
    committing?**\
    One of the issues Elijah brought up was forgetting to add new files
    before commit. Some VCS\'s avoid this problem by not letting you
    commit a tree with *unknown* files.
-   **When renaming a versioned file, does it count as a single
    *modified* file, or a *removed* file and an *added* file?**\
    This one is a basic question of whether the VCS supports renames or
    not.
-   **If I delete a versioned file, is it put in the *removed* category
    automatically?**\
    With some VCS\'s you need to explicitly tell them that you are
    removing a file. With others it is enough to delete the file on
    disk.

These differences are the sorts of things that affect the workflow for
the VCS, so are worth investigating when comparing different systems.

---
### Comments:
#### Jan Schmidt - <time datetime="2007-12-04 19:35:41">4 Dec, 2007</time>

There are also questions of directory management parallel to the file
management.

---
#### James Henstridge - <time datetime="2007-12-04 21:31:41">4 Dec, 2007</time>

In my defence, I will claim that directories are just a special type of
file :)

Some version control systems may be better at managing changes to files
than directories though.

---
#### [Erigami](http://piepalace.ca/blog) - <time datetime="2007-12-05 00:26:36">5 Dec, 2007</time>

I like your categorization, but it\'s worth remembering that rename is a
special type of move. Substitute \"move\" for \"rename\" throughout your
article and your accuracy will improve somewhat. =)

---
