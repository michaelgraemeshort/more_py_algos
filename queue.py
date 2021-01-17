# just use collections.deque

class Queue:
    def __init__(self, q=None): # q: list
        self.q = []
        if q:
            self.q = q

    # def __str__(self):
    #     if self.is_empty:     <-- BROKEN why??    <-- MISSING PARENS!!
    #         return "queue is empty"
    #     return str(self.q)

    def __str__(self):
        if self.q == []:
            return "queue is empty"
        return str(self.q)

    def is_empty(self):
        return not bool(self.q)

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        # inefficient (all subsequent list items have to be moved)
        if self.is_empty:
            raise IndexError("dequeue from empty queue")
        return self.q.pop(0)

    def front(self):
        if self.is_empty:
            raise IndexError("queue is empty")
        return self.q[0]

    def rear(self):
        if self.is_empty:
            raise IndexError("queue is empty")
        return self.q[-1]

    def clear(self):
        self.q.clear()
