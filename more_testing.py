# merge sort revision/modification to suit singly linked list
# break it down into single elements
# merge them, taking advantage of the fact that sorted lists can be merged efficiently


def merge_sort(l):
    def merge(left, right):
        merged = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1
        if left_index < len(left):
            merged.extend(left[left_index:])
            return merged
        merged.extend(right[right_index:])
        return merged


# now do the same for a skeleton singly linked list class


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.head = Node(iterable[0])
            node = self.head
            for i in iterable[1:]:
                node.next = Node(i)
                node = node.next
            self.tail = node

    def __str__(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
        return str(output)

    def append(self, node):  # takes a NODE, not a value
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def _merge(self, other):  # merge sort related, see below
        left_node = self.head
        right_node = other.head
        # change head if necessary
        if right_node.value < left_node.value:
            self.head = right_node
            right_node = right_node.next
        else:
            left_node = left_node.next
        # change pointers of remaining nodes
        node = self.head
        while left_node and right_node:
            if left_node.value < right_node.value:
                node.next = left_node
                left_node = left_node.next
                node = node.next
            else:
                node.next = right_node
                right_node = right_node.next
                node = node.next
        if left_node:
            node.next = left_node
            return
        if right_node:
            node.next = right_node
            self.tail = other.tail

    def _halve(self):  # also merge sort related
        # get middle node
        slow, fast = self.head, self.head.next
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast:
                break
        # partition
        right = LinkedList()
        right.head = slow.next
        right.tail = self.tail
        self.tail = slow
        slow.next = None
        return self, right

    def merge_sort(self):
        if not self.head.next:
            return self
        left, right = self._halve()
        left.merge_sort()
        right.merge_sort()
        left._merge(right)


from random import randint

ll = LinkedList()
for i in range(10):
    ll.append(Node(randint(-9, 9)))
print(ll)
ll.merge_sort()
print(ll)
