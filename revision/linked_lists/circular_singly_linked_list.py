# creation, insertion, traversal, search, delete, clear
# manual testing only


class Node:
    """Node for circular singly linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CircularLinkedList:
    """Circular singly linked list."""

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.head = Node(iterable[0])
            node = self.head
            for i in iterable[1:]:
                node.next = Node(i)
                node = node.next
            self.tail = node  # helpful to have two pointers for other methods
            node.next = self.head

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
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
            if node == self.head:
                break
        return str(output)

    def insert(self, index, value):
        """Insert value before index."""
        new_node = Node(value)
        node = self.head
        prev_node = self.tail
        if not node:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return
        for i in range(index):
            prev_node = node
            node = node.next
        prev_node.next = new_node
        new_node.next = node
        if index == 0:
            self.head = new_node
            return
        if prev_node == self.tail:
            self.tail = new_node

    def remove(self, value):
        if not self.head:
            raise ValueError("CircularLinkedList is empty.")
        node = self.head
        prev_node = self.tail
        while True:
            if node.value == value:
                prev_node.next = node.next
                if node == self.head:
                    self.head = node.next
                elif node == self.tail:
                    self.tail = prev_node
                return
            prev_node = node
            node = node.next
            if node == self.head:
                raise ValueError("CircularLinkedList is empty.")

    def clear(self):
        self.head = None
        self.tail = None
