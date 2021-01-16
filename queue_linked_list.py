class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, nodes=None): # nodes: list
        self.head = None
        self.tail = None
        if nodes:
            node = Node(nodes[0])
            self.head = node
            for i in nodes[1:]:
                node.next = Node(i)
                node = node.next
            self.tail = node

    def __str__(self):
        if not self.head:
            return "queue is empty"
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.data))
            node = node.next
        return " <- ".join(nodes)

    def is_empty(self):
        return not bool(self.head)

    def enqueue(self, item):
        self.tail.next = Node(item)
        self.tail = self.tail.next

    def dequeue(self):
        if not self.head:
            raise IndexError("dequeue from empty queue")
        node = self.head
        self.head = node.next
        node.next = None
        return node.data

    def front(self):
        return self.head.data

    def rear(self):
        return self.tail.data

    def clear(self):
        self.head = None
        self.tail = None
