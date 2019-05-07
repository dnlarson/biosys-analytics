#!/usr/bin/env python3
"""
Author : Danielle Larson
Date   : 2019-05-06
Purpose: Pig Latin
"""

import os
import argparse
import re
import string
import sys

def get_args():
    parser = argparse.ArgumentParser(
        description='Covert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        'STR',
        help='Input text or file',
        action = 'store',
        type = str,
        metavar='STR')
    
    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    STR = args.STR


    words= []
 
    if os.path.isfile(STR):
        words = open(STR, "r").read()
    else:
        words = STR
    #print(words)

    for line in words.split('\n'):
        for word in line.split():
            new_word = re.sub("[^a-zA-Z0-9']", '', word)
            consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
            match = re.match('^([' + consonants + ']+)(.+)', new_word)
            #print(word)
            if match:
                print('-'.join([match.group(2), match.group(1) + 'ay']), end=' ')
            else:
                print(new_word + '-yay', end=' ')
        print()



    #             for lines in f:
    #                 for word in lines.split():
    #                     new_word = re.sub("[^a-zA-Z0-9']", '', word)
    #                     consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    #                     match = re.match('^([' + consonants + ']+)(.+)', new_word)
    #                     if match:
    #                         print('-'.join([match.group(2), match.group(1) + 'ay']))
    #                     else:
    #                         print(word + '-ay')
    #     else:
    #         continue
            
    # for word in STR:
    #     new_word = re.sub("[^a-zA-Z0-9']", '', word)
    #     consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    #     match = re.match('^([' + consonants + ']+)(.+)', new_word)
    #     if match:
    #         print('-'.join([match.group(2), match.group(1) + 'ay']))
    #     else:
    #         print(word + '-ay')

    
    #2nd CASE (Read from a FILE)

    # if not os.path.isfile(FILE):
    #     die('"{}" is not a file'.format(FILE))

    # with open(FILE, "r") as f:
    #     for lines in f:
    #         for word in lines.split():
    #             consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
    #             match = re.match('^([' + consonants + ']+)(.+)', word)
    #             if match:
    #                 print('-'.join([match.group(2), match.group(1) + 'ay']))
    #             else:
    #                 print(word + '-ay')



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stdout)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)

# --------------------------------------------------
if __name__ == "__main__":
    main()