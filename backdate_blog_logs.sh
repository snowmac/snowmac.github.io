#!/bin/bash

# Configuration
USER_NAME="Adam Bourg"
USER_EMAIL="adam.bourg@gmail.com"
FILE="contribution_logs.txt"
START_YEAR=2019
END_YEAR=2024

# Set git user
git config user.name "$USER_NAME"
git config user.email "$USER_EMAIL"

# Loop through each year
for year in $(seq $START_YEAR $END_YEAR)
do
    # Number of days in the year
    days=365
    # Simplistic leap year check
    if [ $((year % 4)) -eq 0 ] && ([ $((year % 100)) -ne 0 ] || [ $((year % 400)) -eq 0 ]); then
        days=366
    fi

    for day in $(seq 1 $days)
    do
        # macOS specific date math: start at Jan 1st of that year and add (day-1) days
        # We'll use the year and day to construct a date
        # date -j -f "%Y %j" "2019 001" "+%Y-%m-%d"
        DATE_STR=$(date -j -f "%Y %j" "$year $(printf "%03d" $day)" "+%Y-%m-%d")
        
        # Random number of commits between 2 and 7
        NUM_COMMITS=$(( ( RANDOM % 6 ) + 2 ))
        
        for (( j=1; j<=$NUM_COMMITS; j++ ))
        do
            # Random hour/min/sec
            H=$(( RANDOM % 24 ))
            M=$(( RANDOM % 60 ))
            S=$(( RANDOM % 60 ))
            TIMESTAMP="$DATE_STR $(printf "%02d:%02d:%02d" $H $M $S)"
            
            # Log entry
            echo "Contribution check at $TIMESTAMP" >> $FILE
            
            # Stage and commit with backdated timestamp
            git add $FILE
            GIT_AUTHOR_DATE="$TIMESTAMP" GIT_COMMITTER_DATE="$TIMESTAMP" git commit -m "Contribution log: $TIMESTAMP" --quiet
        done
        
        # Log progress every 100 days
        if [ $((day % 100)) -eq 0 ]; then
            echo "Processed $DATE_STR"
        fi
    done
done

echo "Finished backdating logs for 2019-2024."
