#  File: Interpreter.py
#  Description: Interprets 'code' and evaluates expressions
#  Student Name: zachary morrison 
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/01/2021
#  Date Last Modified: 10/01/2021

import sys

def main():
    line = sys.stdin.readline().strip().split(' ')
    memory = {}

    while line[0] != 'exit':
        line = sys.stdin.readline().strip().split(' ')

if __name__ == '__main__':
    main()