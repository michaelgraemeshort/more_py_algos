class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self, nodes=None):
        # pushes items onto stack in order given e.g. Stack([1, 2, 3]) pushes 1 first
        self.head = None
        if nodes:
            node = Node(nodes[-1])
            self.head = node
            for i in nodes[-2::-1]:
                node.next = Node(i)
                node = node.next

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length        

    def __str__(self):
        if not self.head:
            return "stack is empty"
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.data))
            node = node.next
        return "\n".join(nodes)

    def is_empty(self):
        """Return True if stack is empty. Otherwise, False."""
        return not self.head

    def push(self, item):
        """Push item onto stack."""
        new_node = Node(item)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):
        """Remove and return the last item."""
        if not self.head:
            raise IndexError("pop from empty stack")
        node = self.head
        # if one item list:
        if not node.next:
            self.head = None
            return node
        self.head = node.next
        node.next = None
        return node.data

    def peek(self):
        """Return the last item."""
        return self.head.data

    def clear(self):
        """Remove all items from stack."""
        self.head = None

