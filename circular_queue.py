# work in progress

class Queue:
    """Circular queue, implemented using a Python list."""
    def __init__(self, max_size, q=None):   # q: list
        self.max_size = max_size
        self.q = []
        self.head = None
        self.tail = None
        if q:
            self.q = q
            self.head = self.q[0]
            self.tail = self.q[-1]

    def __str__(self):
        if self.q == []:
            return "queue is empty"
        return str(self.q)

    def is_empty(self):
        return not bool(self.head)

    def is_full(self):
        return len(self.q) == self.max_size

    def enqueue(self, item):
        if self.is_full:
            raise IndexError("queue is full")
        self.q.append(item)
        self.tail = self.q[-1]

    def dequeue(self):
        pass

    def front(self):
        pass

    def rear(self):
        pass

    def clear(self):
        pass