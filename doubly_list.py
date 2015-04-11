__author__ = 'jarvis'

class Node:
    def __init__(self, num):
        self.data = num
        self.next = self
        self.prev = self

class DList:
    def __init__(self, num):
        self.numOfFrames = num
        self.head = None
        self.count = 0

    def insert_node(self, num):
        node = Node(num)

        if self.head is None:
            self.head = node

        else:
            node.prev = self.head.prev
            node.next = self.head
            self.head.prev.next = node
            self.head.prev = node

    def print_list(self):
        node = self.head.next
        print self.head.data
        while not (node is self.head):
            print node.data
            node = node.next


dlist = DList(10)
dlist.insert_node(10)
dlist.insert_node(20)
dlist.insert_node(30)
dlist.insert_node(40)
dlist.insert_node(50)
dlist.print_list()



