#  File: Geometry.py
#  Description: creating geometric objects and functions that easily manipulate and compare them
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/17/2021
#  Date Last Modified: 09/18/2021

import math
import sys

class Point (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)
    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __ne__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return False
        return True

    def dot(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
class Sphere (object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0, radius=1):
        self.p = Point(x, y, z)
        self.r = radius
    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return "Center: " + str(self.p) + ", Radius: " + str(self.r)
    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * self.r ** 2
    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return 4 / 3 * math.pi * self.r ** 3
    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        if p.distance(self.p) < self.r:
            return True
        return False
    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        if self.p.distance(other.p) < self.r - other.r:
            return True
        return False
    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        for corner in a_cube.corners:
           if corner.distance(self.p) >= self.r:
               return False
        return True
    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        return False
    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        if self.p.distance(other.p) < self.r + other.r:
            return True
        return False
    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        return False
    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        return Cube()

class Cube (object):
    
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0, y=0, z=0, side=1):
        self.p = Point(x, y, z)
        self.side = side
        bottom_left_back_corner = Point(self.p.x - (self.side / 2), self.p.y - (self.side / 2), self.p.z - (self.side / 2))
        self.corners = [
            bottom_left_back_corner,
            Point(bottom_left_back_corner.x + self.side, bottom_left_back_corner.y, bottom_left_back_corner.z),
            Point(bottom_left_back_corner.x + self.side, bottom_left_back_corner.y + self.side, bottom_left_back_corner.z),
            Point(bottom_left_back_corner.x, bottom_left_back_corner.y + self.side, bottom_left_back_corner.z),
            Point(bottom_left_back_corner.x, bottom_left_back_corner.y + self.side, bottom_left_back_corner.z + self.side),
            Point(bottom_left_back_corner.x + self.side, bottom_left_back_corner.y + self.side, bottom_left_back_corner.z + self.side),
            Point(bottom_left_back_corner.x + self.side, bottom_left_back_corner.y, bottom_left_back_corner.z + self.side),
            Point(bottom_left_back_corner.x, bottom_left_back_corner.y, bottom_left_back_corner.z + self.side)
        ]
        self.min_x, self.max_x, self.min_y, self.max_y, self.min_z, self.max_z = self.corners[0].x, self.corners[0].x, self.corners[0].y, self.corners[0].y, self.corners[0].z, self.corners[0].z
        for corner in self.corners:
            if self.min_x > corner.x:
                self.min_x = corner.x
            if self.max_x < corner.x:
                self.max_x = corner.x
            if self.min_y > corner.y:
                self.min_y = corner.y
            if self.max_y < corner.y:
                self.max_y = corner.y
            if self.min_z > corner.z:
                self.min_z = corner.z
            if self.max_z < corner.z:
                self.max_z = corner.z
    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return "Center: " + str(self.p) + ", Side: " + self.side
    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * self.side ** 2
    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3
    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        if p.x < self.max_x and p.x > self.min_x and p.y < self.max_y and p.y > self.min_y and p.z < self.max_z and p.z > self.min_z:
            return True
        return False
    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        if self.is_inside_point(a_sphere.p) and a_sphere.p.x - a_sphere.r > self.min_x and a_sphere.p.x + a_sphere.r < self.max_x and a_sphere.p.y - a_sphere.r > self.min_y and a_sphere.p.y + a_sphere.r < self.max_y and a_sphere.p.z - a_sphere.r > self.min_z and a_sphere.p.z + a_sphere.r < self.max_z:
            return True
        return False
    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        return False
    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        return False
    # determine if another Cube intersects this Cube
    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        return False
    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        return False
    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        return Sphere()

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__(self, x=0, y=0, z=0, radius=1, height=1):
    pass
    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
  def __str__(self):
    return ""
    # compute surface area of Cylinder
    # returns a floating point number
  def area(self):
    return 0
    # compute volume of a Cylinder
    # returns a floating point number
  def volume(self):
    return 0
    # determine if a Point is strictly inside this Cylinder
    # p is a Point object
    # returns a Boolean
  def is_inside_point(self, p):
    return False
    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
  def is_inside_sphere(self, a_sphere):
    return False
    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
  def is_inside_cube(self, a_cube):
    return False
    # determine if another Cylinder is strictly inside this Cylinder
    # other is Cylinder object
    # returns a Boolean
  def is_inside_cylinder(self, other):
    return False
    # determine if another Cylinder intersects this Cylinder
    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
  def does_intersect_cylinder(self, other):
    return False

def main():
    l = sys.stdin.readline().split()
    p = Point(float(l[0]), float(l[1]), float(l[2]))
    l = sys.stdin.readline().split()
    q = Point(float(l[0]), float(l[1]), float(l[2]))
    l = sys.stdin.readline().split()
    sphereA = Sphere(float(l[0]), float(l[1]), float(l[2]), float(l[3]))
    l = sys.stdin.readline().split()
    sphereB = Sphere(float(l[0]), float(l[1]), float(l[2]), float(l[3]))
    l = sys.stdin.readline().split()
    cubeA = Cube(float(l[0]), float(l[1]), float(l[2]), float(l[3]))
    l = sys.stdin.readline().split()
    cubeB = Cube(float(l[0]), float(l[1]), float(l[2]), float(l[3]))
    l = sys.stdin.readline().split()
    cylA = Cylinder(float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(l[4]))
    l = sys.stdin.readline().split()
    cylB = Cylinder(float(l[0]), float(l[1]), float(l[2]), float(l[3]), float(l[4]))
    is_isnt = ["is", "is not"]
    does_doesnt = ["does", "does not"]
    print("Point p", is_isnt[int(sphereA.is_inside_point(p))], "inside sphereA")
    print("sphereB", is_isnt[int(sphereA.is_inside_sphere(sphereB))], "inside sphereA")
    print("cubeA", is_isnt[int(sphereA.is_inside_cube(cubeA))], "inside sphereA")
    print("cylA", is_isnt[int(sphereA.is_inside_cyl(cylA))], "inside sphereA")
    # read data from standard input
    # read the coordinates of the first Point p
    # create a Point object
    # read the coordinates of the second Point q
    # create a Point object
    # read the coordinates of the center and radius of sphereA
    # create a Sphere object
    # read the coordinates of the center and radius of sphereB
    # create a Sphere object
    # read the coordinates of the center and side of cubeA
    # create a Cube object
    # read the coordinates of the center and side of cubeB
    # create a Cube object
    # read the coordinates of the center, radius and height of cylA
    # create a Cylinder object
    # read the coordinates of the center, radius and height of cylB
    # create a Cylinder object
    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    # print if Point p is inside sphereA
    # print if sphereB is inside sphereA
    # print if cubeA is inside sphereA
    # print if cylA is inside sphereA
    # print if sphereA intersects with sphereB
    # print if cubeB intersects with sphereB
    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA
    # print if Point p is inside cubeA
    # print if sphereA is inside cubeA
    # print if cubeB is inside cubeA
    # print if cylA is inside cubeA
    # print if cubeA intersects with cubeB
    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    # print if Point p is inside cylA
    # print if sphereA is inside cylA
    # print if cubeA is inside cylA
    # print if cylB is inside cylA
    # print if cylB intersects with cylA


if __name__ == "__main__":
  main()
