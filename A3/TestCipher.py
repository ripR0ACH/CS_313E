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
  # the key must be greater than 2 but less than the length of the strng provided
  if key >= 2 and key <= len(strng):
    # make a grid with the dimensions of 
    # key x the length of strng
    grid = [["-" for j in range(len(strng))] for i in range(key)]
    # make a counter that will track the letter in the word
    # that is being indexed
    letter_count = 0
    # make a row variable to easily traverse the rows 
    # (since the program needs to zig-zag between rows)
    row = 0
    # add the first character of the strng to the point (0, 0) in the grid
    grid[row][letter_count] = strng[letter_count]
    dir = 1 # this will start the row at zero and go down each time
    # while the letter being indexed is 
    # less than the last index in the strng
    while letter_count < len(strng) - 1:
        letter_count += 1
        row += dir
        # moves in the diagonal direction then adds a letter to the spot
        grid[row][letter_count] = strng[letter_count]
        if row == len(grid) - 1:
          # if the row reaches the bottom of the grid,
          # change direction of row traversal
          dir = -1
        elif row == 0:
          # same as above, but if row reaches top
          dir = 1
  # variable that will contain encoded string
  encoded = ""
  for row in grid:
    # compound the characters in the row
    # and add them to the encoded string
    encoded += "".join([s.replace("-", "") for s in row])
  return encoded

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
  # these two arrays will contain 
  letter_row = []
  letter_placements = []
  if key >= 2 and key <= len(strng):
    grid = [["-" for j in range(len(strng))] for i in range(key)]
    letter_count = 0
    row = 0
    letter_row.append(row)
    letter_placements.append((row, letter_count))
    dir = 1  # this will start the row at zero and go down each time
    while letter_count < len(strng) - 1:
        letter_count += 1
        row += dir
        letter_row.append(row)
        letter_placements.append((row, letter_count))
        if row == len(grid) - 1:
          dir = -1
        elif row == 0:
          dir = 1
    letter_count = 0
    letter_row.sort()
    copy = letter_placements.copy()
    for num in range(len(letter_row)):
      for point in range(len(copy)):
        if copy[point][0] == letter_row[num]:
          grid[copy[point][0]][copy[point][1]] = strng[letter_count]
          letter_count += 1
          del copy[point]
          break
    decoded = ""
    for point in letter_placements:
      decoded += grid[point[0]][point[1]]
    return decoded # placeholder for the actual return statement

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
  strng = strng.lower()
  whitelist = set('abcdefghijklmnopqrstuvwxyz')
  return "".join(filter(whitelist.__contains__, strng))# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
  ALPHA = 'abcdefghijklmnopqrstuvwxyz'
  # create the row of letters being used to encrypt the character
  cipher = ALPHA[ALPHA.index(s):] + ALPHA[:ALPHA.index(s)]
  # return the character from cipher with the index of the index of the pass phrase letter in the alphabet 
  return cipher[ALPHA.index(p)] 

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
  ALPHA = 'abcdefghijklmnopqrstuvwxyz'
  # create the row of letters being used to decrypt the character
  cipher = ALPHA[ALPHA.index(p):] + ALPHA[:ALPHA.index(p)]
  # return the character from alphabet with the index of the index of the plain text letter in the cipher  
  return ALPHA[cipher.index(s)]

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
  # filters the string using the function made above
  strng = filter_string(strng)
  # makes the pass phrase the same length as the string
  phrase = phrase * int(len(strng) / len(phrase)) + phrase[:len(strng) % len(phrase)]
  encoded = ""
  # encodes the string one letter at a time
  for n in range(len(strng)):
    encoded += encode_character(phrase[n], strng[n])
  # returns the encoded string
  return encoded

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
  # filters the string using the function made above
  strng = filter_string(strng)
  # makes the pass phrase the same length as the string 
  phrase = phrase * int(len(strng) / len(phrase)) + phrase[:len(strng) % len(phrase)]
  decoded = ""
  # decodes the string one letter at a time
  for n in range(len(strng)):
    decoded += decode_character(phrase[n], strng[n])
  # returns the decoded string
  return decoded


def main():
  f = []
  # read the plain text from stdin
  for line in sys.stdin: 
    f.append(line.rstrip())
  for i in range(4):
    # read the plain text or encrypted text from stdin
    text = f[2 * i]
    # read the key or pass from stdin
    key = f[2 * i + 1]
    if i == 0:
      print("Rail Fence Cipher\n")
    if i == 2:
      print("Vigenere Cipher\n")
    if i == 0 or i == 2:
      print("Plain Text:", text)
      if i == 0:
        print("Key:", key)
        # encrypt and print the encoded text using rail fence cipher
        print("Encoded Text:", rail_fence_encode(text, int(key)))
        print()
      elif i == 2:
        print("Pass Phrase:", key)
        # encrypt and print the encoded text using Vigenere cipher
        print("Encoded Text:", vigenere_encode(text, key))
        print()
    else:
      print("Encoded Text:", text)
      if i == 1:
        print("Enter Key:", key)
        # decrypt and print the plain text using rail fence cipher
        print("Decoded Text:", rail_fence_decode(text, int(key)))
        print()
      elif i == 3:
        print("Pass Phrase:", key)
        # decrypt and print the plain text using Vigenere cipher
        print("Decoded Text:", vigenere_decode(text, key))
        print()
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
