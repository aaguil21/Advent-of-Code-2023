import pathlib
import os
import numpy as np
from functools import reduce
import re

# Read input
def split_input(filename: str):
    file = [l.strip() for l in open(filename)] 
    data = {}
    data['seeds'] = [int(x) for x in file[0].split(':')[1].strip().split(' ')]

    n = []
    i = 0
    print(file[1])
    for line in file[1:]:
        if any(char.isdigit() for char in line):
            #print(line)
            n.append([int(x) for x in line.strip().split(' ')])
        if ':' in line and n:
            data[i] = n
            n = []
            i += 1
    data[i] = n 
    print(data.keys())
    return data

#---Part One---    

def mapping_seeds(map):
    start = map['seeds']
    for i in range(len(map)-1):
        new_transform = []
        for seed in start:
            for form in map[i]:
                if seed >= form[1] and seed <= form[1]+form[2]:
                    new_transform.append(form[0] + seed-form[1])
        start = new_transform

    return min(start)

#---Part Two ---
def seed_range(map):
    seeds = np.reshape(map['seeds'], (len(map['seeds'])//2, 2))
    
    return y


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day05_input.txt')
    print(mapping_seeds(file))
    print(seed_range(file))