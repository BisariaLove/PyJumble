__author__ = 'jarvis'
class Node:
    def __init__(self, num):
        self.next = None
        self.data = num

class LList:
    def __init__(self, h=None):
        self.head = None

    def insert_node(self, num):
        node = Node(num)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print_list(self):
        node = self.head
        while not (node is None):
            print node.data
            node = node.next

lis = LList()
lis.insert_node(10)
lis.insert_node(20)
lis.insert_node(30)
lis.print_list()






