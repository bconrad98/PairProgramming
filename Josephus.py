#  File: Josephus.py

#  Description: Print the order in which soldiers are executed

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 03/31/18

#  Date Last Modified: 04/01/18

# Creates list for printed order
kill_list=[]

class Link(object):
	def __init__(self,data,next = None):
		self.data = data
		self.next = None

class CircularList(object):
	def __init__(self):
		self.first = Link(1)
		self.first.next = self.first #head points to itself

	# Inserts an element into the list
	def insert(self,item):
		cur=self.first
		new_link = Link(item)
		if(cur==None):
			self.first=new_link
			new_link.next=self.first
		else:
			while (cur.next != self.first):
				cur = cur.next
			new_link.next=cur.next
			cur.next=new_link
		
	# Find the link with the given key
	def find(self,key):
		cur = self.first
		if (key == cur.data):
			return cur
		cur=cur.next
		while (cur != self.first):
			if (key == cur.data):
				return cur
			cur = cur.next
		return None

	# Deleta a link with a given key
	def delete (self,key):
		prev = self.first
		cur = self.first.next
		if(cur==None):
			return None
		while(cur.data!=key):
			prev = cur
			cur = cur.next
		if (cur == self.first):
			self.first = cur.next
			prev.next=cur.next
		else:
			prev.next = cur.next

	# Delete the nth link starting from the Link start
	# Return the next link from the deleted link
	def delete_after(self,start,n): #this needs work
		cur = start
		for i in range(n-1):
			cur = cur.next
		next_link=cur.next
		kill_list.append(cur.data)
		self.delete(cur.data)
		
		return next_link

	# Return a string representation of a Circular list
	def __str__(self):
		cur=self.first
		count = 1
		string = str(cur.data)+ ' '
		cur=cur.next
		while (cur != self.first):
			count += 1
			if (count > 10):
				string += '\n'
				string += str(cur.data) + ' '
				count = 1
			else:
				string += str(cur.data) + ' '
			cur = cur.next
		return string

	def length(self):
		cur = self.first
		count = 1
		cur=cur.next
		while (cur != self.first):
			count += 1
			cur = cur.next
		return count	

def main():
	# Creates object list and reads file
	circular_list = CircularList()
	in_file = open("josephus.txt",'r')
	num_soldiers = int(in_file.readline().strip())

	# Creates the circular list of soldiers
	for i in range (2,num_soldiers+1):
		circular_list.insert(i)
	start = circular_list.find(int(in_file.readline().strip()))
	n = int(in_file.readline().strip())
	
	# Runs program to kill soldiers
	while (circular_list.length() > 1):
		start = circular_list.delete_after(start,n)
	
	# Print list of soldiers killed in order
	for i in range (0,len(kill_list)):
		print(kill_list[i])
	print(circular_list.first.data)
	
main()
