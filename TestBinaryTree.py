#  File: TestBinaryTree.py

#  Description: Write member functions for Tree class

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/12/18

#  Date Last Modified: 04/15/18

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

  # Determines if two binary trees are the same
  def is_similar (self, pNode):
    if (self.root == None and pNode.root == None):
      return True
    elif (self.root == None or pNode.root == None):
      return False
    else:
      return self.is_similar_wrapper(self.root,pNode.root)
    
  # Recursively transverses the binary tree to find equality
  def is_similar_wrapper (self, root1, root2):
    if (root1 == None and root2 == None):
      return True
    elif (root1 == None or root2 == None):
      return False
    else:
      return (root1.data == root2.data) and self.is_similar_wrapper(root1.lChild,root2.lChild) and self.is_similar_wrapper(root1.rChild,root2.rChild)

  # Calls the wrapper function in order to print the level of the tree
  def print_level (self, level):
    if (level > self.get_height()+1):
      return
    level_elements = []
    if (self.root == None):
      print()
      return
    elif (level == 1):
      level_elements.append(self.root.data)
      print(level_elements[0])
    else:
      self.print_level_wrap(self.root,level,level_elements)
      for data in level_elements:
        print(data,end = ' ')
      print()

  # Recursively handles transversal and returns array
  def print_level_wrap(self,aNode,level,array):
    if (level == 1):
      if (aNode != None):
        array.append(aNode.data)
      return
    else:
      if (aNode != None):
        self.print_level_wrap(aNode.lChild,level-1,array)
        self.print_level_wrap(aNode.rChild,level-1,array)
      return

  # Calls wrapping function for get height
  def get_height (self):
    return (self.get_height_wrap(self.root)-1)

  # Recursively analyzes the binary tree to find the max height
  def get_height_wrap(self,root):
    if (root == None):
      return 0
    else:
      return (1+max(self.get_height_wrap(root.lChild),self.get_height_wrap(root.rChild)))

  # Counts the number of nodes in the right and left children of the root
  def num_nodes (self):
    current=self.root
    left=len(self.in_order(current.lChild,[]))
    right=len(self.in_order(current.rChild,[]))
    return(current.data,left,right)

def main():
  # create three trees
  elements = [14]
  elements2 =  [78, 100, 77, 46, 31, 77, 97, 64, 69, 75]
  elements3 =  [94, 50, 64, 87, 99, 84, 54, 93, 80, 76, 90, 60, 95, 17, 38, 72, 15, 
50, 55, 34, 15, 22, 100, 26, 36, 40, 28, 83, 11, 63, 17, 52, 67, 73, 52, 78, 45, 
94, 30, 40, 8, 95, 25, 37, 23, 4, 73, 86, 49, 29, 8, 45, 95, 70, 30, 15, 70, 35, 
58, 87, 67, 7, 40, 9, 87, 58, 64, 81, 83, 45, 80, 81, 55, 10, 39, 27, 24, 21, 62, 
16, 89, 26, 57, 13, 73, 5, 54, 52, 36, 60, 15, 27, 80, 80, 30, 97, 33, 13, 5, 29]
  tree1=Tree()
  tree2=Tree()
  tree3=Tree()
  for i in elements:
    tree1.insert(i)
  for i in elements2:
    tree2.insert(i)
  for i in elements3:
    tree3.insert(i)
  # testing is_similar
  print("Is_similar: ",tree1.is_similar(tree2))

  # print various levels
  print ("Level 1 (tree1):", end = ' ')
  tree1.print_level(1)
  print ("Level 3 (tree2):", end = ' ')
  tree2.print_level(3)
  print ("Level 5 (tree3):", end = ' ')
  tree3.print_level(5)

  # get the height of the two different trees
  print ("Height of tree1: ", tree1.get_height())
  print ("Height of tree2: ", tree2.get_height())
  print ("Height of tree3: ", tree3.get_height())

  # get the total number of nodes of binary search tree
  root,l_length,r_length=tree1.num_nodes()
  print("Tree 1 has", str(l_length+r_length+1), "nodes.")
  root,l_length,r_length=tree2.num_nodes()
  print("Tree 2 has", str(l_length+r_length+1), "nodes.")
  root,l_length,r_length=tree3.num_nodes()
  print("Tree 3 has", str(l_length+r_length+1), "nodes.")

main()
  