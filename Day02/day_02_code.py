import pathlib
import os
import re

# Read input
def split_input(filename):
    x = [l.strip().split(':') for  l in open(filename)]
    y = {z[0]:[g.split(',') for g in z[1].split(';')] for z in x}
    games = {}
    for key, item in y.items():
        new_key = int(''.join([d for d in key if d.isdigit()]))
        g = []
        for i in item:
            k = {'red':0, 'blue':0, 'green':0}
            for marble in i:
                for color in ['red', 'green', 'blue']:
                    if color in marble.lower():
                        k[color] = int(''.join([d for d in marble if d.isdigit()]))
            g.append(k)
        games[new_key] = g

    return games

# Part One    
def check1(values):
    n = set()
    marble_max = {'red':12, 'green':13, 'blue':14}
    for game, bags in values.items():
        for marbles in bags:
            for color in marbles.keys():
                if marbles[color] > marble_max[color]:
                    n.add(game)

    return sum(list(range(1,101))) - sum(n)

def check2(values):
    n = []
    for game, bags in values.items():
        powers = {'red':0, 'blue':0, 'green':0}
        for marbles in bags:
            for color in marbles.keys():
                if marbles[color] > powers[color]:
                    powers[color] = marbles[color]
        i = 1
        for g in powers:
            i *= powers[g]
        n.append(i)
    return sum(n)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day02_input.txt')
    print(check1(file))
    print(check2(file))