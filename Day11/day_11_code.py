import os
import numpy as np

def split_input(filename: str, age=2):
    data = [l.strip() for l in open(filename)]
    data = np.array([[char for char in line] for line in data])
    d_shape = np.shape(data)

    values_x = []
    for x in range(d_shape[0]):
        if np.all(data[x,:] == '.'):
            values_x += [x]
    
    values_y = []
    for x in range(d_shape[1]):
        if np.all(data[:,x] == '.'):
            values_y += [x]
  
    return data, (values_x, values_y)


def star_tracking(map:np.array, expansion:tuple, mulitplier = 2):
    stars = np.argwhere(map == '#')
    num_star = len(stars)
    sum = 0
    for i in range(num_star):
        for k in range(i+1, num_star):
            space = 0
            for y_empty in expansion[1]:     
                if stars[i][1] < stars[k][1]:
                    if y_empty in range(stars[i][1], stars[k][1]):
                        space += mulitplier - 1
                
                else:
                    if y_empty in range(stars[k][1], stars[i][1]):
                        space += mulitplier - 1

            for x_empty in expansion[0]:
                if x_empty in range(stars[i][0], stars[k][0]):
                    space += mulitplier - 1
            sum += abs(stars[i][0] - stars[k][0]) + abs(stars[i][1] - stars[k][1]) + space

    return sum

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file, expansion = split_input('day11_input.txt')
    print(star_tracking(file, expansion))
    print(star_tracking(file, expansion, 1000000))