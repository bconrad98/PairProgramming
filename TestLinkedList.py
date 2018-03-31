#  File: TestLinkedList.py

#  Description: Implement different methods for Linked List class

#  Student Name: Matthew Frangos

#  Student UT EID: msf955

#  Partner Name: Braeden Conrad

#  Partner UT EID: bsc875

#  Course Name: CS313E

#  Unique Number: 51340

#  Date Created: 3/27/2018

#  Date Last Modified: 3/30/2018

class Link (object):
	def __init__ (self, data, next = None):
		self.data = data
		self.next = next

class LinkedList (object):
	def __init__ (self):
		self.first=None

  # get number of links
	def get_num_links (self):
		current=self.first
		count=1
		if(current==None):
			return 0
		while (current != None):
			current = current.next
			count+=1
		return count

  # add an item at the beginning of the list
	def insert_first (self, item):
	  new_link = Link (item)
	  new_link.next = self.first
	  self.first = new_link

	# add an item at the end of a list
	def insert_last (self, item):
		new_link = Link (item)

		current = self.first
		if (current == None):
			self.first = new_link
			return

		while (current.next != None):
			current = current.next

		current.next = new_link

  # add an item in an ordered list in ascending order
	def insert_in_order (self, item):
		new_link=Link(item)
		prev = self.first
		current=self.first
		if(current==None):
			self.first=new_link
			return
		while(new_link.data>current.data):
			prev = current
			current=current.next
			if(current==None):
				break
		new_link.next = current
		prev.next = new_link

  # search in an unordered list, return None if not found
	def find_unordered (self, item):
		current = self.first

		if (current == None):
			return None

		while (current.data != item):
			if (current.next == None):
				return None
			else:
				current = current.next

		return current

  # Search in an ordered list, return None if not found
	def find_ordered (self, item):
		current=self.first
		if(current==None):
			return None
		while(item>current.data):
			current=current.next
			if(current==None):
				break
		if(current==None):
			return None
		elif(current.data==item):
			return current
		else:
			return None

  # Delete and return Link from an unordered list or None if not found
	def delete_link (self, item):
		previous = self.first
		current = self.first

		if (current == None):
			return None

		while (current.data != item):
			if (current.next == None):
				return None
			else:
				previous = current
				current = current.next

		if (current == self.first):
			self.first = self.first.next
		else:
			previous.next = current.next
		return


  # String representation of data 10 items to a line, 2 spaces between data
	def __str__ (self):
		current=self.first
		count=0
		list_str=''
		while(current!=None):
			count=1
			while(count<11):
				if(current==None):
					break
				else:
					count+=1
					list_str+=str(current.data)+'  '
					current=current.next
			list_str+='\n'
		return list_str

  # Copy the contents of a list and return new list
	def copy_list (self):
		if (self.is_empty()):
			return None
		linked_list = LinkedList()
		cur = self.first
		while (cur != None):
			linked_list.insert_last(cur.data)
			cur = cur.next
		return linked_list

  # Reverse the contents of a list and return new list
	def reverse_list (self):
		if (self.is_empty()):
			return None
		linked_list = LinkedList()
		cur = self.first
		while (cur != None):
			linked_list.insert_first(cur.data)
			cur = cur.next
		return linked_list

  # Sort the contents of a list in ascending order and return new list
	def sort_list (self):
		if (self.is_empty()):
			return None
		linked_list = LinkedList()
		cur = self.first
		val_list = []
		while (cur != None):
			val_list.append(cur.data)
			cur = cur.next
		val_list.sort()
		for val in val_list:
			linked_list.insert_last(val)
		return linked_list

  # Return True if a list is sorted in ascending order or False otherwise
	def is_sorted (self):
		cur = self.first
		while(cur.next != None):
			if(cur.data >= cur.next.data):
				return False
			cur = cur.next
		return True

	# Return True if a list is empty or False otherwise
	def is_empty (self):
		if (self.first == None):
			return True
		else:
			return False

	# Merge two sorted lists and return new list in ascending order
	def merge_list (self, other):
		linked_list = LinkedList()
		self_sorted = self.sort_list()
		other_sorted = self.sort_list()
		cur_self = self_sorted.first
		cur_other = other_sorted.first
		while ((cur_self != None) and (cur_other != None)):
			if (cur_self.data < cur_other.data):
				linked_list.insert_last(cur_self.data)
				cur_self = cur_self.next
			else:
				linked_list.insert_last(cur_other.data)
				cur_other = cur_other.next
		while (cur_self != None):
			linked_list.insert_last(cur_self.data)
			cur_self = cur_self.next
		while (cur_other != None):
			linked_list.insert_last(cur_other.data)
			cur_other=cur_other.next
		return linked_list

	# Test if two lists are equal, item by item and return True
	def is_equal (self, other):
		if(self.first==None and other.first==None):
			return True
		elif(self.first==None or other.first==None):
			return False
		if (self.get_num_links() != other.get_num_links()):
			return False
		cur_self = self.first
		cur_other = self.first
		while (cur_self != None and cur_other != None):
			if (cur_self.data != cur_other.data):
				return False
			cur_self = cur_self.next
			cur_other = cur_other.next
		return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
	def remove_duplicates (self):
		if (self.is_empty()):
			return None
		linked_list = self.copy_list()
		data_list = []
		cur = (linked_list).first
		while (cur != None):
			data_list.append(cur.data)
			cur = cur.next
		data_list.sort()
		copy = []
		for i in range(len(data_list)):
			copy.append(data_list[i])
		cur = linked_list.first
		while (cur != None):
			if (data_list.count(cur.data)>1):
					linked_list.delete_link(cur.data)
					trash = data_list.pop(data_list.index(cur.data))
			cur = cur.next
		return linked_list

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  linked_list = LinkedList()
  items = [1,2,3,3,5,6,1,2,8,11,3]
  items2 = [1,2,3,4,5,6,7,8,9,10]
  for item in items:
    linked_list.insert_first(item)
  print("Insert_first: ", linked_list)

  # Test method insert_last()
  linked_list1 = LinkedList()
  for item in items:
    linked_list1.insert_last(item)
  print("insert_last: ",linked_list1)

  # Test method insert_in_order()
  linked_list1.insert_in_order(5)
  print("insert_inorder: ",linked_list1)

  # Test method get_num_links()
  print("num_links: ",linked_list1.get_num_links())

  # Test method find_unordered()
  # Consider two cases - item is there, item is not ther
  print("find_unordered: ",linked_list1.find_unordered(55))
  print("find_unordered: ",linked_list1.find_unordered(2))

  # Test method find_ordered()
  # Consider two cases - item is there, item is not there
  linked_list3 = LinkedList()
  for item in items2:
      linked_list3.insert_last(item)
  print("find_ordered: ",linked_list3.find_ordered(3))
  print("find_ordered: ",linked_list3.find_ordered(11))

  # Test method delete_link()
  # Consider two cases - item is there, item is not there
  linked_list1.delete_link(15)
  print("delete_link: ",linked_list1)
  linked_list1.delete_link(5)
  print("delete_link: ",linked_list1)

  # Test method copy_list()
  print("copy_list: ",linked_list1.copy_list())

  # Test method reverse_list()
  print("reverse_list: ",linked_list1.reverse_list())

  # Test method sort_list()
  print("sort_list: ",linked_list1.sort_list())

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("is_sorted: ",linked_list1.is_sorted())
  print("is_sorted: ",linked_list3.is_sorted())

  # Test method is_empty()
  print("is_empty: ",linked_list1.is_empty())

  # Test method merge_list()
  print("merge_list: ",linked_list1.merge_list(linked_list3))

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("is_equal: ",linked_list1.is_equal(linked_list1))
  print("is_equal: ",linked_list1.is_equal(linked_list3))

  # Test remove_duplicates()
  print("remove_duplicates: ",linked_list1.remove_duplicates())

if __name__ == "__main__":
		main()
