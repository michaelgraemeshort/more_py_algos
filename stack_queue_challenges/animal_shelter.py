# animal shelter

# create data structure that returns the cat/dog/non-specific animal that has been in the shelter for the longest

class Node:
    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.next = None

    def __str__(self):
        return f"{self.species}, {self.name}"


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if not self.head:
            return "queue is empty"
        nodes = []
        node = self.head
        while node:
            nodes.append(f"{node.species}, {node.name}")
            node = node.next
        return "\n".join(nodes)

    def enqueue(self, species, name):
        new_node = Node(species, name)
        if not self.head:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self, species=None):
        if not self.head:
            raise IndexError("queue is empty")
        node = self.head
        if species == None or species == node.species:
            self.head = node.next
            node.next = None
            return node
        while node and species != node.species:
            previous = node
            node = node.next
            if not node:
                raise ValueError(f"{species} not in queue")
        previous.next = node.next
        node.next = None
        return node
