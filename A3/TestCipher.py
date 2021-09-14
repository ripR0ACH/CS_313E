#  File: TestCipher.py
#  Description: this script encodes and decodes different ciphers using rail fence and vigenere cipher
#  Student's Name: zachary morrison
#  Student's UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/13/2021
#  Date Last Modified: 09/13/2021

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    if key >= 2 and key <= len(strng):
        grid = [["-" for j in range(len(strng))] for i in range(key)]
        letter_count = 0
        row = 0
        grid[row][letter_count] = strng[letter_count]
        dir = 1 # this will start the row at zero and go down each time
        while letter_count < len(strng) - 1:
            letter_count += 1
            row += dir
            grid[row][letter_count] = strng[letter_count]
            if row == len(grid) - 1:
                dir = -1
            elif row == 0:
                dir = 1
    encoded = ""
    for row in grid:
        encoded += "".join([s.replace("-", "") for s in row])
    return encoded  # placeholder for the actual return statement

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    if key >= 2 and key <= len(strng):
      grid = [["-" for j in range(len(strng))] for i in range(key)]
      
        
    return ""  # placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
  return ""  # placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
  return ""  # placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
  return ""  # placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
  return ""  # placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
  return ""  # placeholder for the actual return statement


def main():
    li = rail_fence_encode("helloworld", 3)
    print(li)
  # read the plain text from stdin

  # read the key from stdin

  # encrypt and print the encoded text using rail fence cipher

  # read encoded text from stdin

  # read the key from stdin

  # decrypt and print the plain text using rail fence cipher

  # read the plain text from stdin

  # read the pass phrase from stdin

  # encrypt and print the encoded text using Vigenere cipher

  # read the encoded text from stdin

  # read the pass phrase from stdin

  # decrypt and print the plain text using Vigenere cipher


  # The line above main is for grading purposes only.
  # DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
