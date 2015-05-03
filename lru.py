 class QNode:
	def __init__(self, n):
		self.prev = None
		self.next = None
		self.pageNumber = n


class Queue:
	def __init__(self, num):
		self.count = 0
		self.numberOfFrames = num
		self.front = None
		self.rear = None


class LRUCache:
	def __init__(self, num):
		self.hashmap = dict()
		self.q = Queue(num)
	
	def areAllFramesFull(self):
		return self.q.count == self.q.numberOfFrames

	def isQueueEmpty(self):
		return self.q.rear == None

	def deQueue(self):
		if self.isQueueEmpty():
			return
		if self.q.front == self.q.rear:
			self.q.front = None
		temp = self.q.rear
		self.q.rear = self.q.rear.prev

		if self.q.rear is not None:
			self.q.rear.next = None

		self.q.count -= 1

	def enQueue(self, num):
		if self.areAllFramesFull():
			self.hashmap[self.q.rear.pageNumber] = None
			self.deQueue()

		temp = QNode(num)
		temp.next = self.q.front

		if self.isQueueEmpty():
			self.q.rear = self.q.front = temp
		else:
			self.q.front.prev = temp
			self.q.front = temp

		self.hashmap[num ] = temp
		self.q.count += 1

	def referencePage(self, num):
		reqPage = self.hashmap.get(num, None)

		if reqPage == None:
			self.enQueue(num)
		elif reqPage != self.q.front: 
			reqPage.prev.next = reqPage.next
			
			if reqPage.next != None:
				reqPage.next.prev = reqPage.prev

			if reqPage == self.q.rear:
				self.q.rear = reqPage.prev
				self.q.rear.next = None

			reqPage.next = self.q.front
			reqPage.prev = None

			reqPage.next.prev = reqPage
			self.q.front = reqPage
	def printQueue(self):
		temp = self.q.front
		while temp != None:
			print temp.pageNumber
			temp = temp.next

obj = LRUCache(4)
obj.referencePage(1)
obj.referencePage(2)
obj.referencePage(3)
obj.referencePage(1)
obj.referencePage(4)
obj.referencePage(5)
obj.printQueue()
