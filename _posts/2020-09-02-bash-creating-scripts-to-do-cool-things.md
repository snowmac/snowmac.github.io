---
layout: post
title: "bash creating scripts to do cool things"
date: 2020-09-02
categories: bash system
---

Bash is awesome. Specific, useful, sadly can't use it on windows; but its a powerful tool. I wrote a script to allow me to easily generate markdown files in the correct format with all the correct inside guts, so I can quickly & easily write blog posts. Doing things allows me to forget about "How do I format the document? Whats the right file naming convention?" to "Lets write, I'm feeling inspired". 

# Script Sharing: The script I use to create a post

Example usage: `./post.sh Bash creating scripts to do cool things`

`#!/usr/bin/env bash`

Basic entry to any bash script. 

`timestamp=$(date +'%Y-%m-%d')`

Store the formatted time stamp into a variable

`argumentsAsString="$*"`

this allows me to take a string like 'Bash creating scripts to do cool things' which is used in the URL and file name; as well as title. 
`hypened="${argumentsAsString// /-}"`

Format the file name using regex 

`filename="_posts/$timestamp-$hypened.md"`

Create the file name location in a variable 

`touch $filename`

Create the file for real

`echo "---" >> $filename`

Add starting format to the file

`echo "layout: post" >> $filename`

Default layout is post; I don't have anything else. 

`echo "title: \"$*\"" >> $filename`

Add the title, eg: 'Bash creating scripts to do cool things'

`echo "date: $(date +'%Y-%m-%d')" >> $filename`

Have to have a time stamp 

`echo "categories: " >> $filename`

Left blank, but this is part of the URL generation. 

`echo "---" >> $filename`

End header file

`echo "" >> $filename`

Add white space / new line to the file

`#subl $filename`

I used to use Sublime, now I use VS Code. I have not enabled the CLI usage. 

# Full file

Here's the full thing for the post generator: 

```bash 
#!/usr/bin/env bash
timestamp=$(date +'%Y-%m-%d')
argumentsAsString="$*"
hypened="${argumentsAsString// /-}"
filename="_posts/$timestamp-$hypened.md"

touch $filename

echo "---" >> $filename
echo "layout: post" >> $filename
echo "title: \"$*\"" >> $filename
echo "date: $(date +'%Y-%m-%d')" >> $filename
echo "categories: " >> $filename
echo "---" >> $filename
echo "" >> $filename
#subl $filename
```

# Other things worth sharing 

## Automatically push posts to github

Usage: `./push.sh`

```bash 
git add .; git commit -m "adding a post"; git push;
```