# linked list revision/create circular linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

ll = LinkedList()
ll.head = a

print(ll)
