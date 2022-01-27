# creation, insertion, traversal, search, delete, clear


class Node:
    """Node for circular doubly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class CircularLinkedList:
    """Circular doubly linked list."""

    def __init__(self, iterable=None):
        self.head = None  # no tail, this time
        if iterable:
            node = Node(iterable[0])
            self.head = node
            for i in iterable[1:]:
                new_node = Node(i)
                node.next = new_node
                new_node.prev = node
                node = new_node
            node.next = self.head
            self.head.prev = node

    def __contains__(self, value):
        if not self.head:
            return False
        node = self.head
        while True:
            if node.value == value:
                return True
            node = node.next
            if node == self.head:
                return False

    def __str__(self):
        return str(self.traverse())

    def traverse(self, reverse=False):
        """Returns a list representation of the CircularLinkedList."""
        output = []
        node = self.head
        if reverse:
            while True:
                output.append(node.value)
                node = node.prev
                if node == self.head:
                    break
        else:
            while True:
                output.append(node.value)
                node = node.next
                if node == self.head:
                    break
        return output

    def insert(self, index, value):
        """Insert value before index."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        node = self.head
        for i in range(index):
            node = node.next
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
        if node == self.head:
            self.head = new_node

    def remove(self, value):
        """Remove first occurrence of value."""
        if not self.head:
            raise ValueError("CircularLinkedList is empty.")
        node = self.head
        while True:
            if node.value == value:
                # one item list
                if node.next == node:
                    return self.clear()
                # otherwise
                node.prev.next = node.next
                node.next.prev = node.prev
                if node == self.head:
                    self.head = node.next
                return
            node = node.next
            if node == self.head:
                break
        raise ValueError("CircularLinkedList is empty.")

    def clear(self):
        """Remove all items from CircularLinkedList."""
        self.head = None
        self.tail = None
