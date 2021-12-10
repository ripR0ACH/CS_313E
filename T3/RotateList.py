class Link:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList (object):
  # linked list class
  # feel free to add helper methods but do not change existing methods

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

  def rotate(self, k):
    # rotates self by k spaces
    rotate_helper(self, k)

def rotate_helper(linked_list, k):
  if linked_list.first != None and k > 0:
    linked_list.insert_last(linked_list.first.data)
    linked_list.first = linked_list.first.next
    rotate_helper(linked_list, k - 1)

if __name__ == "__main__":
  # write debug statements, test cases, etc (use assert statements)
  # this code will not be run on the autograder, only rotate will be tested
  pass
