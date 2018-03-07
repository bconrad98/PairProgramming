#  File: Triangle.py
#  Description: Use algorithms to find the greatest path sum of a triangle
#  Student's Name: Matthew Frangos
#  Student's UT EID: msf955
#  Partner's Name: Braeden Conrad
#  Partner's UT EID: bsc875
#  Course Name: CS 313E 
#  Unique Number: 51335
#  Date Created: 3/7/2018
#  Date Last Modified:
import time
# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
  return

# returns the greatest path sum using greedy approach
def greedy (grid):
  return

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
  return

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  return

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  return 

def main ():
  # read triangular grid from file

  ti = time.time()
  # output greates path from exhaustive search
  tf = time.time()
  del_t = tf - ti
  # print time taken using exhaustive search

  ti = time.time()
  # output greates path from greedy approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using greedy approach

  ti = time.time()
  # output greates path from divide-and-conquer approach
  tf = time.time()
  del_t = tf - ti
  # print time taken using divide-and-conquer approach

  ti = time.time()
  # output greates path from dynamic programming 
  tf = time.time()
  del_t = tf - ti
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()