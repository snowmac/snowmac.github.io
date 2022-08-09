#!/usr/bin/env bash
timestamp=$(date +'%Y-%m-%d')

if [[ $# -eq 0 ]] ; then
    echo "Please provide a title of the post"
    echo "for example run the command like this:"
    echo "./draft.sh I wrote a fancy bash program"
    echo "The file name then becomes: _drafts/$timestamp-I-wrote-a-fancy-bash-program.md"
    exit 1
fi

argumentsAsString="$*"
hypened="${argumentsAsString// /-}"
filename="_drafts/$timestamp-$hypened.md"

touch $filename

echo "---" >> $filename
echo "layout: post" >> $filename
echo "title: \"$*\"" >> $filename
echo "date: $(date +'%Y-%m-%d')" >> $filename
echo "categories: " >> $filename
echo "---" >> $filename
echo "" >> $filename
#subl $filename