#!/usr/bin/env python3
"""Python Password"""


import argparse
import os
import re
import sys


#-----------------------------------------------------------
def main():
    """main"""

    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    p1, p2 = args


    if p1 == p2:
        print('ok')
    elif p1.capitalize() == p2:
        print('ok')
    elif p1.upper() == p2:
        print('ok')
    elif re.search('.?' + p1 + '.?', p2):
        print('ok')
    else:
        print('nah')




# --------------------------------------------------
if __name__ == '__main__':
    main()