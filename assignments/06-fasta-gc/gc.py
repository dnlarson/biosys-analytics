#!/usr/bin/env python3
"""Calculate GC content of sequence"""

import os
import sys
import argparse
from Bio import SeqI0
from collections import Counter

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_args():
        """get_arguments"""

        parser = argparse.ArgumentParser(
                description = 'Segregate FASTA sequences by GC content',
                formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    
        parser.add_argument(
                'fasta', help='Input FASTA file(s)', nargs = '+', type = str, metavar='FILE')
 
        parser.add_argument(
                '-o',
                '--outdir',
                help='Output directory (default: out)',
                type = str,
                default = None,
                metavar = 'DIR',
                )
        parser.add_argument(
                '-p',
                '--pct_gc',
                help='Dividing line fore percent GC',
                default= 50,
                metavar='int',
                type=int,
                )
        
        return parser.parse_args()
              
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
        
        args = get_args()
        fasta = args.fasta
        out_dir = args.outdir
        pct_gc = args.pct_gc
        percent_gc = args.pct_gc


        if not 1 <= percent_gc <= 100:
                die('{} must be in between 0 and 100'.format(pct_gc))
        count = 0

        if os.path.exits(file):
                os.makedirs(out_dir)
        

        for num, file in enumerate(fasta, start =1):
                if not os.path.isfile(file):
                        warn('{} is not a file'.format(file))
                        continue
                basename = os.path.basename(file)
                root, ext = os.path.splitext(basename)
                print('{}: {}'.format(num, basename))

                high_file = open(os.path.join(out_dir, root + '_high' + ext), 'wt')
                low_file = open(os.path.join(out_dir, root + '_low' + ext), 'wt')
                
                #GC content
                with open(file) as fil:
                        for record in SeqI0.parse(fil, 'fasta'):
                                seq_len = len(record.seq)
                                nuc = Counter(record.seq)
                                gc_num = nucs.get('G', 0) + nucs.get('C', 0)
                                gc = int(gc/seq_len *100)
                                if gc >= pct_gc:
                                        SeqI0.write(record,high_file, 'fasta')
                                else:
                                        SeqI0.write(record,low_file, 'fasta')
                                count += 1
        print('Done, wrote {} sequences to out dir "{}"'.format(count, out_dir))

          

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