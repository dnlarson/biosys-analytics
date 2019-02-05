#!/usr/bin/env python3
"""script to count number of vowels in a single string"""

import sys
import os

def main():
    """main"""

vowels = sys.argv

if len(vowels) != 2:
    script = os.path.basename(vowels[0])
    print('Usage: {} STRING'.format(script))
    sys.exit(1)

vowels = sys.argv[1]
count = 0

for vowel in vowels:
    if(vowel =='a' or vowel =='e' or vowel =='i' or vowel =='o' or vowel =='u' or vowel =='A' or vowel =='E' or vowel =='I' or vowel =='O' or vowel =='U'):
        count += 1
    
if count == 0:
    print('There are 0 vowels in "{}."'.format(vowels))
elif count < 2:
    print('There is 1 vowel in "{}."'.format(vowels))
else:
    print('There are {} vowels in "{}."'.format(count, vowels))

main()