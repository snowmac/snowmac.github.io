#!/usr/bin/env bash
# Create a post in _ready/ scheduled to publish on a future date.
# The Daily Post Publisher GitHub Action moves it into _posts/ once
# that date arrives (or run the workflow manually to publish early).

if [[ $# -lt 2 ]] ; then
    echo "Usage: ./ready.sh YYYY-MM-DD Title of the post"
    echo "Example: ./ready.sh 2026-10-01 I launched something cool"
    echo "The file name then becomes: _ready/2026-10-01-I-launched-something-cool.md"
    exit 1
fi

publish_date="$1"
shift

if ! [[ "$publish_date" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]]; then
    echo "First argument must be a date in YYYY-MM-DD format, got: $publish_date"
    exit 1
fi

argumentsAsString="$*"
hypened="${argumentsAsString// /-}"
filename="_ready/$publish_date-$hypened.md"

touch "$filename"

echo "---" >> "$filename"
echo "layout: post" >> "$filename"
echo "title: \"$*\"" >> "$filename"
echo "date: $publish_date" >> "$filename"
echo "categories: " >> "$filename"
echo "---" >> "$filename"
echo "" >> "$filename"

echo "Created $filename — will publish on $publish_date"
