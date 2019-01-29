#!/bin/bash


if [ $# -eq  0 ]
then
	echo "Usage: cat-n.sh FILE"
	exit 1
fi

INPUT_FILE=$1

if [[ ! -f $INPUT_FILE ]]; then
	echo "$INPUT_FILE is not a file"
	exit 1
fi

i=0
while read -r LINE; do
	i=$((i+1))
	echo "$i $LINE"

done < "$INPUT_FILE"

