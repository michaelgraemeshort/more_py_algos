# add self.size attribute, use it to simplify self.is_empty and self.is_full methods for ?better performance

class Queue:
    """Circular queue, implemented using a Python list."""

    def __init__(self, max_size, q=None):   # q: list. leftmost item enqueued first
        self.max_size = max_size
        self.size = 0
        self.q = [None for i in range(max_size)]
        self.head = 0
        self.tail = 0
        if q:
            if len(q) > self.max_size:
                raise ValueError("maximum queue size exceeded")
            for i in q:
                self.enqueue(i)

    def __str__(self):
        if self.is_empty():
            return "queue is empty"
        return str(self.q)

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("queue is full")
        elif self.tail == len(self.q) - 1:
            self.q[self.tail] = item
            self.tail = 0
        else:
            self.q[self.tail] = item
            self.tail += 1
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.q[self.head]
        self.q[self.head] = None
        if self.head == len(self.q) - 1:
            self.head = 0
        else:
            self.head += 1
        self.size -= 1
        return item

    def front(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.q[self.head]

    def rear(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.q[self.tail]

    def clear(self):
        self.q.clear()
