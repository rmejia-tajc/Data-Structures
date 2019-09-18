import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

# Questions:
# Only ints? 
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
  def __init__(self, value): # We're just using value, so key is value
    self.value = value
    self.left = None
    self.right = None

  # * `insert` adds the input value to the binary search tree, adhering to the
  # rules of the ordering of elements in a binary search tree.
  # Need to traverse to find spot to insert
  
  def insert(self, value):
    pass

  # * `contains` searches the binary search tree for the input value, 
  # returning a boolean indicating whether the value exists in the tree or not.
  # Start from root and traverse the tree
  # We can stop at the first instance of a value
  # We know it's not found if we get to a node that doesn't have children

  def contains(self, target):

    # if the target value is the same as the current node...
    if self.value == target:
      # then the target value does exists in the tree. Return True and it's done searching
      return True

    # if the target value is less than the current node...
    elif self.value > target:

      # if you can't go left - you're at the leaf (end of that branch)...
      if self.left == None:
        # then the target value does NOT exists in the tree. Return False and it's done searching
        return False
      # if you can go left...
      else:
        # then run the search over starting from the node left of the current node (recursion)
        self.left.contains(target)

    #if the target value is more than the current node...
    else:
      # if you can't go right - you're at the leaf (end of that branch)...
      if self.right == None:
        # then the target value does NOT exists in the tree. Return False and it's done searching
        return False
      # if you can go right...
      else:
        # then run the search over starting from the node right of the current node (recursion)
        self.right.contains(target)

    


  # * `get_max` returns the maximum value in the binary search tree.
  def get_max(self):
    pass

  # * `for_each` performs a traversal of _every_ node in the tree, executing
  # the passed-in callback function on each tree node value. There is a myriad of ways to
  # perform tree traversal; in this case any of them should work. 
  def for_each(self, cb):
    pass





    # DAY 2 Project -----------------------
    

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print():
      pass

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(node):
      pass

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(node):
      pass

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
      pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
      pass