import sys
from typing import NoReturn
#  File: WordSearch.py
#  Description:
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/03/2021
#  Date Last Modified: 09/04/2021


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input():
  # dimension for n x n matrix of letters
  n = int(sys.stdin.readline().rstrip())
  # skip the blank line after the n value
  sys.stdin.readline()
  # instantiate the word_grid and read the n x n matrix of letters into a 2D list
  word_grid = [sys.stdin.readline().rstrip().split(' ') for x in range(0, n)]
  # skip the blank line after the word_grid
  sys.stdin.readline()

  # read k, the number of words that are going to be searched for in the matrix
  k = int(sys.stdin.readline().rstrip())
  # instantiate the word_list and read in k lines of words into a 1D list
  word_list = [sys.stdin.readline().rstrip() for x in range(0, k)]
  return word_grid, word_list

# Input: 2D list (grid of letters), the word to be searched, the row that the first letter of the word is found in, and the column that the first letter was found in
# Output: this function has no return value, however, it manipulates the stack list by adding the directions taken in the path that writes a word
stack = []

def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter and i != [0, 0]:
            counter = curr_frequency
            num = i

    return num

def check_accuracy(stack, grid, word, i, j):
  # most common direction moved (longest straight line of movement possible)
  copy_word = grid[i][j]
  if len(stack) > 0:
    mcd = most_frequent(stack)
  else:
    mcd = [0, 0]
  moves = []
  for x in range(len(word) - 1):
    moves.append(mcd)
  
  # try to reconstruct the word using longest straight line technique
  for move in moves:
    if move != [0, 0] and move[0] + i < len(grid) and move[0] + i >= 0 and move[1] + j < len(grid[i]) and move[1] + j >= 0 and copy_word == word[:len(copy_word)]:
      copy_word += grid[i + move[0]][j + move[1]]
      i += move[0]
      j += move[1]
    else:
      copy_word = copy_word[:-1]
      i -= move[0]
      j -= move[1]
      break

  if copy_word == word:
    return True
  else: 
    return False


def search_matrix(grid, word, i, j):
  # directions = the 8 possible directions that the tree can branch
  directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
  # if the word is longer than one character, recursively call this function to map the word path and decrease its length
  if len(word) > 1:
    for dir in directions:
      if dir[0] + i < len(grid) and dir[1] + j < len(grid[i]) and dir[1] + j >= 0 and dir[0] + i >= 0 and grid[dir[0] + i][dir[1] + j] == word[1]:
        stack.append(dir)
        search_matrix(grid, word[1:], dir[0] + i, dir[1] + j)

  # when the word reaches one character, append [0, 0] for a stop condition
  elif len(word) == 1 and check_accuracy(stack, grid, word, i, j):
    stack.append([0, 0])




# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching
#         or (0, 0) if the word does not exist in the grid
def find_word(grid, word):
  count = 0
  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):
      if word[0] == grid[i][j]:
        search_matrix(grid, word, i, j)
        if [0, 0] in stack and check_accuracy(stack, grid, word, i, j):
          return (i + 1, j + 1)
        if word == "SOUTH": print(stack)
      stack.clear()
  return (0, 0)

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print(word + ": " + str(location))


if __name__ == "__main__":
  main()
