import os
import re
import math

def split_input(filename: str):
    data = [l.strip() for l in open(filename)]

    steps = [char for char in data[0]]
    #Converting left and right steps to indexes
    steps = [0 if x=='L' else 1 for x in steps]
             
    network = {spot.split('=')[0].strip() : re.findall(r'\b\w{3}\b', spot.split('=')[1])   for spot in data[2:]}
    return (steps, network)

def network_steps(map:tuple):
    steps, network = map
    spot = 'AAA'
    count = 0

    while spot != 'ZZZ':
        spot = network[spot][steps[count%len(steps)]]
        count+=1

    return count


def simultaneous_steps(map:tuple):
    steps, network = map
    spots = re.findall(r'\b\w{2}[A]\b', ','.join(network.keys()))
    counts = []

    #For each starting position, find it's shortest path
    for spot in spots:
        count = 0
        while spot[-1] != 'Z':
            spot = network[spot][steps[count%len(steps)]]
            count+=1
        counts.append(count)

    #Using least common multiple to find the step where they would all end in Z
    return math.lcm(*counts)


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day08_input.txt')
    test = split_input('test.txt')
    print(f'Amount of steps to reach ZZZ')
    print(network_steps(file))
    print(f'Amount of steps to for all simulataneous positions to read XXZ is:{simultaneous_steps(file)}')
