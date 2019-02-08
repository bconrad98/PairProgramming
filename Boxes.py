#  File: Boxes.py

#  Description: Find the largest subset of boxes that fit

#  Student Name: Matthew Frangos

#  Student UT EID: msf955

#  Partner Name: Braeden Conrad

#  Partner UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 02/23/18

#  Date Last Modified: 02/23/18

# Checks if the subset from the subsets have boxes that all fit
def does_fit_subset(subset):
    for i in range (len(subset)-1):
        if (not(does_fit(subset[i],subset[i+1]))):
            return False
    return True

# Produces all subsets of a list
def subsets (a, b, lo, subsets_list):
  hi = len(a)
  if (lo == hi):
    if (does_fit_subset(b)):
      subsets_list.append(b)
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1,subsets_list)
    subsets (a, b, lo + 1,subsets_list)

# Check if one box fits inside another
def does_fit (box1, box2):
  return (box1[0] < box2[0]) and (box1[1] < box2[1]) and (box1[2] < box2[2])

def main():
  # open file for reading
  in_file = open ('boxes.txt', 'r')

  # read the number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)

  # create empty list of boxes
  box_list = []

  # read the list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    box = line.split()
    for i in range (len(box)):
      box[i] = int (box[i])
    box.sort()
    box_list.append (box)

  # close the file
  in_file.close()

  # sort the box list
  box_list.sort()

  # create a list that will hold the nested boxes
  subset_list = []
  b = []

  # fill list will hold all subsets that fit
  subsets(box_list,b,0,subset_list)

  #find the longest length of the subset list
  Max = len(subset_list[0])
  for i in range(len(subset_list)):
      if len(subset_list[i]) > Max :
          Max = len(subset_list[i])

  # Create new array of the correct subsets of max length
  longest_boxes = []
  for i in range(len(subset_list)):
      if len(subset_list[i]) == Max :
          longest_boxes.append(subset_list[i])

  longest_boxes.sort()
  for i in range (len(longest_boxes)):
  	for j in range (len(longest_boxes[i])):
  		print(longest_boxes[i][j])
  	print()

main()
