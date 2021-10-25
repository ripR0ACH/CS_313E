#  File: recursion2.py 
#  Description: practicing different recursion methods and their applications
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/03/2021
#  Date Last Modified: 10/04/2021


# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target? 
# This is a classic backtracking recursion problem. Once you 
# understand the recursive backtracking strategy in this problem, 
# you can use the same pattern for many problems to search a space 
# of choices. Rather than looking at the whole array, our convention 
# is to consider the part of the array starting at index start and 
# continuing to the end of the array. The caller can specify the 
# whole array simply by passing start as 0. No loops are needed -- 
# the recursive calls progress down the array. 
def groupSum(start, nums, target):
    # make sure that the start is within the bounds of nums
    if start >= len(nums):
        return target == 0
    # recursively decrease the value of sum to using the nums[start] value
    if groupSum(start + 1, nums, target - nums[start]):
        return True
    # pass over the current value of nums[start] to try the other trees
    if groupSum(start + 1, nums, target):
        return True
    # return false if the sum does not add up to the target
    return False
        
    


  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, beginning at the start index, such that the group 
# sums to the given target? However, with the additional constraint 
# that all 6's must be chosen. (No loops needed.)
def groupSum6(start, nums, target):
    # make sure that the start is within the bounds of nums
    if start >= len(nums):
        return target == 0
    # see if nums[start] equals 6, and decrement the value to decrease target
    if nums[start] == 6:
        return groupSum6(start + 1, nums, target - nums[start])
    # otherwise try the normal 
    if groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target):
        return True
    return False


  
# Given an array of ints, is it possible to choose a group of some 
# of the ints, such that the group sums to the given target with this 
# additional constraint: If a value in the array is chosen to be in 
# the group, the value immediately following it in the array must 
# not be chosen. (No loops needed.) 
def groupNoAdj(start, nums, target):
    # make sure that the start is within the bounds of nums
    if start >= len(nums):
        return target == 0
    # runs the normal sum algorithm, but in the first variation it adds 2 to the index to skip over
    # the directly adjacent number
    if groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target):
        return True
    return False


# Given an array of ints, is it possible to choose a group 
# of some of the ints, such that the group sums to the given 
# target with these additional constraints: all multiples of 
# 5 in the array must be included in the group. If the value 
# immediately following a multiple of 5 is 1, it must not 
# be chosen. (No loops needed.)
def groupSum5(start, nums, target):
    # make sure that the start is within the bounds of nums
    if start >= len(nums):
        return target == 0
    # checks if the number that it's currently on is divisible by 5 and that the next value isn't outside the range
    # of the nums list
    if nums[start] % 5 == 0 and start + 1 < len(nums):
        # makes sure that the adjacent number beside the multiple of 5
        # isn't a one
        if nums[start + 1] != 1:
            return groupSum5(start + 1, nums, target - nums[start])
        # if it is a one, it skips it and uses the next number
        else:
            return groupSum5(start + 2, nums, target - nums[start])
    # this if statement runs the regular sum algorithm that was used in the previous sum problems
    if groupSum5(start + 1, nums, target - nums[start]) or groupSum5(start + 1, nums, target):
        return True
    # if none of the conditions above passed, return False
    return False
  
