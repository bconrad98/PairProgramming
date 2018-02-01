#  File: Geom.py
#  Description: Calculates different components of geometric figures.
#  Student Name: Matthew Frangos
#  Student UT EID: msf955
#  Partner Name: Braeden Conrad
#  Partner UT EID: bsc875
#  Course Name: CS 313E
#  Unique Number: 51335
#  Date Created: 1/31/2018
#  Date Last Modified: 1/31/2018

import math

class Point (object):
  # constructor
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist(c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist(c.center)
    return distance < (self.radius + c.radius)

  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    x = (r.ul.x + r.lr.x)/2
    y = (r.ul.y + r.lr.y)/2
    center = Point(x,y)
    radius = center.dist(r.ul)
    return Circle(radius,x,y)

  # string representation of a circle
  def __str__ (self):
    return "Center: " + str(self.center) + " Radius: " + str(round(self.radius,2))

  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16
    return (abs(self.radius - other.radius) < tol) and (abs(self.center.dist(other.center) < tol))

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  def length (self):
    return self.lr.x - self.ul.x

  # determine width of Rectangle (distance along the y axis)
  def width (self):
    return self.ul.y - self.lr.y

  # determine the perimeter
  def perimeter (self):
    return 2*(self.width()+self.length())

  # determine the area
  def area (self):
    return self.length()*self.width()

  # determine if a point is strictly inside the Rectangle
  def point_inside (self, p):
    return (p.x > self.ul.x and p.x < self.lr.x) and (p.y > self.lr.y and p.y < self.ul.y)

  # determine if another Rectangle is strictly inside this Rectangle
  def rectangle_inside (self, r):
    return (r.ul.x > self.ul.x) and (r.ul.y < self.ul.y) and (r.lr.x < self.lr.x) and (r.lr.y > self.lr.y)

  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):
    return not((other.ul.x > self.lr.x) or (other.lr.x < self.ul.x) or (other.lr.y > self.ul.y) or (other.ul.y < self.lr.y))

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):
    ul_x = c.center.x - c.radius
    ul_y = c.center.y + c.radius
    lr_x = c.center.x + c.radius
    lr_y = c.center.y - c.radius
    return Rectangle(ul_x,ul_y,lr_x,lr_y)

  def get_center (self):
    return Point((self.lr.x-self.ul.x)/2,(self.ul.y-self.lr.y)/2)

  # give string representation of a rectangle
  def __str__ (self):
    return "UL: " + str(self.ul) + " LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):
    tol = 1.0e-16
    self_center = self.get_center()
    other_center = other.get_center()
    distance = abs(self_center.dist(other_center))
    return (distance < tol) and (abs(self.length()-other.length())) and (abs(self.width()-other.width()))

def main():
  # open the file geom.txt
  in_file=open("./geom.txt","r")
  coordinates=[]
  for line in in_file:
    line=line.strip()
    words=line.split()
    for numbers in words:
      try:
        coordinates.append(float(numbers))
      except:
        continue
  # create Point objects P and Q
  P=Point(coordinates[0],coordinates[1])
  Q=Point(coordinates[2],coordinates[3])

  # print the coordinates of the points P and Q
  print("Coordinates of P:", P)
  print("Coordinates of Q:", Q)

  # find the distance between the points P and Q
  print("Distance between P and Q:", round(P.dist(Q),2))

  # create two Circle objects C and D
  C=Circle(coordinates[6],coordinates[4],coordinates[5])
  D=Circle(coordinates[9],coordinates[7],coordinates[8])

  # print C and D
  print("Circle C:", C)
  print("Circle D:", D)

  # compute the circumference of C
  print("Circumference of C:", round(C.circumference(),2))

  # compute the area of D
  print("Area of D:", round(D.area(),2))

  # determine if P is strictly inside C
  if(C.point_inside(P)):
    print ("P is inside C")
  else:
    print ("P is not inside C")

  # determine if C is strictly inside D
  if(D.circle_inside(C)):
    print ("C is inside D")
  else:
    print ("C is not inside D")

  # determine if C and D intersect (non zero area of intersection)
  if(D.does_intersect(C)):
    print ("C does intersect D")
  else:
    print ("C does not intersect D")

  # determine if C and D are equal (have the same radius)
  if(C==D):
    print ("C is equal to D")
  else:
    print ("C is not equal to D")

  # create two rectangle objects G and H
  G=Rectangle(coordinates[10],coordinates[11],coordinates[12],coordinates[13])
  H=Rectangle(coordinates[14],coordinates[15],coordinates[16],coordinates[17])

  # print the two rectangles G and H
  print("Rectangle G:", G)
  print("Rectangle H:", H)

  # determine the length of G (distance along x axis)
  print("Length of G:", G.length())

  # determine the width of H (distance along y axis)
  print("Width of H:", H.width())

  # determine the perimeter of G
  print("Perimeter of G:", G.perimeter())
  # determine the area of H
  print("Area of H:", H.area())
  # determine if point P is strictly inside rectangle G
  if(G.point_inside(P)):
    print ("P is inside G")
  else:
    print ("P is not inside G")

  # determine if rectangle G is strictly inside rectangle H
  if(H.rectangle_inside(G)):
    print ("G is inside H")
  else:
    print ("G is not inside H")
  # determine if rectangles G and H overlap (non-zero area of overlap)
  if(H.does_intersect(G)):
    print ("G does overlap H")
  else:
    print ("G does not overlap H")
  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print("Circle that circumscribes G:", Circle().circle_circumscribes(G))
  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print("Rectangle that circumscribes D:", Rectangle().rect_circumscribe(D))
  # determine if the two rectangles have the same length and width
  if(G==H):
    print ("Rectangle G is equal to H")
  else:
    print ("Rectangle G is not equal to H")
  # close the file geom.txt
  in_file.close()

main()
