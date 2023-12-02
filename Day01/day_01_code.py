import pathlib
import os

# Read input
def split_input(filename):
    return [l.strip() for  l in open(filename)]

# Part One    
def check1(values):
    """
    
    """
    nums = []
    for x in values:
        x = [y for y in x if y.isdigit()]
        nums.append(int(x[0]+x[-1]))
    return sum(nums)


# Part Two
def check2(val):
    text_to_digit = {'one':'o1e', 'two':'t2', 'three':'t3e', 'four':'4', 
                     'five':'5e', 'six':'6', 'seven':'7n', 'eight':'8', 'nine':'9'}
    for i, x in enumerate(val): 
        for key, digit in text_to_digit.items():
           x =  x.lower().replace(key, digit)
        val[i] = x

    return check1(val)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    file = split_input('day01_input.txt')
    print(check1(file)) 
    print(check2(file))