# Given an array of ints, is it possible to choose a 
# group of some of the ints, such that the group sums 
# to the given target, with this additional constraint: 
# if there are numbers in the array that are adjacent 
# and the identical value, they must either all be chosen, 
# or none of them chosen. For example, with the array 
# [1, 2, 2, 2, 5, 2], either all three 2's in the middle 
# must be chosen or not, all as a group. (one loop can 
# be used to find the extent of the identical values). 
def groupSumClump(start, nums, target):
    # make sure that the start is within the bounds of nums
    if start >= len(nums):
        return target == 0
    # check that the number after the start is within the bounds of the function
    # and that the next number is the same as the first
    if start + 1 < len(nums) and nums[start] == nums[start + 1]:
        # save the number that needs to be repeated to a variable
        repeated = nums[start]
        # this variable is to contain the sum of the repeated number
        sum_repeat = 0
        # this loop will continue until it reaches the end of the list
        # nums or until the number that it's on doesn't match the number that should be repeated
        while start < len(nums) and nums[start] == repeated:
            sum_repeat += nums[start]
            start += 1
        # it then starts two new brances of recursion: one that subtracts the sum of the repeated number
        # from the target and tries to see if it can find a True path; one that continues trying to find
        # the sum but skips the repeating numbers
        return groupSumClump(start, nums, target - sum_repeat) or groupSumClump(start, nums, target)
    # it also tries the original sum algorithm at the end to add any numbers
    # that don't fit into the conditions outlined above
    if groupSumClump(start + 1, nums, target - nums[start]) or groupSumClump(start + 1, nums, target):
        return True
    # if none of the above blocks evaluates to True, return False
    return False
        

# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sums of the two 
# groups are the same. Every int must be in one group 
# or the other. Write a recursive helper method that 
# takes whatever arguments you like, and make the 
# initial call to your recursive helper from splitArray(). 
# (No loops needed.)
def splitArray(nums):
    # can the summation of the list of nums be evenly divided into two
    if sum(nums) % 2 != 0:
        # if not, return False without running recursive algorithm
        return False
    # otherwise return the helper function
    return splitArrayHelper(nums, len(nums), 0, 0, 0)
# Input: the helper function takes in the array of nums, the length
#        of the array, the starting point of the recursion, the first sum
#        being calculated, and the second sum being calculated
# Output: outputs whether or not the array can be evenly divided into
#         two arrays that have an equal sum of their items
def splitArrayHelper(nums, length, start, sum1, sum2):
    # checks if the starting value is at the end of the array of nums
    if start == length:
        # if it is at the end of nums, it returns True if the sums are the same,
        # otherwise it returns False
        return sum1 == sum2
    # the recursion pursues two separate branches:
    # - the first branch adds one to the starting value
    #   and adds the value nums[start] (the current value
    #   of the nums array) to sum1
    # - the second branch adds one to the starting value
    #   and adds the value nums[start] to sum2
    # this recursion method will check all the different variations
    # of summing the numbers to find if there is a variation where
    # the sums, sum1 and sum2, can be equal
    return splitArrayHelper(nums, length, start + 1, sum1 + nums[start], sum2) or splitArrayHelper(nums, length, start + 1, sum1, sum2 + nums[start])

# Given an array of ints, is it possible to divide the 
# ints into two groups, so that the sum of one group
# is a multiple of 10, and the sum of the other group 
# is odd. Every int must be in one group or the other. 
# Write a recursive helper method that takes whatever 
# arguments you like, and make the initial call to your 
# recursive helper from splitOdd10(). (No loops needed.)
def splitOdd10(nums):
    # checks if the sum of the nums % 10 is even
    # meaning that it reduces the sum of the nums to 
    # be only the value in the ones-place
    if (sum(nums) % 10) % 2 == 0:
        # it returns false if the number is False
        # because it directly contradicts the purpose
        # of the function
        return False
    # oddly enough, I found that this problem can be solved without even using
    # the recursion. It output the exact same results when I just put "return False"
    # on the line below instead of the recursive algorithm
    return splitOdd10Helper(nums, len(nums), 0, 0, 0)
def splitOdd10Helper(nums, length, start, sum1, sum2):
    # checks if the starting value is at the end of the array of nums
    if start == length:
        # if it is at the end of nums, it returns True 
        # if the first sum / 10 has no remainder and the
        # second sum is odd.
        # otherwise it returns False
        return sum1 % 10 == 0 and sum2 % 2 != 0
    # the recursion is the same as in the problem before
    return splitOdd10Helper(nums, length, start + 1, sum1 + nums[start], sum2) or splitOdd10Helper(nums, length, start + 1, sum1, sum2  + nums[start])


  
