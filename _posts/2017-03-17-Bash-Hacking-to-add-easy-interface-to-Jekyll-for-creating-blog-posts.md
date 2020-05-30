---
layout: post
title: Bash Hacking to add easy interface to Jekyll for creating blog posts
---

I'm a big fan of command line tools, I live by the command line, I do my job by the command line. I hate with a passionate fire, copying and pasting text. When I switched to Jekyll for my blog, I decided I needed a command line tool to generate the blog posts in the correct format so I can get layout, title and the correct file name structure.

To achieve this I wrote this [bash script](https://github.com/snowmac/personalsite/blob/master/newPost.sh)

```bash
#!/usr/bin/env bash
timestamp=$(date +'%Y-%m-%d')
argumentsAsString="$*"
hypened="${argumentsAsString// /-}"
filename="_posts/$timestamp-$hypened.md"

touch $filename

echo "---" >> $filename
echo "layout: post" >> $filename
echo "title: $*" >> $filename
echo "---" >> $filename
```

Basically this script takes the current year, month and day, formats them and joins them with your arguments using a hyphen. This is great because to run you just do something like

> ./newPost Bash Hacking to add easy interface to Jekyll for creating blog posts

Which generates a file:

> _posts/2017-03-17-Bash-Hacking-to-add-easy-interface-to-Jekyll-for-creating-blog-posts.md

I love this, because all I have to do is edit, commit and push, bam! I've written a new post easily. No hosting, no SQL injection, no Wordpress updates. Just write in Sublime and I'm done.
