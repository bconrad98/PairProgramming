#  File: BST_Cipher.py

#  Description: Write an encryption mechanism using binary trees

#  Student Name: Matthew Frangos

#  Student UT EID: msf955

#  Partner Name: Braeden Conrad

#  Partner UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/18/18

#  Date Last Modified: 04/18/18

class Node (object):
  def __init__ (self, letter):
    self.letter = letter
    self.lChild = None
    self.rChild = None

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
  	self.root = None
  	encrypt_set = set(encrypt_str)
  	for letter in encrypt_set:
  		letter = letter.lower()
  		if (letter == ' '):
  			self.insert(letter)
  		if (letter <= 'a' or letter >= 'z'):
  			continue
  		self.insert(letter)
  	return

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
  	newNode = Node (ch)
  	if (self.root == None):
  		self.root = newNode
  	else:
  		current = self.root
  		parent = self.root
  		while (current != None):
  			parent = current
  			if (ch < current.letter):
  				current = current.lChild
  			else:
  				current = current.rChild
  		if (ch < parent.letter):
  			parent.lChild = newNode
  		elif (ch == parent.letter):
  			return
  		else:
  			parent.rChild = newNode

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
  	current = self.root
  	string = ''
  	if (self.root.letter == ch):
  		return '*'
  	while ((current != None) and (current.letter != ch)):
  		if (ch < current.letter):
  			current = current.lChild
  			string += '<'
  		else:
  			current = current.rChild
  			string += '>'
  	return string

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
  	if (st == '*'):
  		return self.root.letter
  	else:
  		current = self.root
  		for ch in st:
  			if (current == None):
  				return
  			if (ch == '<'):
  				current = current.lChild
  			else:
  				current = current.rChild
  		return current.letter

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
  	return

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
  	return