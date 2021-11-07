#  File: StringMerge.py
#  Description: Form all new strings according to the criteria given using recursion.
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
import sys
def permute(s1, s2, l):
    if (s1 + s2) not in l:
        l.append(s1 + s2)
    if len(s1) == 0 or len(s2) == 0:
        return l
    if len(s1) > 1 and len(s2) > 1:
        permute(s1[:-1], s2 + s1[-1], l)
        permute(s1[0], s1[1:] + s2, l)
        permute(s2[:-1], s1 + s2[-1], l)
        permute(s2[0], s2[1:] + s1, l)
    return l

# Input:    2 strings, s1 and s2, which both have length >= 0
# Output:   a list of all possible new strings that can be formed bs2 
#           merging s1 and s2 according to the given criteria
def stringMerge(s1, s2):
    l = permute(s1, s2, [])
    return l 
 
def main():
    # read in 2 input strings
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    
    # find all new strings
    result = stringMerge(s1, s2)
    result.sort()
    print(result)
 
if __name__ == '__main__':
    main()