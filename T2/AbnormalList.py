#  File: AbnormalList.py
#  Description: o detect whether a linked list is abnormal and if so, return the value of the abnormal node.
#  Student Name: zachary morrison
#  Student UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
# DO NOT MODIFY THE FOLLOWING CODE
class Link:
  def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList (object):
  # linked list class
  # create a linked list
  def __init__(self):
    self.first = None
  # add an item at the beginning of the list
  def insert_first(self, item):
    new_link = Link(item)
    new_link.next = self.first
    self.first = new_link
  # add an item at the end of a list
  def insert_last(self, item):
    new_link = Link(item)
    current = self.first
    if(current == None):
      self.first = new_link
      return
    while(current.next != None):
      current = current.next
    current.next = new_link
# YOU ARE FREE TO CHANGE THE FOLLOWING CODE
# DO NOT change name or header of find_abnormality
def find_abnormality(linkedList):
    if not linkedList.first:
        return False
    current = linkedList.first
    list = [current.data]
    while current.next != None:
        current = current.next
        if current.data not in list:
            list.append(current.data)
        else:
            return current.data
    return False
            
    pass
if __name__ == "__main__":
  # write debug statements, test cases, etc (use assert statements)
  # this code will not be run on the autograder, only find_abnormality will be tested
  pass