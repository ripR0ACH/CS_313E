#  File: Triangle.py
#  Description: A basic 2D Triangle class
#  Student Name: zachary morrison 
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 10/01/2021
#  Date Last Modified: 10/01/2021

import sys
import math

class Point(object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

class Triangle(object): 
    def __init__(self, a = Point(), b = Point(), c = Point()):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return "Point1: " + str(self.a) + ", Point2: " + str(self.b) + ", Point3: " + str(self.c)
    
    def __eq__(self, other):
        sides = sorted([self.a.dist(self.b), self.b.dist(self.c), self.c.dist(self.a)])
        other_sides = sorted([other.a.dist(other.b), other.b.dist(other.c), other.c.dist(other.a)])
        return sides[0] / other_sides[0] == sides[1] / other_sides[1] == sides[2] / other_sides[2]
    
    def is_obtuse(self):
        sides = sorted([self.a.dist(self.b), self.b.dist(self.c), self.c.dist(self.a)])
        return not (sides[0] ** 2 + sides[1] ** 2 >= sides[2] ** 2)
    
    def is_scalene(self):
        sides = sorted([self.a.dist(self.b), self.b.dist(self.c), self.c.dist(self.a)])
        return sides[0] != sides[1] != sides[2]


# takes a string of coordinates and changes it to a list of Points
def get_points(coords_str):
    coords = [float(c) for c in coords_str.split(" ")]
    return [Point(c[0], c[1]) for c in zip(*[iter(coords)]*2)]

def main():
    # read the two triangles
    pointsA = get_points(sys.stdin.readline().strip())
    pointsB = get_points(sys.stdin.readline().strip())
    triangleA = Triangle(pointsA[0], pointsA[1], pointsA[2])
    triangleB = Triangle(pointsB[0], pointsB[1], pointsB[2])
    # Print final output
    print('A', triangleA)
    print('B', triangleB)
    print('A obtuse', triangleA.is_obtuse())
    print('B obtuse', triangleB.is_obtuse())
    print('A scalene', triangleA.is_scalene())
    print('B scalene', triangleB.is_scalene())
    print('A equals b', triangleA == triangleB)

if __name__ == "__main__":
    main()