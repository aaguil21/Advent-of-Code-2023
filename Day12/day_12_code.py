import os
import re
import functools


def split_input(filename: str, age=2):
    data = [l.strip().split(' ') for l in open(filename)]
    data = [[line[0], [int(x) for x in line[1].split(',')]] for line in data]
    # data = np.array([[char for char in line] for line in data])
    return data


def configurations(data):
    answer = 0
    for x in data:
        a = recursive(x[0], tuple(x[1]))
        answer += a
    return answer


@functools.cache
def recursive(springs, groups):
    if len(springs) > 0 and len(groups) == 0:
        if '#' in springs:
            return 0
        else:
            return 1

    if len(springs) == 0:
        if len(groups) == 0:
            return 1
        else:
            return 0

    if springs[0] == '.':
        return recursive(springs[1:], groups)

    if springs[0] == '?':
        return (recursive('.' + springs[1:], groups) + recursive('#' + springs[1:], groups))

    if springs[0] == '#':
        length = groups[0]
        found_match = True
        if len(springs) < length:
            return 0
        else:
            if '.' in springs[:length]:
                return 0

        if len(springs) > length:
            if springs[length] == '#':
                return 0

        return recursive(springs[length+1:], groups[1:])


def part_two(file):
    answer = 0
    for x in file:
        a = recursive('?'.join([x[0]]*5), tuple(x[1]*5))
        answer += a
    return answer


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day12_input.txt')
    # file = split_input('test.txt')
    print(configurations(file))
    print(part_two(file))
