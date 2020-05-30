---
title: 'Live and die by the keyboard: How to be more productive!'
date: 2016-01-28T06:00:26+00:00
author: adam.bourg@gmail.com
layout: post
permalink: /2016/01/28/use-aliases/
image: /wp-content/uploads/2016/01/2117746551_0b45d97535_b-825x510.jpg
categories:
  - git
  - productivity
  - thoughts
  - thursday
tags:
  - aliases
  - git
  - sublime
  - zsh
---
I live and die by the keyboard. The keyboard is my friend and it&#8217;s way faster to use an application using a keyboard then it is to use a mouse. In fact there are many <a href="http://dl.acm.org/citation.cfm?id=1978942.1979351&coll=DL&dl=GUIDE" target="_blank">studies</a> that show that for non-complex key combinations keyboard shortcuts and aliases are much faster then using the mouse.

**Git Aliases**

If you&#8217;re a Git addict like me, you should know about <a href="http://gitready.com/intermediate/2009/02/06/helpful-command-aliases.html" target="_blank">git</a> <a href="http://githowto.com/aliases" target="_blank">configuration</a>. This allows you to create shortcuts to common things that you use often. In my home directory, I have a .gitconfig file with the following contents:

> [alias]

> st = status

> ck = checkout

> ckb = checkout

> sta = stash apply

> sth = stash

While small, I find the things I most often do in git is switch branches, git status and modifying stashes.

**Zsh Aliases / Command line aliases**

Another source of aliases I use is for <a href="http://zsh.sourceforge.net/Intro/intro_8.html" target="_blank">Zsh</a> _(Zee Shell)_, for this you can do the following:

> alias commandShortCut = &#8220;commandToRun&#8221;

One nasty one I often have to run is to drop the local database in rails, recreate it and seed it with data. This is very long and a pain to type often:

> bundle exec rake db:drop db:create db:migrate db:seed;

My shortcut command for this is:

> ber

To set &#8220;ber&#8221; I used:

> alias ber=&#8221;bundle exec rake db:drop db:create db:migrate db:seed;&#8221;

**Sublime Aliases**

In <a href="https://www.sublimetext.com/" target="_blank">Sublime</a> Aliases are known as Snippets. <a href="http://docs.sublimetext.info/en/latest/extensibility/snippets.html" target="_blank">Snippets</a> are used as apart of the code complete portion of sublime.

To create a snippet in sublime, go to Tools > New Snippet. From there it&#8217;ll give you a template to work with:

> <snippet>

> <content><![CDATA[

> Hello, ${1:this} is a ${2:snippet}.

> ]]></content>

> <!&#8211; Optional: Set a tabTrigger to define how to trigger the snippet &#8211;>

> <!&#8211; <tabTrigger>hello</tabTrigger> &#8211;>

> <!&#8211; Optional: Set a scope to limit where the snippet will trigger &#8211;>

> <!&#8211; <scope>source.python</scope> &#8211;>

> </snippet>

It&#8217;s basically XML or HTML, uncomment the tab trigger and customize what you want to use to tab complete to auto fill in. Within the CDATA part, right where hello is, that is where you can put a tab completed item. Scope allows you to control what document scope you will trigger the snippet in.

Here&#8217;s an example I use for lorem ipsum text, the file is saved at &#8220;packages/users&#8221; within the sublime library as lorem.sublime-snippet:

> <snippet>

> <content><![CDATA[

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vehicula blandit neque, nec ullamcorper leo hendrerit pretium. Morbi turpis risus, finibus sodales velit a, sagittis pharetra nibh. Nullam ultrices dolor in dolor mattis, imperdiet facilisis velit sagittis. Ut dapibus eleifend felis quis consectetur. Aenean sodales lorem ac urna efficitur egestas. Vivamus nec posuere lorem, vitae feugiat quam. Praesent venenatis mattis libero, in dapibus mi molestie sed. Vestibulum mollis leo lorem. Suspendisse id consequat enim, et facilisis diam. Nullam mattis lectus ligula, ac suscipit dui elementum ut. Sed egestas laoreet rutrum. Curabitur vel ex id quam porta vestibulum. Sed hendrerit orci nisl, eu aliquet ante venenatis eu. Praesent vel dapibus velit, eget ultricies ex.
>
> ]]></content>

> <tabTrigger>lorem</tabTrigger>

> </snippet>

There you have it, 3 really great examples of using aliases / snippets in git, sublime and zsh. Using these is sure to make your workflow faster and easier, especially on a Mac or Linux computer!
