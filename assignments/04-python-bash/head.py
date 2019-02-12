#!/usr/bin/env python3

import os
import sys

def main():

    args = sys.argv[1:]

# #If there are no argument
    if len(args) != 1:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

# #If first argument is not a file
    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)

#Check if input number if positive (non-zero)
    line_number = 3

    if len(args) == 2:
        line_number = int(args[1])
        if line_number <= 0:
            print('lines {} must be a positive number'.format(line_number))
            sys.exit(2)
    
    text = open(file)
    count = 0

    for line in text:
        count += 1
        print('{}'.format(line), end = '')
        if count == line_number:
            break

main()
