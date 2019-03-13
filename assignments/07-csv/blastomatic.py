#!/usr/bin/env python3
"""CSV Parsing"""


"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 24 October 2018
Purpose: Python program to write a Python program
"""

import argparse
import os
import sys
import csv
from collections import defaultdict

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files', help='Blast output (-outfmt 6)', type=str, metavar = 'FILE')

    parser.add_argument(
        '-a',
        '--annotations',
        metavar = 'FILE',
        help='Annotation file',
        type = str,
        default = '')

    parser.add_argument(
        '-o',
        '--outfile',
        metavar = 'FILE',
        help='Output file',
        type=str,
        default = '')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """main"""
    
    args = get_args()
    annotations = args.annotations
    outfile = args.outfile
    files = args.files

    for file_name in [files, annotations]:
        if not os.path.isfile(file_name):
            die('"{}" is not a file'.format(file_name))
    
    annot_dict = {}
    with open(annotations) as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            seqID = row['centroid']
            annot_dict[seqID] = row
    # print(annot_dict)

    field_names = "qaccver saccver pident length mismatch gapopen qstart qend sstart send evalue bitscore".split()

    outfile = open(outfile, "w") if outfile else sys.stdout
    header = ['seq_id', 'pident', 'genus', 'species']
    outfile.write('\t'.join(header) + '\n')
        
   
    with open(files) as tabfile:
        reader = csv.DictReader(tabfile, delimiter = '\t', fieldnames= field_names)
        for row in reader:
            seqID =row['saccver']
            if seqID not in annot_dict:
                warn('Cannot find seq "{}" in lookup'.format(seqID))
                continue
            new_dict = annot_dict.get(seqID)
            genus = new_dict.get('genus') or 'NA'
            species = new_dict.get('species') or 'NA'
            pident = row['pident']
            outfile.write('\t'.join([seqID, pident, genus, species]) + '\n')
        


    # print('// ****** Record 1 ****** //')        
    # print('\t'.join([ 'seqID: ', seqID]))
    # for seqID, count in annot_dict.items():
    #     print('\t'.join([str(count), seqID]))
            # die(annot_dict)


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# # --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
if __name__ == '__main__':
    main()
