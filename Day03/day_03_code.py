import pathlib
import os
import numpy as np

# Read input
def split_input(filename: str):
    x = np.asarray([[y for y in l.strip()] for  l in open(filename)])
    values = np.ravel(x)

    return x, values

#---Part One---    

def id_number(index: list, corr: np.array):
    id = 140*index[0] + index[1]  
    num = ''
    while True:
        if not corr[id-1].isdigit():
            break
        id -= 1

    while corr[id].isdigit():
        num += corr[id]
        id += 1
    
    return int(num), id//140, id%140

def search_symbol(corr, x, y):
    xs = [x_0 for x_0 in [x-1, x, x+1] if x_0 in [*range(0,corr.shape[0])]]
    ys = [y_0 for y_0 in [y-1, y, y+1] if y_0 in [*range(0,corr.shape[0])]]

    for x in xs:
        for y in ys:
            if not corr[x][y].isdigit() and corr[x][y] != '.':
                return True
    return False

def find_values(corr, corr_1d):
    nums = []
    x = 0
    while x < corr.shape[0]:
        y = 0
        while y < corr.shape[1]:
            if corr[x][y].isdigit():
                if search_symbol(corr, x, y):
                    n, x, y = id_number([x, y], corr_1d)
                    nums.append(n)
                    continue
            y+=1
        x+=1
    return sum(nums)

#---Part Two ---
def search_nums(corr, corr_1d, x, y):
    xs = [x_0 for x_0 in [x-1, x, x+1] if x_0 in [*range(0,corr.shape[0])]]
    ys = [y_0 for y_0 in [y-1, y, y+1] if y_0 in [*range(0,corr.shape[0])]]

    n = set()
    for x in xs:
        for y in ys:
            if corr[x][y].isdigit():
                num, _x, _y = id_number([x,y], corr_1d)
                n.add(num)
    return n

def find_values2(corr, corr_1d):
    nums = []
    x = 0
    while x < corr.shape[0]:
        y = 0
        while y < corr.shape[1]:
            if corr[x][y] == '*':
                k = search_nums(corr, corr_1d, x, y)
                if len(k) == 2:
                    nums.append(np.prod(list(k)))
            y+=1
        x+=1
    return sum(nums)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file, file_1d = split_input('day03_input.txt')
    print(find_values(file, file_1d))
    print(find_values2(file, file_1d))
