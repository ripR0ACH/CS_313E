#  File: Radix.py
#  Description: this script sorts a list of strings using a radix sort method
#  Student's Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/29/2021
#  Date Last Modified: 11/01/2021

import sys

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

def main():
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

if __name__ == "__main__":
  main()
