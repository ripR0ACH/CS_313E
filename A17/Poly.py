#  File: Poly.py
#  Description:
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 11/08/2021
#  Date Last Modified: 11/08/2021
import sys

class Link (object):
    def __init__ (self, coeff = 1, exp = 1, next = None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__ (self):
        return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
    def __init__ (self):
        self.first = None
    # keep Links in descending order of exponents
    def insert_in_order (self, coeff, exp):
        if self.first == None:
            self.first = Link(coeff, exp)
        else:
            if self.first.next == None and self.first.exp > exp:
                self.first.next = Link(coeff, exp)

    # add polynomial p to this poly nomial and return the sum
    def add (self, p):
        pass
    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        pass
    # create a string representation of the polynomial
    def __str__ (self):
        s = ''
        current = self.first
        while current != None:
            s += str(current) + " "
            current = current.next
        return s
        

def main():
    # read data from file poly.in from stdin
    lists = [LinkedList(), LinkedList()]
    for list in lists:
        n = int(sys.stdin.readline().strip())
        for i in range(n):
            line = sys.stdin.readline().strip().split()
            list.insert_in_order(int(line[0]), int(line[1]))
        sys.stdin.readline()
        print(list)
    print(lists[0].add(lists[1]))
    print(lists[0])

  # create polynomial p

  # create polynomial q

  # get sum of p and q and print sum

  # get product of p and q and print product

if __name__ == "__main__":
  main()