---
title: 'Thoughts for Thursday: Lazy rebasing'
date: 2015-09-24T07:00:25+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2015/09/24/thoughts-for-thursday-lazy-rebasing/
categories:
  - git
  - thoughts
  - thursday
tags:
  - git
  - lifehacks
  - thought
  - thoughts for thursday
---
Rebasing is extremely useful, lets say you branched off of release 1.8.3 and need to fix a defect, but it wasn&#8217;t completed until 1.8.3 was already on production and 1.8.4 is the new hotness. git rebase release1.8.4 defectBranchName will take defectBranchName and reapply the commits over release1.8.4&#8217;s history instead of what it was originally based off of.

The problem is if there are conflicts and sometimes there can be conflicts at every commit. So if possible, what I do is:

> git checkout defectBranchName

> git log

At git log, count the number of commits you made on the branch, N = number of commits to go back

> git reset HEAD~N &#8211;soft

> git stash

> git rebase release1.8.4

> git stash apply

Now you fix the merge conflicts, and commit. The downside is you lose commit history and can create issues if you do this on something like master because you&#8217;ll be changing history. It&#8217;ll be especially big impact if you work on a team and do this on develop or master, but your little feature branch should be ok if no branched off it.

Now there you go, a handy little trick to quickly get synced up with history!
