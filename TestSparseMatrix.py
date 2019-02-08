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

  def insert_link (self, item):
    new_link=Link(item)
    prev = self.first
    current=self.first
    if(current==None):
      self.first=new_link
      return
    while(new_link.data>current.data):
      prev = current
      current=current.next
      if(current==None):
        break
    new_link.next = current

    prev.next = new_link

  def insert_before (self, col, start, data):
    new_link = Link(col, data)
    cur = self.first
    while (cur.next != start):
      cur = cur.next
    new_link.next = cur.next
    cur.next = new_link

  def delete_link2 (self,link):
    prev = self.first
    cur = self.first
    while (cur != link):
      prev = cur
      cur = cur.next
    prev.next = cur.next

  def delete_link (self, item):
    previous = self.first
    current = self.first

    if (current == None):
      return None

    while (current.data != item):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next
    return

  def insert_last (self, col, data):
    new_link = Link (col, data)
    current = self.first

    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link
  def length (self):
    cur = self.first
    tot = 0
    while (cur != None):
      cur = cur.next
      tot += 1
    return tot

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
          if (count>1):
            list_str+=', '+str(current)
          else:
            list_str+=str(current)
          count+=1
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
    cur = self.matrix[row].first
    while (cur != None):
      if (cur.col == col):
        if (data != 0):
          cur.data = data
          return
        else:
          self.matrix[row].delete_link2(cur)
          return
      elif (col < cur.col):
        if (data != 0):
          self.matrix[row].insert_before(col,cur,data)
        return
      else:
        cur = cur.next
    self.matrix[row].insert_last(col,data)    

  # add two sparse matrices
  def __add__ (self, other):
    new_mat=Matrix(self.row,self.col)
    for i in range(self.row):
      new_row=LinkedList()
      row_s=self.get_row(i)
      row_o=other.get_row(i)
      sum1=0
      for j in range(self.col):
        sum1=row_s[j]+row_o[j]
        new_row.insert_last(j, sum1)
      new_mat.matrix.append(new_row)
      '''new_mat=Matrix(self.row,self.col)
    for i in range (len(self.matrix)):
      linked_row_self=self.matrix[i]
      linked_row_other=other.matrix[i]
      curS=linked_row_self.first
      curO=linked_row_other.first
      row_mat=[]
      new_row=LinkedList()
      for j in range(self.col):
        val=0
        if(curS==None):
          if(curO==None):
            continue
          else:
            val=curO.data
            curO=curO.next
        else:
          if(curO==None):
            val=curS.data
            curS=curS.next
          elif(curS.col==curO.col and curS.col==j):
            val=curS.data + curO.data
            curS=curS.next
            curO=curO.next
          elif(curS.col==j):
            val=curS.data
            curS=curS.next
          elif(curO.col==j):
            val=curO.data
            curO=curO.next
        new_row.insert_last(j, val)
      new_mat.matrix.append(new_row)'''
    return (new_mat)

  # multiply two sparse matrices
  def __mul__ (self, other):
    new_mat=Matrix(self.row,other.col)
    for i in range(self.row):
      row=self.get_row(i)
      mat_row=LinkedList()
      for j in range(other.col):
        col=other.get_col(j)
        sum1=0
        for k in range(len(col)):
          sum1+=row[k]*col[k]
        mat_row.insert_last(j,sum1)
      new_mat.matrix.append(mat_row)
    return (new_mat)

  # return a list representing a row with the zero elements inserted
  def get_row (self, n):
    row_list = []
    cur = self.matrix[n].first
    for j in range(self.col):
      if (cur == None):
        row_list.append(0)
      elif (j == cur.col):
        row_list.append(cur.data)
        cur = cur.next
      else:
        row_list.append(0)
    return row_list

  # return a list representing a column with the zero elements inserted
  def get_col (self, n):
    col_list = []
    for linked_row in self.matrix:
      cur = linked_row.first
      while (cur != None):
        if (cur.col == n):
          col_list.append(cur.data)
          break
        cur = cur.next
      if (cur == None):
        col_list.append(0)
    return col_list

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