class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.tail = None
        if nodes:
            nodes = [Node(i) for i in nodes]
            self.head = nodes[0]
            self.tail = nodes[-1]
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            for i in range(len(nodes) - 1, 0, -1):
                nodes[i].previous = nodes[i - 1]

    def __getitem__(self, index):
        return self.get(index)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        length = 0
        if not self.head:
            return length
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def __str__(self):
        if not self.head:
            return "list is empty"
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def get(self, index):
        if not self.head:
            return "list is empty"
        if index >= 0:
            node = self.head
            for i in range(index):
                node = node.next
                if not node:
                    raise IndexError("list index out of range")
            return node
        node = self.tail
        for i in range(abs(index) - 1):
            node = node.previous
            if not node:
                raise IndexError("list index out of range")
        return node

    def add_first(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def add_last_node(self, n):
        if not self.head:
            self.head = n
            self.tail = n
            return
        n.previous = self.tail
        if self.tail:
            self.tail.next = n
        self.tail = n

    def add_after(self, target_node_data, new_data):
        new_node = Node(new_data)
        node = self.head
        while node and node.data != target_node_data:
            node = node.next
        if not node:
            raise Exception("target node not found. data not added")
        new_node.next = node.next
        if new_node.next:
            node.next.previous = new_node
        else:
            self.tail = new_node
        node.next = new_node
        new_node.previous = node

    def add_before(self, target_node_data, new_data):
        new_node = Node(new_data)
        node = self.head
        while node and node.data != target_node_data:
            node = node.next
        if not node:
            raise Exception("target node not found. data not added")
        new_node.next = node
        if node.previous:
            new_node.previous = node.previous
            node.previous.next = new_node
        else:
            self.head = new_node
        node.previous = new_node

    def remove_first(self):
        if not self.head:
            return "list is empty"
        node = self.head
        if not node.next:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            self.head.previous = None

    def remove_last(self):
        if not self.head:
            return "list is empty"
        node = self.tail
        if not node.previous:
            self.head = None
            self.tail = None
        else:
            self.tail = node.previous
            self.tail.next = None

    def remove_node(self, target_node_data):
        if not self.head:
            return "list is empty"
        node = self.head
        while node and target_node_data != node.data:
            node = node.next
        if not node:
            raise Exception("target not found")
        if not node.previous and not node.next: # if target node is only node
            self.head = None
            self.tail = None
            return
        if not node.previous:   # if target node is head node
            self.head = node.next
            self.head.previous = None
            return
        if not node.next:   # if target node is tail node
            self.tail = node.previous
            self.tail.next = None
            return
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

    def reverse_list(self):
        if not self.head:
            return "list is empty"
        self.head, self.tail = self.tail, self.head
        for node in self:
            node.next, node.previous = node.previous, node.next

    # challenge section

    def remove_duplicates(self):
        if not self.head:
            return "list is empty"
        nodes = []
        for node in self:
            if node.data in nodes:
                node.previous.next = node.next
            else:
                nodes.append(node.data)

    def nth_to_last(self, n):
        # pretend singly-linked
        assert type(n) == int and n > 0, "Positive integer n only"
        if not self.head:
            return "list is empty"
        pointer_1 = self.head
        pointer_2 = self.head
        for i in range(n - 1):
            pointer_2 = pointer_2.next
            if not pointer_2:
                raise IndexError("list index out of range")
        while pointer_2.next:
            pointer_2 = pointer_2.next
            pointer_1 = pointer_1.next
        return pointer_1

    def partition(self, value):
        # partition list around given node, in-place
        # pretend singly-linked
        # iterate through list. stop at tail
        # first pass: push node.data >= value to end of list
        # second pass: push node.data > value to end of list
        # probably missing a trick
        # worst code ever written? can't be bothered to DRY it up
        if not self.head:
            return "list is empty"
        if not self.head.next:
            return
        node = self.head
        previous = None
        tail = self.tail
        while node != self.tail:
            if node == self.head and node.data >= value:
                next_node = node.next
                self.head = next_node
                tail.next = node
                node.next = None
                tail = node
                node = next_node
            elif node != self.head and node.data >= value:
                next_node = node.next
                tail.next = node
                node.next = None
                tail = node
                previous.next = next_node
                node = next_node
            else:
                previous = node
                node = node.next
        if node == self.head and node.data >= value:
            next_node = node.next
            self.head = next_node
            tail.next = node
            node.next = None
            tail = node
            node = next_node
        elif node != self.head and node.data >= value:
            next_node = node.next
            tail.next = node
            node.next = None
            tail = node
            previous.next = next_node
            node = next_node
        self.tail = tail
        # 2nd pass
        node = self.head
        previous = None
        tail = self.tail
        while node != self.tail:
            if node == self.head and node.data > value:
                next_node = node.next
                self.head = next_node
                tail.next = node
                node.next = None
                tail = node
                node = next_node
            elif node != self.head and node.data > value:
                next_node = node.next
                tail.next = node
                node.next = None
                tail = node
                previous.next = next_node
                node = next_node
            else:
                previous = node
                node = node.next
        if node == self.head and node.data > value:
            next_node = node.next
            self.head = next_node
            tail.next = node
            node.next = None
            tail = node
            node = next_node
        elif node != self.head and node.data > value:
            next_node = node.next
            tail.next = node
            node.next = None
            tail = node
            previous.next = next_node
            node = next_node
        self.tail = tail

        # this is not how it's done, surprisingly
        # concatenate three lists: < value, == value, > value


def sum_lists(ll_1, ll_2):
    # given two numbers, each in the form of a backwards linked list (e.g. 2 -> 1 -> 3 for 312)
    # return their sum, also as a backwards linked list
    # ideas: first number is the ones, second the tens, etc (10^0, 10^1, 10^2, ...)
    # sum the ones, then the tens, etc, carrying one over each time if necessary

    if not ll_1.head:
        return ll_2
    if not ll_2.head:
        return ll_1
    node_1 = ll_1.head
    node_2 = ll_2.head
    result = []
    carry = 0
    while node_1 or node_2:
        s = 0
        if node_1:
            s += node_1.data
            node_1 = node_1.next
        if node_2:
            s += node_2.data
            node_2 = node_2.next
        s += carry
        carry, remainder = divmod(s, 10)
        result.append(remainder)
    return DoublyLinkedList(result)


def intersect(ll_1, ll_2):
    # see https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/
    node_1 = ll_1.head
    node_2 = ll_2.head
    difference_in_length = len(ll_1) - len(ll_2)
    if difference_in_length > 0:
        for i in range(difference_in_length):
            node_1 = node_1.next
    elif difference_in_length < 0:
        for i in range(abs(difference_in_length)):
            node_2 = node_2.next
    while node_1:
        if node_1 is node_2:
            return node_1
        node_1 = node_1.next
        node_2 = node_2.next
    return False




# wrote this a little while ago. summary:
# initialise DLL with an iterable
# supports iteration, len(), square brackets (for ONE item)
# can add a node at the beginning, the end, or before or after a target node (target node data required)
# can remove a node at the beginning or end, or wherever else (target node data required)

# dll = DoublyLinkedList((1, 1, 2, 2, 3, 4, 4, 5, 5))

# CHALLENGES

