import pathlib
import os
import numpy as np
from functools import reduce

# Read input
def split_input(filename: str):
    x = [l.strip().split(':') for l in open(filename)]
    cards = {}
    for i in x:
        key = int(''.join([alpha for alpha in i[0] if alpha.isdigit()]))  
        nums = i[1].split('|')
        win_nums = nums[0].split(' ')
        win_nums = set([n for n in win_nums if n.isdigit()])
        my_nums = nums[1].split(' ')
        my_nums = set([n for n in my_nums if n.isdigit()])
        cards[key] = [win_nums, my_nums]
    return cards

#---Part One---    

def winning_cards(cards):
    sum = 0
    for card, nums in cards.items():
        n = len(nums[0].intersection(nums[1]))
        if n > 0:
            sum += 2**(n-1)

    return sum

#---Part Two ---
def dup_cards(cards):
    card_plays = {x:1 for x in [*range(1,len(cards)+1)]}
    for key, plays in card_plays.items():
        wins = len(cards[key][0].intersection(cards[key][1]))
        for k in range(1,wins+1):
            card_plays[key+k] += 1*plays
    
    return sum(card_plays.values())


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day04_input.txt')
    print(winning_cards(file))
    print(dup_cards(file))
