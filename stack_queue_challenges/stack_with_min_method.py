# linked list-based stack with min method
# each node should know the minimum value of the stack up to and including itself

class Node:
    def __init__(self, data, stack_minimum=None):
        self.data = data
        self.next = None
        self.stack_minimum = stack_minimum

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
        self.stack_minimum = None

    def __len__(self):
        return self.length

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

    def push(self, value):
        """Push value onto stack."""
        self.length += 1
        if not self.head:
            self.head = Node(value, value)
            self.stack_minimum = value
            return
        if value < self.stack_minimum:
            self.stack_minimum = value
            new_node = Node(value, value)
        else:
            new_node = Node(value, self.stack_minimum)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        """Remove and return the last item."""
        if not self.head:
            raise IndexError("pop from empty stack")
        self.length -= 1
        node = self.head
        # if one item list:
        if not node.next:
            self.head = None
            return node
        self.head = node.next
        node.next = None
        return node.data

    def min(self):
        """Return the minimum stack value."""
        return self.head.stack_minimum

    def peek(self):
        """Return the last item."""
        return self.head.data

    def clear(self):
        """Remove all items from stack."""
        self.head = None
