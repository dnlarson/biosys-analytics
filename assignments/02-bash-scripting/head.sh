#!/bin/bash

if [ $# -eq  0 ]
then
	echo "Usage: head.sh FILE"
	exit 1
fi

INPUT_FILE=$1
NUM_ITERATIONS=3

if [[ ! -f "$INPUT_FILE" ]]; then
    echo "$INPUT_FILE is not a file"
	exit 1
fi

if [[ $# -gt 1 ]]; then
    NUM_ITERATIONS=$2
fi

i=0
while read -r LINE; do
    if [[ $i -eq $NUM_ITERATIONS ]]; then
        break
    fi
    i=$((i+1))
    echo "$LINE"
done < "$INPUT_FILE"