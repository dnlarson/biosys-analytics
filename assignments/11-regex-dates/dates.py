#!/usr/bin/env python3
"""Date Parsing"""


import argparse
import os
import re
import sys
# from datetime import date

#-----------------------------------------------------------
def main():
    """main"""

    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]

    date_re1 = re.compile('(\d{4})'            # group 1
                            '[-]?'             # sep
                            '(\d{1,2})'        # group 2
                            '[-]?'             # sep
                            '(\d{1,2})?'       # group 3
    )  
    
    date_re2 = re.compile('(\d{4})'             # group 1
                             '[/]'              # sep
                             '(\d{1,2})'        # group 2
                             '[/]'              # sep
                             '(\d{1,2})?'       # group 3
    ) 
    
    date_re3 = re.compile('([a-zA-Z]{1,10})'    # group 1
                            '[/,-]?'            # sep
                            '\s*?'              # space
                            '(\d{2,4})'         # group 3
    )        


    # match1 = date_re1.search(date)
    re1 = re.compile('(?P<year>\d{4})'
                      '-'
                      '(?P<month>\d{1,2})'
                      '(-(?P<day>\d{1,2}))?')
    
    re2 = re.compile('(?P<year>\d{4})'
                      '(?P<month>\d{2})'
                      '(?P<day>\d{2})')
    
    re3 = re.compile('(?P<month>\d{1,2})'
                      '[/-]'
                      '(?P<year>\d{2})'
    )
    re4 = re.compile('(?P<month>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'
                     '[,-]\s*'
                      '(?P<year>\d{4})'
    )
    re5 = re.compile('(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)'
                     '[,-]\s*'
                      '(?P<year>\d{4})'
    )
    
    match1 = re1.match(date) or re2.match(date) or re3.match(date)
    match2 = re4.match(date)
    match3 = re5.match(date)

    small_months = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'.split()
    num = dict(map(reversed, enumerate(small_months, 1)))

    long_months = 'January February March April May June July August September October November December'.split()
    num2 = dict(map(reversed, enumerate(long_months, 1)))


    
    if match1:
        date_dict = match1.groupdict()
        day = date_dict.get('day') or '01'
        year = date_dict.get('year')
        if len(year) == 2:
            year = '20'+ year
        print('{}-{:02d}-{:02d}'.format(year, int(match1.group('month')), int(day)))
    elif match2:
        date_dict = match2.groupdict()
        year = date_dict.get('year')
        month = date_dict.get('month')
        print("{}-{:02d}-01".format(year, num.get(month)))
    elif match3:
        date_dict = match3.groupdict()
        year = date_dict.get('year')
        month = date_dict.get('month')
        print("{}-{:02d}-01".format(year, num2.get(month)))
    else:
        print('No match')
        
        





   


    # if match:
    #     day = match1.group('day') or '01'
    #     print("{}-{}")


    # for d in dates:
    #     match = date_re1.match(date) or date_re2.match(date)
    #     x = '{}-{}-{}'.format(match.group(1), match.group(2), match.group(3 if match else 'miss'))
    #     print(x)

# --------------------------------------------------
if __name__ == '__main__':
    main()







