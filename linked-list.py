class Node(object):

	def __init__(self , data):
		self.data = data
		self.nextNode = None

class linkedList(object):
	
	def __init__(self , head=None):
		self.head = head

	def insert(self , node):
		
		if not self.head:
			self.head = node

		else:
			#set new nodes pointer to old head
			node.nextNode = self.head
			#reset head to new node
			self.head = node

	def search(self , lList , Node):
		if self.head == Node:
			return self.head

		else:
			if lList.head.nextNode:
				self.search(linkedlist(lList.head.nextNode) , Node)
			else:
				raise ValueError("Node not in Linked List")

	def size(self):
		current = self.head
		size = 0

		while current is not None:
			size += 1
			current = current.nextNode
		return size

	def delete(self , node):
		if self.size() == 0:
			raise ValueError("List is Empty")
		else:
			current  = self.head
			previous = None
			found = False
			while not found:
				if current == node:
					found = True
				elif current is None:
					raise ValueError("Node not in Lnked List")
				else:
					previous = current
					current = current.nextNode
			if previous is None:
				self.head = current.nextNode
			else:
				previous.nextNode = current.nextNode