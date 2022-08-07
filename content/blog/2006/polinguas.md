---
title: 'po/LINGUAS'
slug: polinguas
date: 2006-04-12T06:13:14+08:00
---

One issue that was meantioned as a [Gnome
Goal](http://live.gnome.org/GnomeGoals) was to switch packages to use a
[`po/LINGUAS`](http://live.gnome.org/GnomeGoals/PoLinguas) file.

The idea makes sense --- translators only need to edit a simple text
file to add a new translation to an application, rather than having to
modify the `configure.in`/`configure.ac` file without breaking things.
Unfortunately, the suggested way of supporting this is a pretty big
hack. A better long term solution would be to use the upstream gettext
macros and `po/Makefile.in.in` infrastructure.

For a Gnome module that doesn\'t use intltool, the following steps
should work.

Make sure the module is being built with Automake 1.8 or 1.9. If it
isn\'t, upgrade to 1.9.

Create an `m4` subdirectory in your project if it doesn\'t exist, add it
in CVS and then create and add a `m4/.cvsignore` file (there are a
number of files that will get created here by gettext that you don\'t
want to check into CVS).

Mark the m4 subdirectory as the macro dir in the `configure.ac` file:\

    AC_CONFIG_MACRO_DIR([m4])

And make sure that the macro dir gets checked if the makefile reruns
aclocal:

    AC_SUBST([ACLOCAL_AMFLAGS], ["-I $ac_macro_dir \${ACLOCAL_FLAGS}"])

If you aren\'t using the `gnome-common` `autogen.sh` script, you will
also need to make sure that aclocal is called with \"`-I m4`\".  If
you are using the `gnome-common` script, then this will happen
automatically.

Remove the `AM_GLIB_GNU_GETTEXT` call from `configure.ac` and replace
it with:

    AM_GNU_GETTEXT([external])
    AM_GNU_GETTEXT_VERSION([0.14.1])

If you aren\'t using the `gnome-common` `autogen.sh` script, change
the call to `glib-gettextize` to `autopoint`, and make sure it gets
run before `aclocal` (again, unneeded if you are using the
`gnome-common` script).

Now rerun `autogen.sh` so that `autopoint` gets run. This should
result in a number of files getting created under `m4`, and some new
files under `po`.

Copy `po/Makevars.template` to `po/Makevars` and customise the
variables. You might want to set `DOMAIN` to `$(GETTEXT_PACKAGE)`
rather than `$(PACKAGE)`. Add this new file in CVS.

Update `po/LINGUAS` from the `ALL_LINGUAS` variable in `configure.ac`,
and then remove the `ALL_LINGUAS` definition. Add `po/LINGUAS` to CVS.

Finally update `m4/.cvsignore` and `po/.cvsignore` to ignore the new
generated files.

As I said at the start, this change is only appropriate for apps not
using `intltool`, since `intltool` overwrites the `po/Makefile.in.in`
file with an incomaptible version.

To get things working with `intltool`, I believe it would make most
sense to modify intltool as follows:

-   Make `intltool` provide some commands that are command line
    argument compatible with `xgettext` and `msgmerge`.
-   Make `IT_PROG_INTLTOOL` alter `XGETTEXT` and `MSGMERGE` with
    the appropriate intltool functions.
-   Don\'t overwrite `po/Makefile.in.in`.
-   If additional makefile rules are needed in the `po`
    subdirectory, install a `po/Rules-intltool` file containing
    them. The gettext M4 macros will include them into the
    resulting Makefile.

---
### Comments:
#### jonner - <time datetime="2006-04-12 21:44:50">3 Apr, 2006</time>

Wait, is this different from dobey\'s desktop-devel post where he says
all you need to do is use intltool from cvs and then remove ALL\_LINGUAS
from configure.ac and add po/LINGUAS?

---
#### al_shopov - <time datetime="2006-04-12 22:07:15">3 Apr, 2006</time>

Hi James,\
Could you please post some more information about the whole
libtool/autoconf/automake (LT/AC/AM) stuff.\
I have tried to find information - how-to\'s, general help etc. but I
have found it too diffucult to grasp. Do you know some docs that I could
use to bootstrap myself out of my coplete newbishness concerning
(LT/AC/AM)?\
An additional source with docs for M4 would be even more helpful.\
I am sorry to bother you personally, but you seem to have passed the
levels I want to achieve. How didi you do it?

Kind regards:\
al\_shopov

---
