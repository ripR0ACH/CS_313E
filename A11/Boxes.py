#  File: Boxes.py
#  Description: finding all possibilities of boxes fitting within each other
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created:
#  Date Last Modified:

import sys

box_nests = []

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes(box_list):
    for idx in range(len(box_list), 0, -1):
        

# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
# read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = list(map(int, line.split()))
        box.sort()
        box_list.append(box)
    # sort the box list
    box_list.sort()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print(max_boxes)

    # print the number of sets of such boxes
    print(num_sets)


if __name__ == "__main__":
    main()
