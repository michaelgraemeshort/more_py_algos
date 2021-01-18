# go to circular_queue_2.py

class Queue:
    """Circular queue, implemented using a Python list."""

    def __init__(self, max_size, q=None):   # q: list
        self.max_size = max_size
        self.q = [None for i in range(max_size)]
        self.head = 0
        self.tail = 0
        if q:
            if len(q) > self.max_size:
                raise ValueError("maximum queue size exceeded")
            self.q = q
            self.tail = len(q) - 1
            self.q = q + [None for i in range(max_size - len(q))]

    def __str__(self):
        if self.is_empty():
            return "queue is empty"
        return str(self.q)

    def is_empty(self):
        return set(self.q) == {None}

    def is_full(self):
        return None not in self.q

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("queue is full")
        if self.tail == len(self.q) - 1:
            self.tail = 0
            self.q[0] = item
        else:
            self.q[self.tail + 1] = item
            self.tail += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        item = self.q[self.head]
        self.q[self.head] = None
        if self.head == len(self.q) - 1:
            self.head = 0
        else:
            self.head += 1
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

