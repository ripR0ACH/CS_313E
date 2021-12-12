import sys

# A class to represent a single Node in the Tree
class Node:
    def __init__(self, data, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

def height_helper(node):
    if node is None:
      return -1
    else:
      l_height = height_helper(node.lChild)
      r_height = height_helper(node.rChild)

      if l_height > r_height:
        return l_height + 1
      else:
        return r_height + 1

def get_level_helper(tree, trgt_level, curr_level = 1):
    if not tree:
      return 0
    if curr_level == trgt_level:
        return 1
    elif curr_level < trgt_level:
        return get_level_helper(tree.lChild, trgt_level, curr_level + 1) + get_level_helper(tree.rChild, trgt_level, curr_level + 1)

# Input -
#   root: a Node object that represents the root of the tree 
#   row: the row being examined. So, the row containing
#   the root is row 1. The row underneath is row 2. etc.
# Output - an int representing the number of nodes in a given row
def num_level_nodes(root, row):
  # Implement method to find number of nodes given a row number
  if row <= height_helper(root):
    return get_level_helper(root, row)

def main():
  pass

if __name__ == "__main__":
  main()  
