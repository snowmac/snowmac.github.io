---
layout: post
title: "Help! My ssh is still prompting for a password"
date: 2021-01-11
categories: SSH bash shell
---

Recently, after 3 years of prodding, begging and asking I was assigned a Macbook Pro at work. Normally, when I work at a company, they hand developers a useful computer, not this client. This client I work for, gave me a Brand New To Me Dell Laptop on my first day. Welp, warm welcome. They didn't care it took almost a month to setup the machine. Welp, 3 years of nagging has shown me that finally good things come to those who are persistent enough. 

Now, with the new Macbook, I can do fancy things like have SSH configurations for the hours I spent connected to and working on remote servers. 

The trouble is, using SSH in the past has always been: remember the user name, password and IP address; then log in, spend a few minutes fiddling with the password and finally get in. Welp, not any more. 

# Enter SSH config 

In `~/.ssh/config` you can set custom ssh config. So instead of using `ssh adam.bourg@192.168.2.2` you can do something like `ssh az_demo_app`, which will connect you to the remote, passwordless (using a key file). This has totally changed my productivity. AMAZING. 

*Example SSH config:*

```bash 
Host az_demo_app
  User adambourg
  HostName 123.18.19.42
  Port 22
  IdentityFile ~/.ssh/id_ed25519
```

Here's the problem, since rediscovering this nifty tool, I've been using `ssh-copy-id` to copy up my SSH keys. The trouble is when I log in, some systems will still prompt for a password. If that's happening to you, I'm here to help you. 

SSH into the remote machine, then `cd ~/.ssh/`. Then do a `ls -al`, if you see anything other then `-rwx------` on `~/.ssh/authorized_keys` then thats the problem. SSH wants authorized keys to only be readable by YOU, on that remote system. It's an easy fix, though, run `chmod 700 ~/.ssh/authorized_keys`. This command will set it to read, write and execute for just you. This is what the SSH tool is expecting. Now logout and try again. This should work. 
