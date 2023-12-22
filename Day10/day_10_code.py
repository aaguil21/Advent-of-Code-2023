import os
import numpy as np

def split_input(filename: str):
    data = [l.strip() for l in open(filename)]
    data = np.array([[char for char in line] for line in data])
    return data


def routing(map):
    itemindex = np.argwhere(map == 'S')
    return itemindex

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day10_input.txt')
    print(routing(file))