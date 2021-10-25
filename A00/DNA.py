import sys  
#  File: DNA.py
#  Description: this program finds the longest sequence of matching letters in two separate DNA strands.
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 08/30/2021
#  Date Last Modified: 08/30/2021

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
def longest_subsequence(s1, s2):
    sequences = []
    # loop through the full string s1 until it is 1 character or shorter
    while len(s1) > 1:
        # start at character 0
        s = 0
        # end at character 2
        e = 2
        sub = s1[s:e]
        # see if the substring from s1 is found within s2
        while sub in s2:
            if e <= len(s1):
                e += 1
                sub = s1[s:e]
            else:
                break
        # return the longest substring that could be in s2
        e -= 1
        sub = s1[s:e]
        if sub in s1 and sub in s2 and len(sub) != 1 and sub not in sequences:
            # if the substring from s1 is found within both s1 and s2 and is longer than 1 character, it is added to the longest_sequences list
            sequences.append(sub)
        s1 = s1[s+1:]
    
    sequences.sort()
    if len(sequences) == 0:
        return "No Common Sequence Found"
    else:
        # sorts the list for the letter sequence that is max length
        max = sequences[0]
        for longest in range(1, len(sequences)):
            if len(max) < len(sequences[longest]):
                max = sequences[longest]
        list = max
        for longest in range(1, len(sequences)):
            if len(max) == len(sequences[longest]) and max != sequences[longest]:
                list += "\n" + sequences[longest]
        return list

def main():
  # read the data
    n = int(sys.stdin.readline().rstrip())    
  # for each pair
    for pair in range(n):
        print(longest_subsequence(sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()), end="\n\n")
if __name__ == "__main__":
  main()
