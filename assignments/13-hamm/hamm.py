#!/usr/bin/env python3
"""Hamming Distance"""

import argparse
import logging
import os
import re
import sys

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE', help='FILE inputs', nargs = 2, type = str)

    parser.add_argument(
        '-d',
        '--debug',
        action='store_true',
        dest='debug',
        help = 'Debug',
        default = False)


    return parser.parse_args()

# --------------------------------------------------
def dist(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    
    distance = 0
    if(len(s1) == len(s2)):
        return sum(el1 != el2 for el1, el2 in zip(s1, s2))
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            if(s1[i] != s2[i]):
                distance += 1
        distance += len(s2) - len(s1)
        return distance
    elif len(s1) > len(s2):
        for i in range(len(s2)):
            if(s1[i] != s2[i]):
                distance += 1
        distance += len(s1) - len(s2)
        return distance

# --------------------------------------------------
def test_dist():
    """dist ok"""
    tests = [('foo', 'boo', 1), ('foo', 'faa', 2), ('foo', 'foobar', 3),
             ('TAGGGCAATCATCCGAG', 'ACCGTCAGTAATGCTAC',
              9), ('TAGGGCAATCATCCGG', 'ACCGTCAGTAATGCTAC', 10)]

    for s1, s2, n in tests:
        d = dist(s1, s2)
        assert d == n
# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    debug = args.debug
    FILE = args.FILE        #file1[0] and file2[1]

  
    for input_file in FILE:
        if not os.path.isfile(input_file):
            die('"{}" is not a file'.format(input_file))

    #logging to DEBUG
    logging.basicConfig(
    filename='.log',
    filemode='w',
    level=logging.DEBUG if args.debug else logging.CRITICAL
    )


    s1 = FILE[0]
    s2 = FILE[1]

    logging.debug('file1 = {}, file2 = {}'.format(s1, s2))

    total_distance = 0
    with open(s1, 'r') as f1, open(s2, 'r') as f2:
        words1 = f1.read().split()
        words2 = f2.read().split()

        L = 0
        if(len(words1) < len(words2)):
            L = len(words1)
        else:
            L = len(words2)

        i = 0

        for i in range(L):
            word1 = words1[i]
            word2 = words2[i]

            distance = dist(word1, word2)
            logging.debug('s1 = {}, s2 = {}, d = {}'.format(word1, word2, distance))
            
            total_distance += distance

        print(total_distance)



    
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