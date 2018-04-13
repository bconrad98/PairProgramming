#  File: TestBinaryTree.py

#  Description: Creates and test a binary search tree

#  Student's Name: Matthew Frangos

#  Student's UT EID: msf955

#  Partner's Name: Braeden Conrad

#  Partner's UT EID: bsc875

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 4/12/2018

#  Date Last Modified: 4/12/2018

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # search for a node with a key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lchild
      else:
        current = current.rchild
    return current

  # insert a node in a tree
  def insert (self, val):
    new_node = Node (val)

    if (self.root == None):
      self.root = new_node
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lchild
        else:
          current = current.rchild
      if (val < parent.data):
        parent.lchild = new_node
      else:
        parent.rchild = new_node

  # in order traversal - left, center, right
  def in_order (self, aNode):
    if (aNode != None):
      self.in_order (aNode.lchild)
      print (aNode.data)
      self.in_order(aNode.rchild)

  # pre order traversal - center, left, right
  def pre_order (self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.pre_order (aNode.lchild)
      self.pre_order (aNode.rchild)

  # post order traversal - left, right, center
  def post_order (self, aNode):
    if (aNode != None):
      self.post_order (aNode.lchild)
      self.post_order (aNode.rchild)
      print (aNode.data)

  # return the node with minimum value
  def min_node (self):
    current = self.root

    if (current == None):
      return None

    while (current.lchild != None):
      current = current.lchild

    return current



  # return the node with maximum value
  def max_node (self):
    current = self.root
    
    return current
      

  # delete a node with a given key
  def delete (self, key):
    delete_node = self.root
    parent = self.root
    is_left = False

    # if empty tree
    if (delete_node == None):
      return None

    # find the delete node
    while (delete_node != None) and (delete_node.data != key):
      parent = delete_node
      if (key < delete_node.data):
        delete_node = delete_node.lchild
        is_left = True
      else:
        delete_node = delete_node.rchild
        is_left = False

    # if node not found
    if (delete_node == None):
      return None

    # check if delete node is a leaf node
    if (delete_node.lchild == None) and (delete_node.rchild == None):
       if (delete_node == self.root):
         self.root = None
       elif (is_left):
         parent.lchild = None
       else: 
         parent.rchild = None

    # delete node is a node with only a left child
    elif (delete_node.rchild == None):
      if (delete_node == self.root):
        self.root = delete_node.lchild
      elif (is_left):
        parent.lchild = delete_node.lchild
      else:
        parent.rchild = delete_node.lchild

    # delete node has both left and right children
    else:
      # find delete node's successor and the successor's parent node
      successor = delete_node.rchild
      successor_parent = delete_node

      while (successor.lchild != None):
        successor_parent = successor
        successor = successor.lchild

      # successor node is right child of delete node
      if (delete_node == self.root):
        self.root = successor
      elif (is_left):
        parent.lchild = successor
      else:
        parent.rchild = successor

      # connect delete node's left child to be the successor's left child
      successor.lchild = delete_node.lchild

      # successor node left descendant of delete node
      if (successor != delete_node.rchild):
        successor_parent.lchild = successor.rchild
        successor.rchild = delete_node.rchild

      return delete_node
