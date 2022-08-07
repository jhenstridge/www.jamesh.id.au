---
title: 'Experimenting with C++ Reflection'
slug: experimenting-with-c-reflection
date: 2017-01-17T19:33:45+08:00
draft: false
---

For a number of projects I\'ve worked on at Canonical have involved
using GObject based libraries from C++. To make using these APIs easier
and safer, we\'ve developed a few helper utilities. One of the more
useful ones was a class (originally by [Jussi
Pakkenen](http://nibblestew.blogspot.com/)) that presents an API similar
to the C++11 smart pointers but specialised for GObject types [we called
`gobj_ptr`](http://bazaar.launchpad.net/~unity-team/thumbnailer/trunk/view/head:/include/internal/gobj_memory.h).
This ensures that objects are unrefed when the smart pointer goes out of
scope, and increments the reference count when copying the pointer.

However, even with the use of this class I still end up with a bunch of
type cast macros littering my code, so I was wondering if there was
anything I could do about that. With the current C++ language the answer
seems to be \"no\", since GObject\'s convention of subclasses as
structures whose first member is a value of the parent structure type is
at a higher level but then I found a paper describing an extension for
[C++ Static
Reflection](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0194r1.html).
This looked like it could help, but seems to have missed the boat for
C++17. However, there is [a sample implementation for
Clang](https://github.com/matus-chochlik/clang) written by Matus
Chochlik, so I downloaded and compiled that to have a play.

At its heart, there is a new `reflexpr()` operation that takes a type as
an argument, and returns a type-like \"metaobject\" that describes the
type. For example:

>     using MO = reflexpr(sometype);
>
> These metaobjects can then be manipulated using various helpers in the
> `std::meta` namespace. For example,
> `std::meta::reflects_same_v<MO1,MO2>` will tell you whether two
> metaobjects represent the same thing. There were a few other useful
> operations:
>
> -   `std::meta::Class<MO>` will return true if the metaobject
>     represents a class or struct (which are effectively
>     interchangeable in C++).
> -   `std::meta::get_data_members_m<MO>` will return a metaobject
>     representing the members of a class/struct.
> -   From a sequence metaobject, we can determine its length with
>     `std::meta::get_size_v<MO>`, and retrieve the metaobject elements
>     in the sequence with `std::meta::get_element_m<MO>`
> -   We can get a metaobject representing the type for a data member
>     metaobject with `std::meta::get_type_m<MO>`.
>
> Put all this together, and we\'ve got the building blocks to walk the
> GObject inheritance hierarchy at compile time. Now rather than spread
> the reflection magic throughout my code, I used it to declare a
> templated compile time constant:
>
> >     template <typename Base, typename Derived>
> >     constexpr bool is_base_of = ...
> >
> > With this, an expression like `is_base_of<GObject, GtkWidget>` will
> > evaluate true, while something like
> > `is_base_of<GtkContainer, GtkLabel>` will evaluate false.
> >
> > As a simple example, this constant could be used to implement an
> > up-cast helper:
> >
> > >     template <typename Target, typename Source>
> > >     inline Target* gobj_cast(Source* v)
> > >     {
> > >         static_assert(is_base_of<Target, Source>,
> > >                       "Could not verify that target type is a base of source type");
> > >         return reinterpret_cast<Target*>(v);
> > >     }
> > >
> > > ![](https://blogs.gnome.org/jamesh/files/2017/01/squirrelgirl-c.jpg){.alignright
> > > .size-full .wp-image-567 width="334" height="555"}If we can verify
> > > that this is a correct up-cast, this function will compile down to
> > > a simple type cast. Otherwise, compilation will fail on the
> > > `static_assert`, printing a relatively short and readable error
> > > message.
> > >
> > > The same primitive could be used for other things, such as
> > > allowing you to construct a `gobj_ptr<T>` from an instance of a
> > > subclass, or copying one `gobj_ptr` to another one representing a
> > > parent class.
> > >
> > > It\'d be nice to implement something like `dynamic_cast` for
> > > down-casting, but I don\'t think even static reflection will help
> > > us map from a struct type to the corresponding helper function
> > > that returns the `GType`.
> > >
> > > If you want to experiment with this, the code used to implement
> > > all of the above can be found in the following repository:
> > >
> > > > <https://github.com/jhenstridge/gobject-cpp-reflection>
