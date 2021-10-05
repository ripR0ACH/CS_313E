#  File: FuzzyAnagram.py
#  Description: Determine if two words are k-fuzzy anagrams of each other
#  Student Name: zachary morrison 
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/01/2021
#  Date Last Modified: 10/01/2021

import sys

# Input:    word1, word2 are 2 strings of the two words to check
#           k is the number of "off" characters allowed
# Output:   True if word1 and word2 are k-fuzzy anagrams of each other,
#           False otherwise
def is_fuzzy_anagram(word1, word2, k):
    letter = 0
    if len(word2) - len(word1) > k:
        return False
    while letter < len(word2):
        if word2[letter] in word1:
            word1 = word1.replace(word2[letter], '', 1)
        letter += 1
    return len(word1) <= k

def main():
    # read the number of test cases
    cases = int(sys.stdin.readline())

    # loop through cases
    for case in range(cases):
        line = sys.stdin.readline().split()
        k, word1, word2 = int(line[0]), line[1], line[2]
        if (is_fuzzy_anagram(word1, word2, k)):
            print(word2 + ' is a/an ' + str(k) + ' fuzzy anagram of ' + word1)
        else:
            print(word2 + ' is not a/an ' + str(k) + ' fuzzy anagram of ' + word1)

if __name__ == "__main__":
    main()