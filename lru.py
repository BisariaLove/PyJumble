__author__ = 'jarvis'

class QNode:
    def __init__(self, num):
        self.prev = None
        self.next = None
        self.pageNumber = num

class Queue:
    def __init__(self, num):
        self.count = 0
        self.front = None
        self.rear = None
        self.numberOfFrames = num

class Hash:
    def __init__(self, num):
        self.capacity = num
        self.array = dict()

class LRU:
    @staticmethod
    def are_all_frames_full(q):
        "returns a boolean value"
        return q.count == q.numberOfFrames

    @staticmethod
    def is_queue_empty(q):
        return q.rear == None

    def de_queue(self, q):
        if self.is_queue_empty(q):
            return

        if q.front == q.rear:
            q.front = None
        temp = q.rear
        q.rear = q.rear.prev

        if q.rear != None:
            q.rear.next = None

        q.count -= 1

    def enqueue(self, q, h, pnum):
        if self.are_all_frames_full(q):
            h.array[q.rear.pageNumber] = None
            self.de_queue(q)
            temp = QNode(pnum)
            temp.next = q.front

            if self.is_queue_empty(q):
                q.rear = q.front = temp
            else:
                q.front.prev = temp
                q.front = temp
            h.array[pnum] = temp
            q.count += 1

    def referencePage(self, q, h, pnum):
        reqPage = h.array.get(pnum, None)

        if reqPage == None:
            self.enqueue(q, h, pnum)
        elif reqPage != q.front:
            reqPage.prev.next = reqPage.next
            if reqPage.next != None:
                reqPage.next.prev = reqPage.prev

            if reqPage == q.rear:
                q.rear = q.front
                q.rear.next = None

            reqPage.next = q.front
            reqPage.prev = None
            reqPage.next.prev = reqPage
            q.front = reqPage

q = Queue(4)
h = Hash(10)
l = LRU()
l.referencePage(q, h, 1)
l.referencePage(q, h, 2)
l.referencePage(q, h, 3)
l.referencePage(q, h, 1)
l.referencePage(q, h, 4)
l.referencePage(q, h, 5)

"""print q.front.pageNumber
print q.front.next.pageNumber
print q.front.next.next.pageNumber
print q.front.next.next.next.pageNumber"""