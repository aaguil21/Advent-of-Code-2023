import os
from math import sqrt, floor, ceil

def split_input(filename: str):
    file = [l.strip() for l in open(filename)] 
    data = {}
    data['Time'] = [int(x) for x in file[0].split(':')[1].strip().split(' ') if x.isdigit()]
    data['Distance'] = [int(x) for x in file[1].split(':')[1].strip().split(' ') if x.isdigit()]

    return data

def record_beat(data):
    beats = 1
    for i, x in enumerate(data['Time']):
        b_plus = floor((x + sqrt(x**2 - 4*data['Distance'][i]))/2)
        b_minus = ceil((x - sqrt(x**2 - 4*data['Distance'][i]))/2)
        beats *= (b_plus - b_minus + 1)
    
    return beats

def single_race(data):
    time = int(''.join([str(x) for x in data['Time']]))
    dist = int(''.join([str(x) for x in data['Distance']]))

    b_plus = floor((time + sqrt(time**2 - 4*dist))/2)
    b_minus = ceil((time - sqrt(time**2 - 4*dist))/2)

    return b_plus - b_minus + 1


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day06_input.txt')
    print(record_beat(file))
    print(single_race(file))