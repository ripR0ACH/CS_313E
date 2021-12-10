#  File: Poly.py
#  Description:
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 11/08/2021
#  Date Last Modified: 11/08/2021
import sys
from typing import final

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
            current = self.first
            if current.next == None and exp < current.exp:
                current.next = Link(coeff, exp)
                return
            while current.next != None:
                if exp < current.exp and exp > current.next.exp:
                    current.next = Link(coeff, exp, current.next)
                    return
                elif exp == current.exp:
                    c = coeff + current.coeff
                    print('here', c)
                    current = Link(c, exp, current.next)
                    return c
                current = current.next
            if exp < current.exp:
                current.next = Link(coeff, exp)
                return
            elif exp > current.exp:
                tmp = current
                current = Link(coeff, exp, tmp)
                return
            else:
                c = coeff + current.coeff
                current = Link(c, exp, current.next)
                return
            
    # add polynomial p to this poly nomial and return the sum
    def add (self, p):
        final_poly = LinkedList()
        current = self.first
        while current != None:
            final_poly.insert_in_order(current.coeff, current.exp)
            current = current.next
        current = p.first
        while current != None:
            final_poly.insert_in_order(current.coeff, current.exp)
            current = current.next
        return final_poly
    # multiply polynomial p to this polynomial and return the product
    def mult (self, p):
        pass
    # create a string representation of the polynomial
    def __str__ (self):
        s = ''
        if self.first == None:
            return s
        current = self.first
        while current.next != None:
            s += str(current) + " + "
            current = current.next
        s += str(current)
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
    l = LinkedList()
    print(l.insert_in_order(lists[1].first.coeff, lists[1].first.exp))
    print(lists[0].add(l))

  # create polynomial p

  # create polynomial q

  # get sum of p and q and print sum

  # get product of p and q and print product

if __name__ == "__main__":
  main()