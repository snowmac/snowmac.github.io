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