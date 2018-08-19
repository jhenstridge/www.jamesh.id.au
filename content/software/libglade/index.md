---
title: "Libglade"
date: 2005-02-11T00:00:00+08:00
draft: false
---

Libglade was a library that took user interfaces designed with the
[GLADE user interface builder](https://glade.gnome.org/), and then
instantiated them at runtime.

<!--more-->

When I started the project, the only way to use GLADE user interfaces
was by generating C source code.  In contrast, Libglade made it
possible to test out interface changes without even recompiling the
program.

Libglade can also automatically connect signal handlers in the user
interface.  It does this by matching handler names specified in the
glade file with symbols in the executable looked up with the dynamic
linker (this requires that applications be linked with the
`--export-dynamic` flag).

A minimal libglade program in C looks like this:

{{< highlight C >}}
#include <gtk/gtk.h>
#include <glade/glade.h>

void
some_handler(GtkWidget *widget)
{
    /* a handler referenced by the glade file.  Must not be static
     * so that it appears in the global symbol table. */
}

int
main(int argc, char **argv)
{
    GladeXML *xml;
    GtkWidget *widget;

    gtk_init(&argc, &argv);
    xml = glade_xml_new("filename.glade", NULL, NULL);

    /* get a widget (useful if you want to change something) */
    widget = glade_xml_get_widget(xml, "widgetname");

    /* connect signal handlers */
    glade_xml_signal_autoconnect(xml);

    gtk_main();

    return 0;
}
{{< /highlight >}}

There are also [Python bindings]({{< ref "/software/pygtk/index.md"
>}}) for libglade.  This makes a nice rapid application development
system.  The Python equivalent of the above program is:

{{< highlight python >}}
import gtk
import gtk.glade

def some_handler(widget):
    pass

xml = gtk.glade.XML('filename.glade')
widget = xml.get_widget('widgetname')
xml.autoconnect({
  'some_handler': some_handler
})
gtk.main()
{{< /highlight >}}

## Downloads

Libglade can be downloaded from ftp.gnome.org or its mirrors:

https://download.gnome.org/sources/libglade/

Libglade is no longer maintained, as its functionality has been folded
into GTK in the form of the [GtkBuilder
class](https://developer.gnome.org/gtk3/stable/GtkBuilder.html).
