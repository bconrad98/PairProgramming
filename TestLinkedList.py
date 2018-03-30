#  File: TestLinkedList.py

#  Description:

#  Student Name: Matthew Frangos

#  Student UT EID: msf955

#  Partner Name: Braeden Conrad

#  Partner UT EID: bsc875

#  Course Name: CS 313E

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
		if(current==None):
			self.first=new_link
			return
		while(new_link.data>current.data):
			current=current.next
		new_link.next = current

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
		if(current.data==item):
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


  # String representation of data 10 items to a line, 2 spaces between data
	def __str__ (self):
		current=self.first
		count=0
		list_str=''
		while(current!=None):
			count=1
			while(count<10):
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
      if (self.is_empty):
          return None
      linked_list = LinkedList()
      cur = self.first
      while (cur != None):
          linked_list.insert_last(cur.data)
          cur = cur.next
      return linked_list

  # Reverse the contents of a list and return new list
  def reverse_list (self):
      if (self.is_empty):
          return None
      linked_list = LinkedList()
      cur = self.first
      while (cur != None):
          linked_list.insert_first(cur.data)
          cur = cur.next
      return linked_list

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self):
      if (self.is_empty):
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
      return self.is_equal(self.sort_list())

  # Return True if a list is empty or False otherwise
  def is_empty (self):
      if (self.first == None):
          return True
      else:
          return False

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other):
      linked_list = LinkedList()


  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
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
      cur = linked_list.first
      while (cur != None):
          data_list.append(cur.data)
          cur = cur.next
      data_list.sort()
      for i in range (len(data_list)-1):
          if (data_list[i] == data_list[i+1)]):
               trash = data_list.pop(i)
      cur = linked_list.first
      while (cur != None):
          if (cur.data in data_list):
              linked_list.remove_link(cur.data)
          cur = cur.next
      return linked_list

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered()
  # Consider two cases - item is there, item is not there

  # Test method find_ordered()
  # Consider two cases - item is there, item is not there

  # Test method delete_link()
  # Consider two cases - item is there, item is not there

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()

if __name__ == "__main__":
  main()
