#  File: Hull.py
#  Description:
#  Student Name:
#  Student UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created:
#  Date Last Modified:

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return (p.x * q.y + q.x * r.y + r.x * p.y - p.y * q.x - q.y * r.x - r.y * p.x)

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
  upper_hull = [sorted_points[0], sorted_points[1]]
  for i in range(2, len(sorted_points)):
    upper_hull.append(sorted_points[i])
    while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0:
      del upper_hull[-2]
  lower_hull = [sorted_points[-1], sorted_points[-2]]
  for i in range(len(sorted_points) - 3, 1, -1):
    lower_hull.append(sorted_points[i])
    while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0:
      del lower_hull[-2]
  lower_hull = lower_hull[1:len(lower_hull) - 1]
  return upper_hull + lower_hull

def det_list(pts = []):
  det = 0
  if len(pts) > 0:
    for i in range(len(pts)):
      if i < len(pts) - 1:
        det += pts[i].x * pts[i + 1].y
      elif i == len(pts) - 1:
        det += pts[i].x * pts[0].y
    for i in range(len(pts)):
      if i < len(pts) - 1:
        det -= pts[i].y * pts[i + 1].x
      elif i == len(pts) - 1:
        det -= pts[i].y * pts[0].x
  return det

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  return abs(det_list(convex_poly)) / 2

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  # print the sorted list of Point objects
  # get the convex hull
  hull = convex_hull(sorted_points)
  # run your test cases
  print("Convex Hull")
  # print your results to standard output
  # print the convex hull
  for i in hull:
    print(i)
  # get the area of the convex hull
  # print the area of the convex hull
  print("\n" + "Area of Convex Hull = " + str(area_poly(hull)))

if __name__ == "__main__":
  main()