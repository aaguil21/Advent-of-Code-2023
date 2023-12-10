import os
from collections import Counter

def split_input(filename: str):
    data = [l.strip().split(' ') for l in open(filename)]
    data = [[[char for char in x[0]], int(x[1])] for x in data]

    return data

def poker_rank(hand, joker_rule=False):

    z = Counter(hand[0])
    if joker_rule:
        if 'J' in z.keys():
            y = z['J']
            z['J'] = 0
            z[max(z, key=z.get)] += y
            
    z = list(z.values())
    if max(z) == 1:
        return 1
    elif max(z) == 2 and z.count(2) == 1:
        return 2
    elif z.count(2) == 2:
        return 3
    elif max(z) == 3 and 2 not in z:
        return 4
    elif max(z) == 3 and 2 in z:
        return 5
    elif max(z) == 4:
        return 6
    else:
        return 7
    
def card_rank(x, joker_rule=False):
    CARD_RANK = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
    if joker_rule:
        CARD_RANK['J'] = 0

    return (CARD_RANK[x[0][0]], CARD_RANK[x[0][1]], CARD_RANK[x[0][2]], 
                                CARD_RANK[x[0][3]], CARD_RANK[x[0][4]] )


def sort_cards(cards, jokers=False):
    cards.sort(key= lambda x: (poker_rank(x, jokers), card_rank(x, jokers)))
    winnings = 0
    for i in range(len(cards)):
        winnings += (i+1)*cards[i][1]
    return winnings

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day07_input.txt')
    #file = split_input('test.txt')
    print(sort_cards(file))
    print(sort_cards(file, True))