#  File: Graph.py

#  Description: Write an encryption mechanism using binary trees

#  Student Name: Matthew Frangos

#  Student UT EID: msf955

#  Partner Name: Braeden Conrad

#  Partner UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 04/18/18

#  Date Last Modified: 04/19/18

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()
    # add the vertex to the Queue
    theQueue.enqueue(v)
    # mark the vertex as visited
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    # set vertex as start
    vertex = v
    while (not theQueue.isEmpty()):
    	# get the next univisited vertex until none left
    	u = self.getAdjUnvisitedVertex(vertex)
    	while (u != -1):
    		(self.Vertices[u]).visited = True
    		print (self.Vertices[u])
    		theQueue.enqueue(u)
    		u = self.getAdjUnvisitedVertex(vertex)
    	# if next unvisited vertex not found, dequeue and make that the vertex for next level
    	if (u == -1):
    		vertex = theQueue.dequeue()

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):

  # get a copy of the list of vertices
  def getVertices (self):

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):

def main():
  # test depth first search

  # test breadth first search

  # test deletion of an edge

  # test deletion of a vertex

main()