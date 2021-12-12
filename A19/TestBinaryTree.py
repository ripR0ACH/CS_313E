#  File: TestBinaryTree.py
#  Description: 
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 11/15/2021
#  Date Last Modified: 11/15/2021

import sys
import math

class Node(object):
    def __init__(self, data, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild
    


class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        root = self.root
        while root:
            if root.lchild != None and data < root.data:
                root = root.lchild
                continue
            elif root.rchild != None and data > root.data:
                root = root.rchild
                continue
            elif data > root.data:
                root.rchild = Node(data)
                return
            elif data < root.data:
                root.lchild = Node(data)
                return
    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        return str(self) == str(pNode)
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level): 
        return get_level_helper(self.root, self.get_height(), level)
    # Returns the height of the tree
    def get_height(self): 
        return get_height_helper(self.root)
    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        return num_nodes_helper(self.root) - 1
    def __str__(self):
        return str_tree(self)

def num_nodes_helper(tree, count = 0):
    if tree:
        return num_nodes_helper(tree.lchild, count) + num_nodes_helper(tree.rchild, count)
    else:
        return count + 1
def get_height_helper(tree, h = 0):
    if not tree:
        return h
    if get_height_helper(tree.lchild, h + 1) >= get_height_helper(tree.rchild, h + 1):
        return get_height_helper(tree.lchild, h + 1)
    elif get_height_helper(tree.rchild, h + 1) > get_height_helper(tree.lchild, h + 1):
        return get_height_helper(tree.rchild, h + 1)
def get_level_helper(tree, h, trgt_level, curr_level = 0):
    if trgt_level >= h:
        return ''
    if not tree:
        return ''
    if tree and not tree.rchild and not tree.lchild:
        return str(tree.data) + ' '
    if curr_level == trgt_level:
        return str(tree.data) + ' '
    if curr_level < trgt_level and curr_level < h:
        return get_level_helper(tree.lchild, h, trgt_level, curr_level + 1) + get_level_helper(tree.rchild, h, trgt_level, curr_level + 1)
def str_tree(tree):
    s = ''
    lvl = 0
    h = tree.get_height()
    while lvl < h:
        s += tree.get_level(lvl) + 'down '
        lvl += 1
    return s.strip()
    

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints

    trees = [Tree(), Tree(), Tree()]
    s = ''
    t_inputs = [tree1_input, tree2_input, tree3_input]
    for i in range(3):
        for item in t_inputs[i]:
            trees[i].insert(item)
    print(str(tree1_input) + '\n' + str(tree2_input) + '\n' + str(tree3_input))
    for i in range(3):
        print(f'Tree #{i + 1}:\t {trees[i]}')
    # Test your method is_similar()
    
    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
    main()