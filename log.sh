#!/usr/bin/env bash
#
# bash script to log text to the current date's entry.
# Inputs:
#   [TEXT_TO_APPEND]
#

PAGE=`date --rfc-3339=date`

if [ "$#" == "1" ]; then
    # append argument
    exec append.py $PAGE $1
else
    # append the vim buffer
    exec append.py $PAGE
fi

