#!/usr/bin/env python3
"""Bottles of beer song!!"""


import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """get arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-n',
        '--num_bottles',
        metavar = 'INT',
        type =int,
        help='How many bottles',
        default = 10)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    num_bottles = args.num_bottles

    if num_bottles < 1:
        die('N {} must be a positive integer'.format(num_bottles))

    for num_bottles in range(num_bottles,0,-1):
        if num_bottles > 2:
            print('{} bottles of beer on the wall,\n'
                  '{} bottles of beer,\n'
                  'Take one down, pass it around,\n'
                  '{} bottles of beer on the wall!\n'.format(num_bottles, num_bottles, num_bottles))
            # print(num_bottles)
        elif num_bottles == 2:
            print('{} bottles of beer on the wall,\n'
                  '{} bottles of beer,\n'
                  'Take one down, pass it around,\n'
                  '{} bottle of beer on the wall!\n'.format(num_bottles, num_bottles, num_bottles - 1))
            # print(num_bottles)
        else:
            print('{} bottle of beer on the wall,\n'
                  '{} bottle of beer,\n'
                  'Take one down, pass it around,\n'
                  '{} bottles of beer on the wall!'.format(num_bottles, num_bottles, num_bottles - 1)) 
            # print(num_bottles)
        


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)

# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
if __name__ == '__main__':
    main()
