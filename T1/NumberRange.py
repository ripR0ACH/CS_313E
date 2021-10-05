#  File: NumberRange.py
#  Description: Combine the close ranges of numbers to save space
#  Student Name: zachary morrison 
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/01/2021
#  Date Last Modified: 10/01/2021

import sys

# Input:    An list of unique postive integers
# Output:   An sorted list of string of the combined ranges
def combine_into_ranges(number_list):
    combined_list = []
    nums = sorted(set(number_list))
    gaps_in_nums = [[start, end] for start, end in zip(nums, nums[1:]) if start + 1 < end]
    edges_of_ranges = iter(nums[:1] + sum(gaps_in_nums, []) + nums[-1:])
    ranges = list(zip(edges_of_ranges, edges_of_ranges))

    
    # this list contains the indexes of the ranges that aren't
    # valid for this problem
    not_fit = []
    for i in range(len(ranges)):
        if ranges[i][1] - ranges[i][0] < 2:
            not_fit.append(i)
    for i in range(len(not_fit) - 1, -1, -1):
        del ranges[not_fit[i]]
    if len(ranges) == 0:
        for num in nums:
            combined_list.append(str(num))
        return combined_list
    for ran in ranges:
        for ind in range(len(nums) - 1, -1, -1):
            if ran[0] <= nums[ind] <= ran[1]:
                del nums[ind]
    for ran in ranges:
        for num in nums:
            if num < ran[0] and str(num) not in combined_list:
                combined_list.append(str(num))
        combined_list.append(str(ran[0]) + "-" + str(ran[1]))
    for num in nums:
        if len(ranges) > 0 and num > ranges[-1][1]:
            combined_list.append(str(num))
    return combined_list


            
# NO NEED TO CHANGE main()
def main():
    # Read the list of numbers
    number_list = [*map(int, sys.stdin.readline().split())]
    # print the answer
    ans = combine_into_ranges(number_list)
    # TODO print
    for i in range(len(ans)):
        if i == len(ans) - 1:
            print(ans[i], end = '')
        else:
            print(ans[i], end = ' ')


if __name__ == "__main__":
    main()