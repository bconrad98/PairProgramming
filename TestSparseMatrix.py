# File: TestSparseMatrix.py

# Description: Sparse matrix representation has a 1-D list where each
#              element in that list is a linked list having the column
#              number and non-zero data in each link

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/04/18

#  Date Last Modified: 04/05/18

class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  # return a String representation of a Link (col, data)
  def __str__ (self):
    return '(' + str(self.col) + ', ' + str(self.data) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # return a String representation of a LinkedList
  def __str__ (self):
    current=self.first
    count=0
    list_str=''
    while(current!=None):
      count=1
      while(count<11):
        if(current==None):
          break
        else:
          count+=1
          list_str+=str(current.data)+'  '
          current=current.next
      list_str+='\n'
    return list_str


class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []

  # perform assignment operation: matrix[row][col] = data
  def set_element (self, row, col, data):
    return    

  # add two sparse matrices
  def __add__ (self, other):
    return

  # multiply two sparse matrices
  def __mul__ (self, other):
    return

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    return

  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    return

  # return a String representation of a matrix
  def __str__ (self):
    s = ''
    for linked_row in self.matrix:
      cur = linked_row.first
      for j in range(self.col):
        if (cur == None):
          s += '%-4s ' % (0)
        elif (j == cur.col):
          s += '%-4s ' % (cur.data)
          cur = cur.next
        else:
          s += '%-4s ' % (0)
      s += '\n'
    return s

def read_matrix (in_file):
  line = in_file.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = Matrix (row, col)

  for i in range (row):
    line = in_file.readline().rstrip("\n").split()
    new_row = LinkedList()
    for j in range (col):
      elt = int (line[j])
      if (elt != 0):
        new_row.insert_last(j, elt)
    mat.matrix.append (new_row)
  line = in_file.readline()

  return mat

def main():
  in_file = open ("./matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = read_matrix (in_file)
  print (matA)
  matB = read_matrix (in_file)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  matP = read_matrix (in_file)
  print (matP)
  matQ = read_matrix (in_file)
  print (matQ)

  matR = matP * matQ
  print (matR)

  print ("\nTest Setting a Zero Element to a Non-Zero Value")
  matA.set_element (1, 1, 5)
  print (matA)

  print ("\nTest Setting a Non-Zero Elements to a Zero Value")
  matB.set_element (1, 1, 0)
  print (matB)

  print ("\nTest Getting a Row")
  row = matP.get_row(1)
  print (row)

  print ("\nTest Getting a Column")
  col = matQ.get_col(0)
  print (col)
  
  in_file.close()

main()