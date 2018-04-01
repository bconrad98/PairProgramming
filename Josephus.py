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

class Link(object):
	def __init__(self,data,next = None):
		self.data = data
		self.next = None
class CircularList(object):
	def __init__(self):
		self.head = Link(None)
		self.head.next = self.head #head points to itself
	def insert(self,item):
		new_link = Link(item)
		cur = self.head.next
		while (cur.next != self.head):
			cur = cur.next
		cur.next = new_link
		new_link.next = self.head
	def find(self,key):
		cur = self.head.next
		while (cur != self.head):
			if (key == cur.data):
				return cur
			cur = cur.next
		return None

	def delete (self,key):
		prev = self.head.next
		cur = self.head.next
		while (cur != self.head):
			if (cur.data == key):
				break
			prev = cur
			cur = cur.next
		if (cur == self.head):
			return None
		prev.next = cur.next

	def delete_after(self,start,n): #this needs work
		cur = start
		for i in range(n-1):
			cur = cur.next
		if (cur == self.head):
			cur = cur.next
		if (cur.next == self.head):
			next_link = cur.next.next
		else: 
			next_link = cur.next
		self.delete(cur.data)
		
		return next_link

	def __str__(self):
		cur=self.head.next
		count = 0
		string = ''
		while (cur != self.head):
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
		cur = self.head.next
		count = 0
		while (cur != self.head):
			count += 1
			cur = cur.next
		return count	

def main():
	circular_list = CircularList()
	in_file = open("josephus.txt",'r')
	num_soldiers = int(in_file.readline().strip())
	for i in range (1,num_soldiers+1):
		circular_list.insert(i)
	start = circular_list.find(int(in_file.readline().strip()))
	n = int(in_file.readline().strip())
	while (circular_list.length() > 1):
		start = circular_list.delete_after(start,n)
		print(start.data-1)
	print("Last element:",circular_list.head.next.data)

main()
