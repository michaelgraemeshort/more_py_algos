# - Implement stack and queue classes:
#     - Python list-based:
#         - with size limit
#         - without size limit
#     - Linked list-based:
#         - with size limit
#         - without size limit
# - Implement a circular queue class using a Python list

# common stack operations: push, pop, peek, is_empty
# common queue operations: queue, enqueue, front, rear

# optional maxsize for each of the below

from collections import deque


class ListStack:
    def __init__(self, maxsize=None):
        self.stack = []
        self.size = 0
        self.maxsize = float("inf") if not maxsize else maxsize

    def push(self, value):
        if self.size < self.maxsize:
            self.stack.append(value)
            self.size += 1
        else:
            raise IndexError(f"ListStack size limit ({self.maxsize}) reached.")

    def pop(self):
        if self.stack:
            self.size -= 1
            return self.stack.pop()
        else:
            raise IndexError("pop from empty ListStack.")

    def peek(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print("Stack is empty.")

    def is_empty(self):
        if not self.stack:
            return True
        return False


class ListQueue:  # more like DequeQueue
    def __init__(self, maxsize=None):
        self.queue = deque()
        self.size = 0
        self.maxsize = float("inf") if not maxsize else maxsize

    def enqueue(self, value):
        if self.size < self.maxsize:
            self.queue.append(value)
            self.size += 1
        else:
            raise IndexError(f"ListQueue size limit ({self.maxsize}) reached.")

    def dequeue(self):
        if self.queue:
            self.size -= 1
            return self.queue.popleft()
        else:
            raise IndexError("dequeue from empty ListQueue.")

    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print("Queue is empty.")

    def rear(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print("Queue is empty.")


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:  # inherit stack and queue classes from here
    def __init__(self, maxsize=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.maxsize = float("inf") if not maxsize else maxsize

    def __len__(self):
        return self.size

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        if self.size < self.maxsize:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
        else:
            raise IndexError(f"{self.__class__} size limit ({self.maxsize}) reached.")

    def pop(self):
        if not self.head:
            raise IndexError(f"pop from empty {self.__class__}.")
        popped = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            popped.prev.next = None
            self.tail = popped.prev
        self.size -= 1
        return popped.value


class LinkedListStack(LinkedList):
    def push(self, value):
        self.append(value)

    def peek(self):
        if self.tail:
            print(self.tail.value)
        else:
            print("Stack is empty.")

    def is_empty(self):
        if not self.head:
            return True
        return False


class LinkedListQueue(LinkedList):
    def enqueue(self, value):
        self.append(value)

    def dequeue(self):
        if not self.head:
            raise IndexError("Dequeue from empty LinkedListQueue.")
        front = self.head
        self.head = front.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return front.value

    def front(self):
        if not self.head:
            print("Queue is empty.")
        else:
            print(self.head.value)

    def rear(self):
        if not self.head:
            print("Queue is empty.")
        else:
            print(self.tail.value)


class CircularQueue:
    pass  # can't be bothered
