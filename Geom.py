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

  # string representation of a circle
  def __str__ (self):

  # test for equality of radius
  def __eq__ (self, other):
    tol = 1.0e-16

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
      

  # determine if two Rectangles overlap (non-zero area of overlap)
  def does_intersect (self, other):

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  def rect_circumscribe (self, c):

  # give string representation of a rectangle
  def __str__ (self):

  # determine if two rectangles have the same length and width
  def __eq__ (self, other):

def main():
  # open the file geom.txt

  # create Point objects P and Q

  # print the coordinates of the points P and Q

  # find the distance between the points P and Q

  # create two Circle objects C and D

  # print C and D

  # compute the circumference of C

  # compute the area of D

  # determine if P is strictly inside C

  # determine if C is strictly inside D

  # determine if C and D intersect (non zero area of intersection)

  # determine if C and D are equal (have the same radius)

  # create two rectangle objects G and H

  # print the two rectangles G and H

  # determine the length of G (distance along x axis)

  # determine the width of H (distance along y axis)

  # determine the perimeter of G

  # determine the area of H

  # determine if point P is strictly inside rectangle G

  # determine if rectangle G is strictly inside rectangle H

  # determine if rectangles G and H overlap (non-zero area of overlap)

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle

  # determine if the two rectangles have the same length and width

  # close the file geom.txt
main()
