#  File: TopoSort.py

#  Description: Runs a topological sort

#  Student's Name: Matthew Frangos

#  Student's UT EID: msf955

#  Partner's Name: Braeden Conrad

#  Partner's UT EID: bsc875

#  Course Name: CS 313E 

#  Unique Number: 51335

#  Date Created: 5/3/2018

#  Date Last Modified: 5/3/2018

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

  def is_inside(self,label):
    labels = []
    while (not self.isEmpty()):
      labels.append(self.pop())
    labels.reverse()
    for val in labels:
      self.push(val)
    if (label in labels):
      return True
    return False

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

  def modAdjUnvisitedVertex (self, stack):
    nVert = len(self.Vertices)
    v = stack.peek()
    for i in range (nVert):
      if (self.adjMat[v][i] > 0 and (self.Vertices[i]).wasVisited()):
        if (stack.is_inside(i)):
          return -2
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  def deleteVertex (self, vertexLabel):
    vertex=self.getIndex(vertexLabel)
    for i in range(len(self.adjMat)):
      del(self.adjMat[i][vertex])
    del(self.adjMat[vertex])
    del(self.Vertices[vertex])

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
    # the queue is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # determine if a directed graph has a cycle
  def hasCycle (self):
    nVert = len(self.Vertices)
    for v in range(nVert):
      # create a Stack
      theStack = Stack()

      # mark vertex v as visited and push on the stack
      (self.Vertices[v]).visited = True
      theStack.push (v)

      # vist other vertices according to depth
      while (not theStack.isEmpty()):
        # get an adjacent unvisited vertex
        u = self.modAdjUnvisitedVertex (theStack)
        if (u == -1): 
          u = theStack.pop()
        elif (u == -2):
          nVert = len (self.Vertices)
          for i in range (nVert):
            (self.Vertices[i]).visited = False
          return True
        else:
          (self.Vertices[u]).visited = True
          theStack.push(u)
      # the stack is empty let us reset the flags
      nVert = len (self.Vertices)
      for i in range (nVert):
        (self.Vertices[i]).visited = False
    return False

  # return a list of vertices after a topological sort
  def toposort (self):
  	copy=Graph()
  	copy.Vertices=self.Vertices
  	copy.adjMat=self.adjMat
  	topo_visit=[]
  	delete_list=[]
  	idx=0
  	while(len(copy.Vertices)>0):
  		idx=0
	  	while(idx<len(copy.Vertices)):
	  		has_visit=False
	  		vertex=copy.Vertices[idx].label
	  		for i in range(len(copy.Vertices)):
	  			if(copy.adjMat[i][idx]==1):
	  				has_visit=True
	  				break
	  		if(has_visit):
	  			idx+=1
	  		else:
	  			topo_visit.append(vertex)
	  			delete_list.append(vertex)
	  			idx+=1
	  	while(len(delete_list)>0):
	  		copy.deleteVertex(delete_list[0])
	  		delete_list.pop(0)
  	return topo_visit   

def main():
  # create a Graph object
  graph = Graph()

  # open file for reading
  inFile = open ("./topo.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())

  for i in range (numVertices):
    letter = (inFile.readline()).strip()
    graph.addVertex (letter)

  # read the edges
  numEdges = int ((inFile.readline()).strip())

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    edge = edge.split()
    start = graph.getIndex(edge[0])
    finish = graph.getIndex(edge[1])

    graph.addDirectedEdge (start, finish)

  # test if it has a cycle
  print ('Cycle Present:', graph.hasCycle())

  # test topological sort
  print ('Topological Sort:')
  print(graph.toposort())

main()

