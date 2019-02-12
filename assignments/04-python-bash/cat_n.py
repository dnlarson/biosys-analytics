#!/usr/bin/env python3
"""Programm that catenates"""

import os
import sys

def main():
    
    args = sys.argv[1:]

    if len(args) < 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    
    text = open(file)
    line_number = 1
    for line in text:
        print('    ' + str(line_number) + ": " + line, end = '')
        line_number += 1

main()







