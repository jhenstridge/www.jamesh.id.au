---
title: 'Shared Branches using Bazaar and Launchpad'
slug: shared-branches-using-bazaar-and-launchpad
date: 2006-08-17T20:20:46+08:00
tags: ['Bazaar', 'Launchpad']
---

Earlier, [David Allouche](http://ddaa.net/blog/)\
described [how to\
host Bazaar branches on
Launchpad](http://ddaa.net/blog/launchpad/bzr-hosting). At the end, he
alluded to the\
ability to create branches that can be committed to by anyone on a\
team. I\'ll describe how this works here.

**Launchpad Teams**

[Launchpad](https://launchpad.net/) allows people to organise
themseleves into teams. Most\
of the things people can do in Launchpad can also be done by teams,\
including owning branches.

You can create a new team at the following page:

> `https://launchpad.net/people/+newteam`

There are three different membership policies you can choose\
from:

-   **Open**: anyone can join. Choosing this sort of team\
    effectively gives everyone write access to branches owned by the\
    team.
-   **Moderated**: new memberships must be approved by one of the\
    administrators (this is the default policy). This makes it easy for\
    people to request commit access to the branch while still requiring\
    approval from a team administrator..
-   **Restricted**: new members can only be added by the team\
    administrators. This is appropriate if new members shouldn\'t be
    able\
    to propose themselves normally.

Once the team has been created, members of the team can create the\
branches.

**Uploading a Team Owned Branch**

Now that you are a member of a team, you can upload branches to\
that team\'s directory on `bazaar.launchpad.net`. This is done\
in the same way as uploading personal branches described in [David\'s\
article](http://ddaa.net/blog/launchpad/bzr-hosting):

    cd branchdir
    bzr push --create-prefix sftp://bazaar.launchpad.net/~teamname/product/branchname

When the command completes, the team owned branch will have been\
created. Now you can treat this branch like a personal branch, but\
once someone else pushes a commit to the branch, \"`bzr push`\"\
will tell you that the branch has diverged, and not let you push your\
changes until you merge them to your branch.

An alternative model is to use checkouts, which provide a workflow\
closer to CVS and Subversion without losing Bazaar\'s ability to work\
while disconnected.

**Bazaar Checkouts**

A Bazaar checkout is a local working copy bound to a remote branch\
such that changes are committed to the remote location. The remote\
branch data is also cached locally to speed up local operations and\
allow you to work while disconnected from the network. A checkout of\
the previously created team branch can be created with the following\
command:

    bzr checkout sftp://bazaar.launchpad.net/~teamname/product/branchname team-branch
    cd team-branch

Alternatively if you still have the local branch used to create\
the team branch, it can be converted to a checkout with the
\"`bzr bind`\" command:

    cd branchdir
    bzr bind sftp://bazaar.launchpad.net/~teamname/product/branchname

You can then make commits to the checkout as you would with any\
other branch, provided the checkout is up to date with the remote\
branch. If another team member has committed to the branch in the\
mean time though, you will be prompted to update your checkout to the\
head of the latest version of the remote branch.

If this happens, the checkout can be updated by issuing the\
\"`bzr update`\" command. You can then retry the commit, after\
fixing any conflicts that are reported.

**Disconnected Operation with Checkouts**

If you are disconnected from the network, it will be impossible to\
publish your changes to the remote branch so running the
\"`bzr commit`\" command on the checkout will fail.

To handle this situation, Bazaar lets you make local commits in\
your checkout. This is performed with the \"`bzr commit --local`\"
command. You can treat these commits just like regular\
commits and get diffs between them, etc.

When you are connected to the network again, run \"`bzr update`\". This
will pull in any changes made to the remote branch\
and turn your local commits into a pending merge. After fixing any\
conflicts (if there are any), running \"`bzr commit`\" will\
publish the changes to the remote branch for the world to see.

**Feature Branches**

If you are developing a feature that is not yet appropriate to\
check into the mainline team branch, the checkout workflow may not be\
convenient. In this case, it may make sense to create a personal\
branch to do the work and then merge the changes later on.

You can create a new branch using the \"`bzr branch`\"\
command. Since the checkout made previously contains full history\
data we can branch from it directly, which saves saves downloading the\
branch again:

    bzr branch checkoutdir mybranch

If you want to make this branch available to others, it can be\
published to `bazaar.launchpad.net` as described in David\'s\
original article.

Merging your branch into the checkout is the same as merging into\
any other Bazaar branch:

    bzr update
    bzr merge mybranch
    # resolve any conflicts that may be reported
    bzr commit

Once the commit completes, the changes will be available on the\
team branch.

**Conclusion**

Without much trouble, you can create a shared mainline branch with
Bazaar and Launchpad and use it in a way familiar to Subversion users.
With one extra command you can extend the familiar model to allow
commits while disconnected, providing the power of distributed revision
control when you need it.
