#  File: ExpressionTree.py

#  Description: Creates an expression tree

#  Student's Name: Matthew Frangos

#  Student's UT EID: msf955

#  Partner's Name: Braeden Conrad

#  Partner's UT EID: bsc875

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 4/11/2018

#  Date Last Modified: 4/12/2018

operators=['+', '-', '*', '/']

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack is empty
  def is_empty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

# Create Binary Node class with data and children
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

# Create tree class with a root
class Tree (object):
  def __init__ (self):
    self.root = None

  # Follows algorithm given to make a tree from the given string expression
  def createTree (self, expr):
  	theStack=Stack()
  	array=expr.split()
  	current=Node(None)
  	self.root=current
  	for val in array:
  		if(val=='('):
  			current.lchild=Node(None)
  			theStack.push(current)
  			current=current.lchild
  		elif(val in operators):
  			current.data=val
  			theStack.push(current)
  			current.rchild=Node(None)
  			current=current.rchild
  		elif(val==')'):
  			if(theStack.is_empty()!=True):
  				current=theStack.pop()
  		else:
  			current.data=val
  			current=theStack.pop()

  # Helper function to evaluate, performs rudamentary mathematics
  def operate (self, oper1, oper2, token):
	  if (token == "+"):
	    return oper1 + oper2
	  elif (token == "-"):
	    return oper1 - oper2
	  elif (token == "*"):
	    return oper1 * oper2
	  elif (token == "/"):
	    return oper1 / oper2

  # Runs evaluation of the binary tree
  def evaluate (self, aNode):
	  theStack = Stack()
	  tokens=self.post_order(self.root,[])
	  for item in tokens:
	    if (item in operators):
	      oper2 = theStack.pop()
	      oper1 = theStack.pop()
	      theStack.push (self.operate (oper1, oper2, item))
	    else:
	      theStack.push (float(item))
	  return theStack.pop()
  
  # in order traversal - left, center, right - returns array
  def in_order (self, aNode, array):
    if (aNode != None):
      self.in_order (aNode.lchild, array)
      array.append(aNode.data)
      self.in_order (aNode.rchild, array)
    return array

  # pre order traversal - center, left, right - returns array
  def pre_order (self, aNode, array):
    if (aNode != None):
      array.append(aNode.data)
      self.pre_order (aNode.lchild, array)
      self.pre_order (aNode.rchild, array)
    return array

  # post order traversal - left, right, center - returns array
  def post_order (self, aNode, array):
    if (aNode != None):
      self.post_order (aNode.lchild, array)
      self.post_order (aNode.rchild, array)
      array.append(aNode.data)
    return array

# Prints array in row
def print_array(array):
	for a in array:
		print(str(a), end=' ')
	print()

def main():
	tree=Tree()
	in_file = open ("./expression.txt", "r")
	line=in_file.readline()
	tree.createTree(str(line))
	value=tree.evaluate(tree.root)
	tree.in_order(tree.root,[])
	print(str(line), " = ", str(value))
	print("Prefix Expression:", end=' ')
	print_array(tree.pre_order(tree.root,[]))
	print("Postfix Expression:", end=' ')
	print_array(tree.post_order(tree.root,[]))
main()
