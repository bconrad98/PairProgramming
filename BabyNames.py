#  File: BabyNames.py

#  Description: Allow a user to query a database of baby names

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 03/20/2018

#  Date Last Modified: 03/20/2018

import urllib.request

def read_file(file_name):
    baby_names = {}
    in_file = open(file_name,"r")
    for line in in_file:
        line = line.strip()
        temp_array = line.split(' ')
        int_array = list(map(int,temp_array[1:]))
        baby_names[temp_array[0]] = int_array
    in_file.close()
    return baby_names

def read_url(url):
   baby_names = {}
   try:
       in_file = urllib.request.urlopen(url)
   except:
       print("Could not open url.")
       return -1
   for line in in_file:
       line = str(line, encoding = 'utf8')
       line = line.strip()
       temp_array = line.split(' ')
       int_array = list(map(int,temp_array[1:]))
       baby_names[temp_array[0]] = int_array
   in_file.close()
   return baby_names

def display_menu():
    print("Options")
    print("Enter 1 to search for names.")
    print("Enter 2 to display data for one name.")
    print("Enter 3 to display all names that appear in one decade.")
    print("Enter 4 to display all names that appear in all decades.")
    print("Enter 5 to display all names that are more popular in every decade.")
    print("Enter 6 to display all names that are less popular in every decade.")
    print("Enter 7 to quit.")
    choice = int(input("Enter choice: "))
    return choice

def name_search(name_dict,name_entered):
    for name in name_dict:
        if (name == name_entered):
            return True
    return False

def show_rankings(name_dict,name_entered):
    if (name_search(name_dict,name_entered)):
        print(name_entered,":",sep='',end=' ')
        for rank in name_dict[name_entered]:
            print(rank,end=' ')
        print()
        for i in range(10):
            decade = "19" + str(i) + "0" + ":"
            print(decade,name_dict[name_entered][i])
        print("2000:",name_dict[name_entered][-1])
        print()
    else:
        print("Name not in database.")
        print()

def alldecades_rank(name_dict):
    name_list = []
    for name in name_dict:
        if (0 not in name_dict[name]):
            name_list.append(name)
    return name_list

def get_decade_index(decade):
    digits = decade%100
    if (decade < 2000):
        index = digits//10
    else:
        index = 10
    return index

def single_decade_rank(name_dict,decade):
    name_list = []
    index = get_decade_index(decade)
    for i in range(1,1001):
        for name in name_dict:
            if (name_dict[name][index] == i):
                name_list.append(name)
    return name_list

def more_popular_names(name_dict):
    more_popular_list = []
    for name in name_dict:
        flag = True
        for i in range (0,len(name_dict[name])-1):
            if (name_dict[name][i]<name_dict[name][i+1]):
                flag = False
            if (0 in name_dict[name]):
                flag = False
        if (flag):
            more_popular_list.append(name)
    return more_popular_list

def less_popular_names(name_dict):
    less_popular_list = []
    for name in name_dict:
        flag = True
        for i in range (0,len(name_dict[name])-1):
            if (name_dict[name][i]>name_dict[name][i+1]):
                flag = False
            if (0 in name_dict[name]):
                flag = False
        if (flag):
            less_popular_list.append(name)
    return less_popular_list

def min_not_zero(nums):
    Min = find_non_zero(nums)
    for i in range(len(nums)):
        if (nums[i] < Min and nums[i]!=0):
            Min = nums[i]
    return Min
def find_non_zero(nums):
    i=0
    while (nums[i]==0):
        i = i+1
    return nums[i]

def main():
  name_dict = read_url("http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt")
  can_read = True
  if (name_dict == -1):
      can_read = False
  choice = display_menu()
  while ((choice < 7 or choice <= 1) and can_read):
      if (choice == 1):
          name = input("Enter a name: ")
          if (name_search(name_dict,name)):
              print()
              print("The matches with their highest ranking decade are:")
              index = name_dict[name].index(min_not_zero(name_dict[name]))
              if (index < 10):
                  decade = "19" + str(index) + "0"
              else:
                  decade = "2000"
              print(name,decade)
              print()
          else:
              print(name,"does not appear in any decade.")
              print()
      elif (choice == 2):
          name = input("Enter a name: ")
          show_rankings(name_dict,name)
      elif (choice == 3):
          decade = int(input("Enter decade: "))
          index = get_decade_index(decade)
          decade_list = single_decade_rank(name_dict,decade)
          for name in decade_list:
              string = name + ":"
              print(string,name_dict[name][index])
          print()
      elif (choice == 4):
          all_decades_list = alldecades_rank(name_dict)
          num = len(all_decades_list)
          print(num,"names appear in every decade. The names are:")
          for name in all_decades_list:
              print(name)
          print()
      elif (choice == 5):
          more_popular_list = more_popular_names(name_dict)
          num = len(more_popular_list)
          print(num,"names are more popular in every decade.")
          for name in more_popular_list:
              print(name)
          print()
      elif (choice == 6):
          less_popular_list = less_popular_names(name_dict)
          num = len(less_popular_list)
          print(num,"names are less popular in every decade.")
          for name in less_popular_list:
              print(name)
          print()
      choice = display_menu()
  print("Goodbye.")
main()
