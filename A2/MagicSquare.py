#  File: MagicSquare.py
#  Description: this script generates and validates a magic square. The general process is laid out in the comments below
#  Student's Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/09/2021
#  Date Last Modified: 09/10/2021

import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square(n):
    # making an empty square of the n * n dimension
    square = [[0 for j in range(n)] for i in range(n)]
    num = 1
    row = len(square) - 1
    col = int(len(square[row]) / 2)
    while num <= n ** 2:
        square[row][col] = num
        if row == n - 1 and num % n != 0:
            row -= (n - 1)
        elif num % n == 0:
            row -= 1
        else:
            row += 1
        if col == n - 1 and num % n != 0:
            col -= (n - 1)
        elif num % n == 0:
            col = col
        else:
            col += 1
        num += 1
    return square

# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
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

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square(magic_square):
    n = len(magic_square)

    # check the sum of every row in the magic square
    for row in magic_square:
        if sum(row) != n * (n ** 2 + 1) / 2:
            return False
    
    # check the sum of every column in the magic square
    col = 0
    while col < n:
        total = 0
        for row in range(n):
            total += magic_square[row][col]
        if total != n * (n ** 2 + 1) / 2:
            return False
        col += 1
    
    # check the sum of the two main diagonals in the magic square
    row = 0
    col = 0
    total = 0
    while row < n and col < n:
        total += magic_square[row][col]
        row += 1
        col += 1
    if total != n * (n ** 2 + 1) / 2:
        return False
    total = 0
    row = 0
    col = n - 1
    while row < n and col > -1:
        total += magic_square[row][col]
        row += 1
        col -= 1
    if total != n * (n ** 2 + 1) / 2:
        return False

    return True

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers(square, n):
    # directions = the 8 possible directions where numbers that can be added to the sum would be
    directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
    # if the number is greater than the largest number in the magic square, return 0
    if n > len(square) ** 2 or n <= 0:
        return 0

    i = 0
    j = 0
    # i and j become the exact position, square[i][j], where the number, n, is located
    for row in range(len(square)):
        if n in square[row]:
            i = row
            j = square[row].index(n)

    total = 0
    # this loops totals up the numbers surrounding n, as long as they exist
    for dir in directions:
        if dir[0] + i < len(square) and dir[1] + j < len(square[i]) and dir[1] + j >= 0 and dir[0] + i >= 0:
            total += square[i + dir[0]][j + dir[1]]
    return total


def main():
    # read the input file from stdin
    n = int(sys.stdin.readline().rstrip())
    nums_to_check = []
    for line in sys.stdin:
        nums_to_check.append(int(line.rstrip()))
    
    # create the magic square
    sq = make_square(n)

    # print the sum of the adjacent numbers
    if check_square(sq):
        for num in nums_to_check:
            print(sum_adjacent_numbers(sq, num))
# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
