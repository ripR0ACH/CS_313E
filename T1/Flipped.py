#  File: Flipped.py
#  Description: Flip a matrix both horizontally and vertically
#  Student Name: zachary morrison 
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/01/2021
#  Date Last Modified: 10/01/2021

# Input: matrix is a 2d list
# Output: return the equivalent matrix that has been flipped both horizontally and vertically
def flip_matrix(matrix):
    flipped = [[matrix[i][j] for j in range(len(matrix[i]) - 1, -1, -1)] for i in range(len(matrix) - 1, -1, -1)]
    return flipped
def main():
    # read number of rows of matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    
    # get the result from your call to flip_matrix()
    result = flip_matrix(matrix)

    # print the result to standard output
    for i in range(len(result)):
        for j in range(len(result[i])):
            print(result[i][j], end = '')
            if j < len(result[i]) - 1: print(' ', end = '')
        if i < len(result) - 1: print()

if __name__ == "__main__":
    main()