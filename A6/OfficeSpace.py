#  File: OfficeSpace.py
#  Description: finding the amount of space to be allocated to different people based on their requests
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/23/2021
#  Date Last Modified: 09/24/2021

import sys, unittest

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
  # area of a rectangle is equal to 
  # the length of one side (rect.x2 - rect.x1)
  # times the length of the other side
  # (rect.y2 - rect.y1)
	return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
  # if two rectangles overlap, they will both have at
  # least one of their corners inside the other rectangle
  
  # this checks to see if the lower x-bound
  # of the first rectangle is inside the two 
  # x-bounds of the other rectangle
  rect1_x1_in_rect2 = rect2[0] <= rect1[0] < rect2[2]

  # this checks to see if the upper x-bound of
  # the first rectangle is inside the two 
  # x-bounds of the other rectangle
  rect1_x2_in_rect2 = rect2[0] < rect1[2] <= rect2[2]

  # this checks to see if the lower y-bound
  # of the first rectangle is inside the two 
  # y-bounds of the other rectangle
  rect1_y1_in_rect2 = rect2[1] <= rect1[1] < rect2[3]

  # this checks to see if the upper y-bound of
  # the first rectangle is inside the two 
  # y-bounds of the other rectangle
  rect1_y2_in_rect2 = rect2[1] < rect1[3] <= rect2[3]

  # this long conditional statement checks if all
  # four corners of rect1 are inside rect2
  rect1_in_rect2 = rect1[0] > rect2[0] and rect1[1] > rect2[1] and rect1[2] < rect2[2] and rect1[3] < rect2[3]
  # this long conditional statement checks if all
  # four corners of rect2 are inside rect1
  rect2_in_rect1 = rect2[0] > rect1[0] and rect2[1] > rect1[1] and rect2[2] < rect1[2] and rect2[3] < rect1[3]
  
  # create a tuple with four numbers representing
  # the bottom-left and upper-right points of a 
  # rectangle
  rect = (0, 0, 0, 0)

  # this if-elif block checks if either of the 
  # rectangles are completely inside the other and
  # returns  
  if rect1_in_rect2:
    rect = (rect1[0], rect1[1], rect1[2], rect1[3])
    return rect
  elif rect2_in_rect1:
    rect = (rect2[0], rect2[1], rect2[2], rect2[3])
    return rect
  
  # this if-elif block checks if any two combinations
  # of (rect1.x, rect1.y) is contained inside rect2
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
  
  # returns the corners of rect1 and rect2 that are
  # contained within each other
  # (returns (0, 0, 0, 0) if there are none)
  return rect
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
  # the number of zeroes in the 2D list
  zeroes = 0
  # indexes through each row in the 2D list
  for row in bldg:
    # adds the number of zeroes in the row to the total
    zeroes += row.count(0)
  # returns the number of zeroes in the 2D list
  return zeroes
# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
  # count = number of spaces that are wanted  
  # for more than one office space
  count = 0
  # indexes through the y values
  for y in range(len(bldg)):
    # indexes throught the x values
    for x in range(len(bldg[y])):
      # if the x, y value is greater than one
      # then this means that more than one person
      # requested this office space
      if bldg[y][x] > 1:
        # add one to the count of contested space
        count += 1
  
  # return the area of contested space
  return count
# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
  # ones = the number of spaces within a rectangle
  # that are not being requested for a different 
  # office space
  ones = 0
  # this if statement validates that the rectangle is
  # actually inside the area of the building
  if rect[0] >= 0 and rect[1] >= 0 and rect[2] < len(bldg[0]) and rect[3] < len(bldg):
    # loops through the values in the y-axis
    # of the rect (rect[1] == rect.y1 and
    # rect[3] == rect.y2)
    for y in range(rect[1], rect[3]):
      # loops through the values in the x-axis
      # of the rect (rect[0] == rect.x1 and
      # rect[3] == rect.x2)
      for x in range(rect[0], rect[2]):
        # this if statement checks if the 
        # bldg(x, y) == 0, meaning that it is
        # uncontested
        if bldg[y][x] == 1:
          # adds one to the count of ones
          ones += 1
  # returns the number of ones
  return ones
# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
  # creates a building (bld) with the dimensions specified
  # in office
  bld = [[0 for j in range(office[2])] for i in range(office[3])]
  # checks if there are any people requesting cubes 
  if len(cubicles) > 0:
    # loops through every rectangle requested
    for cube in cubicles:
      # loops through the range of the y-axis in
      # the requested rect (cube)
      for y in range(cube[1], cube[3]):
        # loops throught the range of the x-axis in
        # the requested rect (cube)
        for x in range(cube[0], cube[2]):
          # adds one to every point in bld(x, y)
          # where a person wants their cubical
          bld[y][x] += 1
  # returns the 2D array representing the building
  return bld
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  bld = request_space((0, 0, 33, 26), [(2, 3, 10, 11), (7, 2, 18, 8), (17, 11, 30, 24)])
  assert area((0, 0, 33, 26)) == 858
  assert unallocated_space(bld) == 574
  assert contested_space(bld) == 15
  assert uncontested_space(bld, (2, 3, 10, 11)) == 49
  assert uncontested_space(bld, (7, 2, 18, 8)) == 51
  assert uncontested_space(bld, (17, 11, 30, 24)) == 169
  return "all test cases passed"

def main():
  # run your test cases
  test_cases()
  # read the data
  w, h = sys.stdin.readline().rstrip().split()
  office = (0, 0, int(w), int(h))
  cubicle_count = int(sys.stdin.readline().rstrip())
  names = []
  offices = []
  for i in range(0, cubicle_count):
    line = sys.stdin.readline().rstrip().split()
    names.append(line[0])
    offices.append((int(line[1]), int(line[2]), int(line[3]), int(line[4])))
  bldg = request_space(office, offices)
  # print the following results after computation
  # compute the total office space
  # compute the total unallocated space
  # compute the total contested space
  # compute the uncontested space that each employee gets
  print("Total " + str(area(office)) + "\nUnallocated " + str(unallocated_space(bldg)) + "\nContested " + str(contested_space(bldg)))
  i = 0
  while i < len(names) and i < len(offices) and len(names) == len(offices):
    print(names[i], uncontested_space(bldg, offices[i]))
    i += 1

if __name__ == "__main__":
  main()
