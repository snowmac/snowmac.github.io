---
layout: post
title: "running ubuntu on a work windows laptop"
date: 2020-06-09
categories: os windows ubuntu sysadmin devops
---

Suppose you're a developer, on your first day of a new job you're handed not a MacBook Pro but instead a Dell or HP laptop. You go into denial, question your manager and learn that almost no one, developers included, at the firm use anything but Windows. But there is good news, they give you local admin privileges. This is where I found myself 2 and half years ago at my job, the job I now love. I considered quitting on the spot, but decided to give it a try; heck they were PAYING me to set it up... 

# Why for Ubuntu on Windows through the sub system 

First of all, I would not choose Windows for my primary NodeJS development environment, but if I have to use Windows there are a myriad of tools that support development and allow you to be effective at your job. These tools include Git Bash, VS Code, Postman, Chrome and most importantly Windows Linux Sub System. 

My use case for the sub system is limited to one application I need: Redis. I need redis. I cannot work without the latest version of Redis. Sure there ARE [redis for windows](https://redislabs.com/ebook/appendix-a/a-3-installing-on-windows/a-3-2-installing-redis-on-window/), but Redis is massively out of date for Windows. 

Why not Vmware, Virtual Box, Docker, Vagrant? I've tried all of the above, while they are good tools, they are painful. Each option requires you to configure ports, files, file sync, proxing and a whole host of other options. There is NOT a simple run these 5 commands and have a TOOL that works everytime that is BRAIN DEAD simple within these options. 

# The How

I'm assuming you have admin privileges, if not; good luck to you getting this installed because it won't work. Taking my info from two [key](https://docs.microsoft.com/en-us/windows/wsl/install-win10) [articles](https://docs.microsoft.com/en-us/windows/wsl/install-manual) from Microsoft, here is what you need to do. I'm also making the assumption that your employer blocks access to the Microsoft App store for windows; but is **not** a deal breaker for installing Linux. 

Open power shell as an admin, then run the following command to enable the WSL (Window Subsystem for Linux):
```shell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

Once the command above is done, restart your computer. 

Now time to download your flavor of Linux; you can see your choices on the [MS site](https://docs.microsoft.com/en-us/windows/wsl/install-manual). Here is [Ubuntu 18 download](https://docs.microsoft.com/en-us/windows/wsl/install-manual). Once that is downloaded, open Powershell again as an admin and navigate to the folder where the Ubuntu is downloaded. Once at the folder, run the following command where app_name is the name of the ubuntu version: 

```shell 
Add-AppxPackage .\app_name.appx
```

# Up and running

Once all of the above are done, the system will prompt you to create a user and password for the linux; I recommend you do this. Use a dumb password like Password123 that is easy to remember; it does not have to be secure. I would also run updates for Linux: 

```shell
sudo apt update && sudo apt upgrade
```

After setting up an account and updates; next you can easily install redis or any other tools you need using ```sudo apt install```. When you restart the system does not automatically start WSL services, to do this I recommend following [these instructions](https://dev.to/ironfroggy/wsl-tips-starting-linux-background-services-on-windows-login-3o98).