# Given an array of ints, is it possible to divide the ints 
# into two groups, so that the sum of the two groups is the 
# same, with these constraints: all the values that are 
# multiple of 5 must be in one group, and all the values 
# that are a multiple of 3 (and not a multiple of 5) 
# must be in the other. (No loops needed.) 
def split53(nums):
    # this function just returns the value of the helper function
    return split53Helper(nums, len(nums), 0, 0, 0)
def split53Helper(nums, length, start, sum1, sum2):
    # checks if the starting value is at the end of the array of nums
    if start == length:
        # if it is at the end of nums, it returns True if the sums are the same,
        # otherwise it returns False
        return sum1 == sum2
    # checks if the current number is divisible by 5
    if nums[start] % 5 == 0:
        # if it is, it adds the value to sum1
        sum1 += nums[start]
    # else, it checks if the current number is divisible by 3
    elif nums[start] % 3 == 0:
        # if it is, it adds the value to sum2
        sum2 += nums[start]
    else:
        # otherwise, it runs the same recusion as the problems above
        return split53Helper(nums, length, start + 1, sum1 + nums[start], sum2) or split53Helper(nums, length, start + 1, sum1, sum2 + nums[start])
    # and if all the conditional blocks above fail,
    # it moves forward one number in the array and tries again
    return split53Helper(nums, length, start + 1, sum1, sum2)


