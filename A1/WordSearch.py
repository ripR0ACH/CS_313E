import sys
#  File: WordSearch.py

#  Description:

#  Student Name: zachary morrsion

#  Student UT EID: zim225

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 09/03/2021

#  Date Last Modified: 09/04/2021


# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search


def read_input():

  # Input: a 2-D list representing the grid of letters and a single
  #        string representing the word to search
  # Output: returns a tuple (i, j) containing the row number and the
 #         column number of the word that you are searching
  #         or (0, 0) if the word does not exist in the grid


def find_word(grid, word):


def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)


print(word + ": " + str(location))


if __name__ == "__main__":
  main()
