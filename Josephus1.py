#  File: Josephus.py

#  Description: Print the order in which soldiers are executed

#  Student Name: Braeden Conrad

#  Student UT EID: bsc875

#  Partner Name: Matthew Frangos

#  Partner UT EID: msf955

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: 03/31/18

#  Date Last Modified: 03/31/18
kill_list=[]

class Link(object):
	def __init__(self,data,next = None):
		self.data = data
		self.next = None

class CircularList(object):
	def __init__(self):
		self.first = Link(1)
		self.first.next = self.first #head points to itself

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

	def delete (self,key):
		prev = self.first
		cur = self.first
		if(cur==None):
			return None
		while(cur.data!=key):
			prev = cur
			cur = cur.next
		if (cur == self.first):
			self.first = self.first.next
		else:
			prev.next = cur.next


	def delete_after(self,start,n): #this needs work
		cur = start
		for i in range(n-1):
			cur = cur.next
		next_link=cur.next
		kill_list.append(cur.data)
		self.delete(cur.data)
		
		return next_link

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
	circular_list = CircularList()
	in_file = open("josephus.txt",'r')
	num_soldiers = int(in_file.readline().strip())
	for i in range (2,num_soldiers+1):
		circular_list.insert(i)
	print(circular_list)
	start = circular_list.find(int(in_file.readline().strip()))
	print(start)
	n = int(in_file.readline().strip())
	print(circular_list.length())
	while (circular_list.length() > 1):
		start = circular_list.delete_after(start,n)
		
	print("Last element:",circular_list.first.data)
	print(circular_list)
	print(kill_list)
	print(len(kill_list))

main()
