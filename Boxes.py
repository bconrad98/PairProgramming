#  File: Boxes.py

#  Description: Find the largest subset of boxes that fit

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 02/23/18

#  Date Last Modified: 02/23/18

def does_fit_subset(subset):
    for i in range (len(subset)-1):
        if (not(does_fit(subset[i],subset[i+1]))):
            return False
    return True

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
  #print subsets that have longest length
  longest_boxes = []
  for i in range(len(subset_list)):
      if len(subset_list[i]) == Max :
          longest_boxes.append(subset_list[i])
          
  for i in range (len(longest_boxes)):
  	for j in range (len(longest_boxes[i])):
  		print(longest_boxes[i][j])
  	print()

main()