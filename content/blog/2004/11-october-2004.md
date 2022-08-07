---
title: '11 October 2004'
slug: 11-october-2004
date: 2004-10-11T09:54:43+08:00
draft: false
tags: ['Gnome']
---

[**Federal Election**](http://vtr.aec.gov.au/)

Looks like we are going to have at least another three years with [The
Rodent](http://www.johnhoward.com.au/). It also looks like they will
have a majority in the senate, which will reduce the senate\'s
effectiveness as a house of review.

We might not have John Howard for the entire term though, since he is of
retirement age. NineMSN seems to think that [Peter Costello is already
the leader](http://news.ninemsn.com.au/article.aspx?id=15411).

It also looks like [The Democrats](http://www.democrats.org.au) senators
up for reelection got completely wiped out, with much of their support
going to [The Greens](http://www.greens.org.au/).

**Gnome-VFS**

Robert Collins wrote an [interesting critique on the gnome-vfs
API](http://www.advogato.org/person/robertc/diary.html?start=22). I
don\'t agree with all the points, and there are some reasons why the API
isn\'t as elegant as it could be. Below are some responses.

> **Initialisation**
>
> One thing that `gnome_vfs_init()` does is to call `g_thread_init()`.
> Before this function is called, the locking APIs in glib are no-ops.
> You really want this function called early on if the app is going to
> use threads, otherwise you will end up with inconsistencies (eg. a
> `lock()` call might be a no-op, but the `unlock()` call might not be
> if `g_thread_init()` is called in between).
>
> The other issue is that `gnome_vfs_init()` can fail. If it is called
> automatically, then any function that might invoke the initialisation
> routine now has a new failure mode. I don\'t know whether this is a
> real problem or not though.
>
> **Calling Style - Inconsistent Ordering**
>
> One big difference between the out parameters in `gnome_vfs_open()`
> and `gnome_vfs_read()` is that the first function is essentially a
> constructor for a file handle, while the second is a method for a file
> handle that fills in a provided buffer.
>
> I\'ll agree that the calling conventions are not as nice as they could
> be though. If they were being designed today, I suspect that they
> would look more like this:
>
>     GnomeVFSHandle  *gnome_vfs_open (const gchar     *text_uri,
>                                      GnomeVFSOpenMode open_mode,
>                                      GError         **error);
>     GnomeVFSFileSize gnome_vfs_read (GnomeVFSHandle  *handle,
>                                      gpointer         buffer,
>                                      GnomeVFSFileSize bytes,
>                                      GError         **error);
>
> Unfortunately, the `GError` API was not developped til the 2.0 series,
> while these parts of the gnome-vfs API persist from the 1.x days.
>
> **Calling Style - Inconsistent Method Naming**
>
> I agree that the `gnome_vfs_truncate()` function name is inconsistent.
> My guess as to why they chose `gnome_vfs_truncate` and
> `gnome_vfs_truncate_handle()` was to match the underlying `truncate()`
> and `ftruncate()` C library calls. This was probably a case of
> balancing consistent APIs with ease of transition from libc APIs to
> gnome-vfs APIs.
>
> **Returning data to pointers**
>
> I agree that the existing calling convention is not as nice as it
> could be. As I said earlier, it would probably have been designed to
> use `GError` if it was being developed today.
>
> The `GError` API has a number of benefits over `errno` style ones,
> including:
>
> 1.  Automatically threadsafe. The place where the error is reported is
>     on the stack. A global variable is a problem for multi threaded
>     apps on systems without Linux 2.6 style thread local storage (you
>     need to do tricks like making `errno` into a function that returns
>     the appropriate variable for the current thread).
> 2.  In Robert\'s example, the actual error information is looked up
>     from a file handle. What do you do if there is no file handle
>     involved in the function call? Also, wouldn\'t `gnome_vfs_open()`
>     return a `NULL` file handle on error?
> 3.  For the cases where there is a file handle to look up the error
>     info on, what happens if two threads are working with the file
>     handle at the same time?
> 4.  `GError` is consistent with other Gnome APIs `:)`
>
> The `GError` API also makes it easy to pass error data up a number of
> call frames similar to exceptions. If your function has a `GError`
> argument, you can simply pass that same error object to other
> functions when you call them. If those functions fail on an error,
> simply return immediately, and the caller can handle the error.
>
> **Streams Interface**
>
> There actually is a stream interface available in one of the libraries
> both GTK and gnome-vfs depend on: `GIOChannel`. I guess it would be
> nice if gnome-vfs provided a `GIOChannel` implementation for VFS file
> handles. The main thing that would be needed here would be the
> `io_create_watch()` implementation, which would probably require
> exposing a file descriptor to poll on (this could probably be
> implemented using a pipe pretty easily).
>
> Doing this as GObject interfaces isn\'t really an option, since
> `GIOChannel` is implemented in `libglib` which is below `libgobject`,
> and gnome-vfs file handles aren\'t GObjects. I know that at one point
> Ian was planning to change the various handles to GObjects, but this
> didn\'t happen. It would probably be possible to do this kind of
> change while only requiring changes to VFS methods, so it can\'t be
> completely ruled out.
>
> **Directory Interface**
>
> You can asynchronously load a directory listing using
> `gnome_vfs_async_load_directory()`. I don\'t blame you for missing it
> --- the organisation of the APIs in the various headers is a bit
> confusing.
>
> **Language Bindings**
>
> There are a lot of things a language binding can do to make gnome-vfs
> nicer to use. Some of these things include:
>
> -   If the language provides exceptions, convert error
>     `GnomeVFSResult`\'s to exceptions and change the calling
>     conventions to something more sane.
> -   If the language allows for runtime type checking or multiple
>     dispatch, don\'t wrap the `gnome_vfs_foo()` and
>     `gnome_vfs_foo_uri()` functions separately. Instead, just check if
>     a string or a `GnomeVFSURI` was passed in and do the right thing.
> -   If the language has a standard file handle interface or
>     convention, try to implement it in the binding.
>
> The Python bindings do some of these things, and definitely make
> things easier to use.
