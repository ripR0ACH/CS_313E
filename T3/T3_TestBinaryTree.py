#  File: TestBinaryTree.py

'''
 Description: Use get_height() function in programming assignment to determine the
balance factor of a node and then determine if the tree is balanced. Implement
get_balance_factor (self, aNode) returns the absolute value of difference in height of left and right subtree
is_balanced (self) returns true if balanced and false if not balanced. A balanced tree has a absolute difference no more than 1
'''
#  Student Name: 

#  Student UT EID: 

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 12/3/2021

#  Date Last Modified: 12/3/2021

import sys
import random
import math
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
    # self.parent = None
    # self.visited = False

  def __str__ (self):
    s = ''
    return s

class Tree (object):
  def __init__ (self):
    self.root = None
    # self.size = 0

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
                current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # takes in the current node and the current height and returns the new height
  def height_helper(self, aNode):
    if aNode is None:
      return -1;
    else:
      l_height = self.height_helper(aNode.lChild)
      r_height = self.height_helper(aNode.rChild)

      if l_height > r_height:
        return l_height + 1
      else:
        return r_height + 1

  # returns the absolute value of difference in height of left and right subtree
  def get_balance_factor (self, aNode):
    return int(math.sqrt((self.height_helper(aNode.lChild) - self.height_helper(aNode.rChild)) ** 2))
  # returns true if balanced and false if not balanced. A balanced tree has a balance factor no more than 1
  def is_balanced (self, aNode):
    if self.get_balance_factor(aNode) == 0 or self.get_balance_factor(aNode) == 1:
      return True
    else:
      return False
      

      

 
def main():
    # DO NOT MODIFY MAIN
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints
    tree1 = Tree()
    for i in tree1_input:
        tree1.insert(i)
    print(tree1.is_balanced(tree1.root))

if __name__ == "__main__":
  main()