#!/usr/bin/env python3
"""translate DNA/RNA to AA"""

import os
import sys
import argparse
from collections import Counter

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_args():
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations',
        dest='codons',
        action='store',
        required=True,
        default=None,
        metavar="FILE")

    parser.add_argument(
        '-o',
        '--outfile',
        help='A file with codon translations',
        dest='outfile',
        action='store',
        default="out.txt",
        metavar="FILE")

    parser.add_argument(
        'STR', help='Filename or string to count', type=str, metavar='STR')

    return parser.parse_args()

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():

    args = get_args()
    outfile = args.outfile
    codons = args.codons
    STR = args.STR.upper()


    if not os.path.isfile(codons):
        die('--codons "{}" is not a file'.format(codons))

    # string = arg[0]
    # k = 3
    # n = len(string) - k + 1

    # for i in range (0, n, k):
    #     print(string[i, i+k]

    protein_dict = {}
    output = ''


    with open(codons) as f:
        lines = f.readlines()
        
        for line in lines:
            k, v = line.split()
            protein_dict[k] = v

    for i in range(0, len(STR), 3):
        rna = STR[i:i+3] #taking 3 elements at a time

        if rna not in protein_dict:
            output += '-'
        else:
            output += protein_dict[rna]


    with open(outfile, "w") as f:
        f.write(output)
        print('Output written to "{}"'.format(outfile))


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
