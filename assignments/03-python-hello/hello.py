#!/usr/bin/env python3
"""hello with many arguments"""

import sys
import os

def main():
    """main"""

args = sys.argv
# print(len(args))

if len(args) < 2:
    script = os.path.basename(args[0])
    print('Usage: {} NAME [NAME2 ...]'.format(script))
    sys.exit(1)
elif len(args) == 2:
    names = args[1]
    print('Hello to the 1 of you: ' + args[1] + '!' )
elif len(args) == 3:
    names = args[1:]
    print('Hello to the 2 of you: {}!'.format(' and '.join(names)))
elif len(args) > 3:
    names = args[1:]
    arglength= len(names)
    lastname=names.pop()
    print('Hello to the {} of you: {}, and {}!'.format(arglength,', '.join(names), lastname))


main()