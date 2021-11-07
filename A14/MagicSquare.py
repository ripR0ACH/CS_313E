#  File: MagicSquare.py
#  Description: this script generates and validates a magic square. The general process is laid out in the comments below
#  Student's Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/24/2021
#  Date Last Modified: 10/27/2021

import math

def print_square(magic_square):
    n = len(magic_square)
    for i in magic_square:
        for j in i:
            # printing the square with up to two spaces between each number in a row
            if n ** 2 < 10:
                print('{:1}'.format(j), end=' ')
            elif n ** 2 < 100:
                print('{:2}'.format(j), end='  ')
            else:
                print('{:3}'.format(j), end='  ')
        # adding a line break after each row 
        print()

class Queue(object):
    def __init__(self, q = []):
        self.queue = q
    def enq(self, item):
        self.queue = [item] + self.queue[:]
    def deq(self):
        temp = self.queue[-1]
        self.queue = self.queue[:-1]
        return temp
    def __str__(self):
        s = '['
        for i in self.queue:
            s += str(i) + ', '
        s = s[:-2] + ']'
        return s

def groupSum(q, target, row):
    # make sure that the start is within the bounds of nums
    if sum(row) == target and len(row) == int(math.sqrt(len(q.queue))):
        return row
    elif len(row) < int(math.sqrt(len(q.queue))):
        row.append(q.deq())

def make_square(n):
    # making an empty square of the n * n dimension
    q = Queue([i + 1 for i in range(n ** 2)])
    


def main():
    # make_square(4)
    pass

if __name__ == "__main__":
  main()