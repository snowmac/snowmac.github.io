---
layout: post
title: "Chrome Dev Tools In Depth"
date: 2020-05-29
categories: 
---

# Chrome Dev Tools In Depth

Welcome to my first real post in 2020. This is hybrid post, part post, part video and part notes. I'm writing this as mostly notes for the students at [Redwood Code Academy](https://redwoodcodeacademy.com/); I'm giving a demo for a friend of mine, [Abdul](https://www.linkedin.com/in/abdul-sarnor/). 

# Why use in browser dev tools? 

Why? Why? Why? I'm going to start sounding like a 2 year old. Well, when you're doing any kind of development that the user could interact with, be it, APIs or UIs, using dev tools will help you immensely. 

Not only does the dev tools have a debugger, but it can change code on the fly, you can inspect & record network traffic, you can analyse performance of an application, you can do many more things including attach to a Node JS application running locally or remote, and debug dynamically. 

# How to open dev tools?

There are a few ways: 

1. Right click, then click "inspect". This takes you to the element viewer. 
2. Keyboard Shortcut (Mac: Command Option i), (Windows: Control Shift i)
3. View > Developer > Developer Tools

# Its open, now what? 

![Standard Dev Tools Bar](/assets/img/5-29-chrometools-nav.png)

First you have the navigation bar. This has a few useful tabs:

* Elements 
* Console 
* Sources
* Network 
* Performance 
* Memory 
* Application 
* Security
* Audits 

These 9 panels allow you to thoroughly debug and improve your application quickly and easily. Since this guide is focused on beginners, we're going to focus on Elements, Console and Network; which I find to be the most useful. We will also explore application. 

# First, elements. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/VDcwnu5pb8s" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This is perhaps the most powerful tool of them all. With it you can do many things, you can first dig into the source code, change attributes on the fly, you can also change values on the fly. 

# Console 

<iframe width="560" height="315" src="https://www.youtube.com/embed/vcYlt26g35M" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The console is a powerful tool, from testing out parsing scripts to debugging. It is incredibly helpful. 

# Network 

<iframe width="560" height="315" src="https://www.youtube.com/embed/5u77nUugAEk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You can record traffic, play it back, see network traffic over timeline and inspect values sent to the server

# Final Thoughts

More details to come, more notes. I'll add a few more videos: debugger, nodejs debugging and application; stay tuned. 
