#!/usr/bin/env python3
"""Reads in first line of contents"""

import os
import sys
import argparse

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description = 'Find directory name(s)',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-w',
        '--width',
        help = 'width space of each line',
        type = int,
        metavar = "int",
        default = 50,
        )
    parser.add_argument(
        'directory',
        help = 'directory name(s)',
        type = str,
        metavar = "DIR",
        nargs = '+',
        )    
    
    return parser.parse_args()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():

    args = get_args()
    width = args.width
    period = '.' * width     #number of periods in between line and line number

    for directory in args.directory:   
        if not os.path.isdir(directory):
            print('"{}" is not a directory'.format(directory), file = sys.stderr)
            continue       #skip for-loop if a directory
    
        dir_dict = {}
        print(directory)
    

        for file in os.listdir(directory):
            path = os.path.join(directory, file)
            line = open(path).readline().rstrip()  #read in line and remove white space to the right
            dir_dict[line] = file

        for line, file in sorted(dir_dict.items()):  #return list of tuples
            lines = len(line)
            files = len(file)
            period = '.'*(width - lines - files)
            # print(len(line))
            print('{:5} {} {}'.format(line, period, file))
    

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":
    main()
    

    




