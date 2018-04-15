#  File: TestBinaryTree.py

#  Description: Write member functions for Tree class

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/12/18

#  Date Last Modified: 04/12/18

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

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

  # in order traversal - left, center, right - returns array
  def in_order (self, aNode, array):
    if (aNode != None):
      self.in_order (aNode.lChild, array)
      array.append(aNode.data)
      self.in_order (aNode.rChild, array)
    return array

  # pre order traversal - center, left, right - returns array
  def pre_order (self, aNode, array):
    if (aNode != None):
      array.append(aNode.data)
      self.pre_order (aNode.lChild, array)
      self.pre_order (aNode.rChild, array)
    return array

  # post order traversal - left, right, center - returns array
  def post_order (self, aNode, array):
    if (aNode != None):
      self.post_order (aNode.lChild, array)
      self.post_order (aNode.rChild, array)
      array.append(aNode.data)
    return array

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
        isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
        successor.rChild = deleteNode.rChild

    return True
  def is_similar (self, pNode):
    if (self.root == None and pNode.root == None):
      return True
    elif (self.root == None or pNode.root == None):
      return False
    current1 = self.root
    current2 = pNode.root

    #check through the left tree
    while (current1 != None and current2 != Null):
      if (current1.data != current2.data):
        return False
      current1 = current1.lChild
      currtent2 = current2.lChild
    # check through right tree
    current1 = self.root
    current2 = pNode.root
    while (current1 != None and current2 != Null):
      if (current1.data != current2.data):
        return False
      current1 = current1.rChild
      currtent2 = current2.rChild
    return True

  def print_level (self, level):
    return



  def get_height (self):
    return


  def num_nodes (self):
    current=self.root
    left=len(self.in_order(current.lChild,[]))
    right=len(self.in_order(current.rChild,[]))
    return(current.data,left,right)

def main():
  # create three trees
  elements = [50,30,70,10,40,60,80,7,25,38,47,58,65,77,96]
  elements2 = [50,30,70,10,40,44,62,80,7,25,99,38,47,1,27,58,65,77,96]
  tree1=Tree()
  tree2=Tree()
  tree3=Tree()
  for i in elements:
    tree1.insert(i)
    tree2.insert(i)
  for i in elements2:
    tree3.insert(i)
  root,l_length,r_length=tree1.num_nodes()
  print(root,l_length,r_length)

main()
  