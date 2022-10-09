class Queue(object):
    class Node(object):
        def __init__(self, item, prev, next):
            self.item = item
            self.prev = prev
            self.next = next
        pass
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        pass
    def enqueue(self, item):
        node = self.Node(item, None, None)
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node
        if self.tail == None:
            self.tail = node
        pass
    def dequeue(self):
        res = self.tail.item
        if self.tail.prev != None:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        if self.tail == None:
            self.head = None
        return res
    def front(self):
        return self.head.item
    def back(self):
        return self.tail.item
    def empty(self):
        return self.tail == None
        pass
    def test(self):
        q = Queue()
        print(q.empty())
        q.enqueue(1)
        print(q.empty())
        q.enqueue(2)
        print(q.empty())
        q.enqueue(3)
        print(q.empty())
        print(q.front())
        print(q.back())
        print(q.dequeue())
        print(q.empty())
        print(q.dequeue())
        print(q.empty())
        print(q.dequeue())
        print(q.empty())
