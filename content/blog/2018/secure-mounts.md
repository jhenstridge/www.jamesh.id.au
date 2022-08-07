---
title: 'Performing mounts securely on user owned directories'
slug: secure-mounts
date: 2018-04-19T18:47:14+08:00
tags: ['Linux', 'Ubuntu']
---

While working on a feature for snapd, we had a need to perform a
\"secure bind mount\". In this context, \"secure\" meant:

1.  The source and/or target of the mount is owned by a less privileged
    user.
2.  User processes will continue to run while we\'re performing the
    mount (so solutions that involve suspending all user processes are
    out).
3.  While we can\'t prevent the user from moving the mount point, they
    should not be able to trick us into mounting to locations they
    don\'t control (e.g. by replacing the path with a symbolic link).

The main problem is that the mount system call uses string path names to
identify the mount source and target. While we can perform checks on the
paths before the mounts, we have no way to guarantee that the paths
don\'t point to another location when we move on to the `mount()` system
call: a classic [time of check to time of
use](https://en.wikipedia.org/wiki/Time_of_check_to_time_of_use) race
condition.

One suggestion was to modify the kernel to add a `MS_NOFOLLOW` flag to
prevent symbolic link attacks. This turns out to be harder than it would
appear, since the kernel is documented as ignoring any flags other than
`MS_BIND` and `MS_REC` when performing a bind mount. So even if a
patched kernel also recognised the `MS_NOFOLLOW`, there would be no way
to distinguish its behaviour from an unpatched kernel. Fixing this
properly would probably require a new system call, which is a rabbit
hole I don\'t want to dive down.

So what can we do using the tools the kernel gives us? The common way to
reuse a reference to a file between system calls is the file descriptor.
We can securely open a file descriptor for a path using the following
algorithm:

1.  Break the path into segments, and check that none are empty, `"."`,
    or `".."`.
2.  Open the root directory with `open("/", O_PATH|O_DIRECTORY)`.
3.  Open the first segment with
    `openat(parent_fd, "segment", O_PATH|O_NOFOLLOW|O_DIRECTORY)`.
4.  Repeat for each of the remaining file descriptors, closing parent
    descriptors as needed.

Now we just need to find a way to use these file descriptors with the
mount system call. I came up with two strategies to achieve this.

**Use the current working directory**

The first idea I tried was to make use of the fact that the mount system
call accepts relative paths. We can use the `fchdir` system call to
change to a directory identified by a file descriptor, and then refer to
it as `"."`. Putting those together, we can perform a secure bind mount
as a multi step process:

1.  `fchdir` to the mount source directory.
2.  Perform a bind mount from `"."` to a private stash directory.
3.  `fchdir` to the mount target directory.
4.  Perform a bind mount from the private stash directory to `"."`.
5.  Unmount the private stash directory.

While this works, it has a few downsides. It requires a third
intermediate location to stash the mount. It could interfere with
anything else that relies on the working directory. It also only works
for directory bind mounts, since you can\'t `fchdir` to a regular file.

Faced with these downsides, I started thinking about whether there was
any simpler options available.

**Use magic `/proc` symbolic links**

For every open file descriptor in a process, there is a corresponding
file in `/proc/self/fd/`. These files appear to be symbolic links that
point at the file associated with the descriptor. So what if we pass
these `/proc/self/fd/NNN` paths to the mount system call?

The obvious question is that if these paths are symbolic links, is this
any different than passing the real paths directly? It turns out that
there is a difference, because the kernel does not resolve these
symbolic links in the standard fashion. Rather than recursively
resolving link targets, the kernel short circuits the process and uses
the path structure associated with the file descriptor. So it will
follow file moves and can even refer to paths in other mount namespaces.
Furthermore the kernel keeps track of deleted paths, so we will get a
clean error if the user deletes a directory after we\'ve opened it.

So in pseudo-code, the secure mount operation becomes:

    source_fd = secure_open("/path/to/source", O_PATH);
    target_fd = secure_open("/path/to/target", O_PATH);
    mount("/proc/self/fd/${source_fd}", "/proc/self/fd/${target_fd}",
          NULL, MS_BIND, NULL);

This resolves all the problems I had with the first solution: it
doesn\'t alter the working directory, it can do file bind mounts, and
doesn\'t require a protected third location.

The only downside I\'ve encountered is that if I wanted to flip the bind
mount to read-only, I couldn\'t use `"/proc/self/fd/${target_fd}"` to
refer to the mount point. My best guess is that it continues to refer to
the directory shadowed by the mount point, rather than the mount point
itself. So it is necessary to re-open the mount point, which is another
opportunity for shenanigans. One possibility would be to read
`/proc/self/fdinfo/NNN` to determine the mount ID associated with the
file descriptor and then double check it against `/proc/self/mountinfo`.
