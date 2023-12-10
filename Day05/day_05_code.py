import os
import numpy as np



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
    destination = [[point[0], point[2]] for point in map[6]]
    lowest = []

    for d in destination:
        orig, d = [d], [d]
        for form in range(len(map)-2,-1, -1):
            n, o = [], []
            for k in range(len(orig)):
                for i in map[form]:

                    diff = i[0] - d[k][0]
                    if diff < 0 and abs(diff) <= i[2]:
                        n.append([i[1]-diff,  min(d[k][1], i[2] + diff)])
                        o.append([orig[k][0], min(d[k][1], i[2] + diff)])

                    if diff >= 0 and diff <= d[k][1]:
                        n.append([i[1], min(d[k][1] - diff, i[2])])
                        o.append([orig[k][0]+diff, min(d[k][1] - diff, i[2])])

            orig = o
            d = n

        for k in range(len(orig)):
            for seed in seeds:
                diff = seed[0] - d[k][0]
                if diff < 0 and abs(diff) <= seed[1]:
                    lowest.append(orig[k][0])
                if diff >= 0 and diff <= d[k][1]:
                    lowest.append(orig[k][0] + diff)
        
    return min(lowest)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day05_input.txt')
    print(mapping_seeds(file))
    print(seed_range(file))