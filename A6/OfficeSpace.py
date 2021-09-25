#  File: OfficeSpace.py
#  Description: finding the amount of space to be allocated to different people based on their requests
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/23/2021
#  Date Last Modified: 09/24/2021

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
	return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  # if rect2.x1 <= rect1.x1 < rect2.x2 or rect2.x1 < rect1.x1 <= rect2.x2
  # and rect2.y1 <= rect1.y1 < rect2.y2 or rect2.y1 < rect1.y2 <= rect2.y2
  # (this really long if statement is going to ensure that if a corner on one
  # rectangle is inside the rectangle, 
  rect1_x1_in_rect2 = rect2[0] <= rect1[0] < rect2[2]
  rect1_x2_in_rect2 = rect2[0] < rect1[2] <= rect2[2]
  rect1_y1_in_rect2 = rect2[1] <= rect1[1] < rect2[3]
  rect1_y2_in_rect2 = rect2[1] < rect1[3] <= rect2[3]
  rect = (0, 0, 0, 0)
  if rect1_x1_in_rect2 and rect1_y1_in_rect2:
    rect = (rect1[0], rect1[1], rect2[2], rect2[3])
  elif rect1_x1_in_rect2 and rect1_y2_in_rect2:
    rect = (rect1[0], rect1[3], rect2[2], rect2[1])
  elif rect1_x2_in_rect2 and rect1_y1_in_rect2:
    rect = (rect1[2], rect1[1], rect2[0], rect2[3])
  elif rect1_x2_in_rect2 and rect1_y2_in_rect2:
    rect = (rect1[2], rect1[3], rect2[0], rect2[1])
  if rect[0] > rect[2] or rect[1] > rect[3]:
    rect = (rect[2], rect[3], rect[0], rect[1])
  return rect
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
	pass

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
	pass

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
	pass

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
	pass

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  print(overlap((10, 10, 14, 14), (3,3,12,12)))
  return "all test cases passed"

def main():
  # read the data
  # run your test cases
  # w, h = sys.stdin.readline().rstrip().split()
  w, h = 33, 26
  bld = [[0 for j in range(w)] for i in range(h)]
  print(bld)
  print (test_cases())
  # print the following results after computation
  # compute the total office space
  # compute the total unallocated space
  # compute the total contested space
  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()
