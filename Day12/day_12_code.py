import os
import regex as re

def split_input(filename: str, age=2):
    data = [l.strip().split(' ') for l in open(filename)]
    data = [[line[0], [int(x) for x in line[1].split(',')]] for line in data]
    #data = np.array([[char for char in line] for line in data])
    return data

def configurations(data):
    string = ''
    for i, point in enumerate(data[1]):
        string = '[\.\?][\#\?]{' + f'{point}' + '}[\.\?]?'
        l = re.findall(string, data[0], overlapped=True)
        #elif i == len(data[1])-1:
         #   string += '[\#\?]{' + f'{point}' + '}'
        #else:
        #    string += '[\#\?]{' + f'{point}' + '}[\.\?]{1,10}?'

    print(string)
 
    return l


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file= split_input('day12_input.txt')
    print(file[0])
    print(configurations(file[0]))
    print(8/3)