#######################################################################################################
#######################################################################################################
#                                                                                                     #
#                   DO NOT MODIFY ANYTHING BELOW THIS LINE !!                                         #
#                                                                                                     #
#######################################################################################################
#######################################################################################################
def main(argv):
    problems = ["groupSum", "groupSum6", "groupNoAdj", "groupSum5", "groupSumClump", "splitArray", "splitOdd10", "split53"]
    if len(argv) == 0:
        printHelp()
        exit(1)
    elif "all" in argv:
        argv = problems
    for problem in argv:
        if not problem in problems:
            printHelp()
            exit(1)
    
    groupSum_args = [(0, [2, 4, 8], 10), (0, [2, 4, 8], 14), (0, [2, 4, 8], 9), (0, [2, 4, 8], 8), (1, [2, 4, 8], 8), (1, [2, 4, 8], 2), (0, [1], 1), (0, [9], 1), (1, [9], 0), (0, [], 0), (0, [10, 2, 2, 5], 17), (0, [10, 2, 2, 5], 15), (0, [10, 2, 2, 5], 9)]
    groupSum6_args = [(0, [5, 6, 2], 8), (0, [5, 6, 2], 9), (0, [5, 6, 2], 7), (0, [1], 1), (0, [9], 1), (0, [], 0), (0, [3, 2, 4, 6], 8), (0, [6, 2, 4, 3], 8), (0, [5, 2, 4, 6], 9), (0, [6, 2, 4, 5], 9), (0, [3, 2, 4, 6], 3), (0, [1, 6, 2, 6, 4], 12), (0, [1, 6, 2, 6, 4], 13), (0, [1, 6, 2, 6, 4], 4), (0, [1, 6, 2, 6, 4], 9), (0, [1, 6, 2, 6, 5], 14), (0, [1, 6, 2, 6, 5], 15), (0, [1, 6, 2, 6, 5], 16)]
    groupNoAdj_args = [(0, [2, 5, 10, 4], 12), (0, [2, 5, 10, 4], 14), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4, 2], 7), (0, [2, 5, 10, 4], 9), (0, [10, 2, 2, 3, 3], 15), (0, [10, 2, 2, 3, 3], 7), (0, [], 0), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [5, 10, 4, 1], 11)]
    groupSum5_args = [(0, [2, 5, 10, 4], 19), (0, [2, 5, 10, 4], 17), (0, [2, 5, 10, 4], 12), (0, [2, 5, 4, 10], 12), (0, [3, 5, 1], 4), (0, [3, 5, 1], 5), (0, [1, 3, 5], 5), (0, [3, 5, 1], 9), (0, [2, 5, 10, 4], 7), (0, [2, 5, 10, 4], 15), (0, [2, 5, 10, 4], 11), (0, [1], 1), (0, [9], 1), (0, [9], 0), (0, [], 0)]
    groupSumClump_args = [(0, [2, 4, 8], 10), (0, [1, 2, 4, 8, 1], 14), (0, [2, 4, 4, 8], 14), (0, [8, 2, 2, 1], 9), (0, [8, 2, 2, 1], 11), (0, [1], 1), (0, [9], 1)]
    splitArray_args = [([2, 2]), ([2, 3]), ([5, 2, 3]), ([5, 2, 2]), ([1, 1, 1, 1, 1, 1]), ([1, 1, 1, 1, 1]), ([]), ([1]), ([3, 5]), ([5, 3, 2]), ([2,2,10,10,1,1]), ([1,2,2,10,10,1,1]), ([1,2,3,10,10,1,1])]
    splitOdd10_args = [[5, 5, 5], [5, 5, 6], [5, 5, 6, 1], [6, 5, 5, 1], [6, 5, 5, 1, 10], [6, 5, 5, 5, 1], [1], [], [10, 7, 5, 5], [10, 0, 5, 5], [10, 7, 5, 5, 2], [10, 7, 5, 5, 1]]
    split53_args = [[1,1], [1, 1, 1], [2, 4, 2], [2, 2, 2, 1], [3, 3, 5, 1], [3, 5, 8], [2, 4, 6], [3, 5, 6, 10, 3, 3]]
	
	
    groupSum_ans = [True, True, False, True, True, False, True, False, True, True, True, True, True]
    groupSum6_ans = [True, False, False, True, False, True, True, True, False, False, False, True, True, False, False, True, True, False]
    groupNoAdj_ans = [True, False, False, True, True, True, False, True, True, False, True, True]
    groupSum5_ans = [True, True, False, False, False, True, True, False, False, True, False, True, False, True, True]
    groupSumClump_ans = [True, True, False, True, False, True, False]
    splitArray_ans = [True, False, True, False, True, False, True, False, False, True, True, False, True]
    splitOdd10_ans = [True, False, True, True, True, False, True, False, True, False, True, False]
    split53_ans = [True, False, True, False, True, False, True, True]

    for prob in argv:
      correct = 0  # counts number of test cases passed
      leftParen = "("
      rightParen = ")"
      # loop over test cases
      for i in range(len(locals()[prob+"_args"])):
        if type(locals()[prob+"_args"][i]) is tuple:
          leftParen = rightParen = ""
        if (type(locals()[prob+"_args"][i]) is str) or (type(locals()[prob+"_args"][i]) is int) or (type(locals()[prob+"_args"][i]) is list) or (len(locals()[prob+"_args"][i]) == 1): # function takes one argument
          if globals()[prob](locals()[prob+"_args"][i]) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](locals()[prob+"_args"][i])), " expected:", str(locals()[prob+"_ans"][i]))
        elif len(locals()[prob+"_args"][i]) == 2: # there are two arguments to function
          first, second = locals()[prob+"_args"][i]
          if globals()[prob](first, second) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWorng!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second)), " expected:", str(locals()[prob+"_ans"][i]))
        else:    
          first, second, third = locals()[prob+"_args"][i]
          if globals()[prob](first, second, third) == locals()[prob+"_ans"][i]:
              print ("\nCorrect!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
              correct += 1
          else: # print fail message
              print ("\nWrong!", prob + leftParen + str(locals()[prob+"_args"][i]) + rightParen + " result:", str(globals()[prob](first, second, third)), " expected:", str(locals()[prob+"_ans"][i]))
      print ("\n" + prob + ": passed", correct, "out of", len(locals()[prob+"_ans"]), "\n")

def printHelp():
    print ("\nInvoke this script with the name of the function you wish to test.")
    print ("e.g. python recursion1.py factorial")
    print ("Invoke with \"python recursion1.py all\" to run all of the function tests\n")
      
import sys
main(sys.argv[1:])
