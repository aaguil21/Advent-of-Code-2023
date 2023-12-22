import os


def split_input(filename: str):
    data = [l.strip().split(' ') for l in open(filename)]
    for i, line in enumerate(data):
         data[i] = [int(x) for x in line]

    return data

def next_point(history):
    total_points = 0
    for line in history:
        sequence = [line]
        current = line.copy()
        while any([x!=0 for x in current]):
            next = []
            for i in range(len(current)-1):
                next.append(current[i+1] - current[i])
            current = next
            sequence.append(next)
        #print(sequence)

        for k in range(len(sequence)-1, 0,-1):
            sequence[k-1].append(sequence[k-1][-1] + sequence[k][-1])
        

        total_points += sequence[0][-1]

    return total_points


def previous_point(history):
    total_points = 0
    for line in history: 
        sequence = [line]
        current = line.copy()
        while any([x!=0 for x in current]):
            last = []
            for i in range(len(current)-1):
                last.append(current[i+1] - current[i])
            current = last
            sequence.append(last)
       

        for k in range(len(sequence)-1, 0,-1):
            sequence[k-1].insert(0, sequence[k-1][0] - sequence[k][0])

        total_points += sequence[0][0]

    print(sequence)
    return total_points


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day09_input.txt')
    #file= split_input('test.txt')
    print(next_point(file))
    print(previous_point(file))
