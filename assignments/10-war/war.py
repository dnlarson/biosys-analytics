#!/usr/bin/env python3
"""War Card Game"""


import argparse
import sys
import random
from itertools import product
import re  #regular expressions

# --------------------------------------------------
def get_args():
    """get arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
        '-s',
        '--seed',
        metavar = 'int',
        help='Random seed',
        type= int,
        default = None)

    return parser.parse_args()

# --------------------------------------------------
def main():
    """main"""
    args = get_args()
    seed = args.seed

    if seed is not None:
        random.seed(seed)

    suits = list('♥♠♣♦')   #string
    vals = list(map(str, range(2,11))) + list('JQKA')                                       
    cards = sorted(map(lambda t: '{}{}'.format(*t),product(suits,vals))) #for the test suite to start from the same starting pt
    
    random.shuffle(cards)
    
    p1_win = 0
    p2_win = 0
    # draws = 0

    card_val = dict(list(map(lambda t: list(reversed(t)), enumerate(list(vals)))))

    while len(cards) > 0:
        p1_cards = cards.pop()
        p2_cards = cards.pop()
        # print(p1_cards,p2_cards)
        val1 = card_val[p1_cards[1:]]
        val2 = card_val[p2_cards[1:]]

        # if p1_cards[1:] > p2_cards[1:]:
        if val1 > val2:
            p1_win += 1
            print('{:>3} {:>3} {}'.format(p1_cards, p2_cards,'P1'))
        # elif p2_cards[1:] > p1_cards[1:]:
        elif val1 < val2:
            p2_win += 1 
            print('{:>3} {:>3} {}'.format(p1_cards, p2_cards, 'P2'))
        else:
            print('{:>3} {:>3} {}'.format(p1_cards, p2_cards, 'WAR!'))

    if p1_win > p2_win:
        print('P1 {} P2 {}: Player 1 wins'.format(p1_win, p2_win))
    elif p2_win > p1_win:
        print('P1 {} P2 {}: Player 2 wins'.format(p1_win, p2_win))
    else:
        print('P1 {} P2 {}: DRAW'.format(p1_win, p2_win))

    # cards = []
    # for i in ['\u2663', '\u2660', '\u2666', '\u2665']:
    #     for j in range(2,11):
    #         cards.append(str(j) + i)
    #     for j in ("J", "Q", "K", "A"):
    #         cards.append(str(j) + i)
    # return cards
    

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