# doubly linked list class with common operations
# todo: extend support for negative indexing


class Node:
    """Node for LinkedList class."""

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Doubly-linked list with tail."""

    def __init__(self, iterable=None):
        self.head, self.tail = None, None
        self.length = 0
        if iterable:
            node = Node(iterable[0])
            self.head = node
            self.length = 1
            for i in iterable[1:]:
                node.next = Node(i)
                node.next.prev = node
                self.length += 1
                node = node.next
            self.tail = node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __len__(self):
        return self.length

    def __contains__(self, value):
        for node in self:
            if node.value == value:
                return True
        return False

    def __getitem__(self, index):
        """Returns self[index]."""
        if isinstance(index, int):
            if not -len(self) <= index < len(self):
                raise IndexError("index out of range")
            if index < 0:
                node = self.tail
                for i in range(-1, index, -1):
                    node = node.prev
                return node.value
            node = self.head
            for i in range(index):
                node = node.next
            return node.value
        if isinstance(index, slice):
            output = []
            start = 0 if not index.start else index.start
            if start >= len(self):
                return output
            stop = len(self) if not index.stop or index.stop > len(self) else index.stop
            step = 1 if not index.step else index.step
            node = self.head
            for i in range(start):
                node = node.next
            output.append(node.value)
            for i in range((stop - start - 1) // step):
                for j in range(step):
                    node = node.next
                output.append(node.value)
            return output
        raise TypeError("List indices must be integers or slices")

    def __delitem__(self, index):
        """Delete self[item]."""
        if not self.head or index >= len(self):
            raise IndexError("index out of range")
        if index < 0:
            raise IndexError("cannot index LinkedList by negative number")
        if index == 0:
            return self.popleft()
        if index == len(self) - 1:
            return self.pop()
        node = self.head
        for i in range(index):
            node = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1

    def __add__(self, other):
        """Returns self + other."""
        result = LinkedList()
        result.extend(self)
        result.extend(other)
        return result

    def __iadd__(self, other):
        """Return self += other."""
        return self + other

    def __mul__(self, value):
        """Return self * value."""
        result = LinkedList()
        for i in range(value):
            result.extend(self)
        return result

    def __imul__(self, value):
        """Return self *= value."""
        return self * value

    def __str__(self):
        return str([node.value for node in self])

    def append(self, value):
        """Append object to the right of the LinkedList."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def appendleft(self, value):
        """Append object to the left of the LinkedList."""
        if not self.head:
            return self.append(value)
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def pop(self, index=None):
        """Remove and return item at index (default last)."""
        if not self.head:
            raise IndexError("pop from empty LinkedList")
        if len(self) == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped.value
        if index is None:
            popped = self.tail
            self.tail = popped.prev
            self.length -= 1
            return popped.value
        if index >= len(self):
            raise IndexError("pop index out of range")
        if index == 0:
            return self.popleft()
        node = self.head
        for i in range(index - 1):
            node = node.next
        popped = node.next
        node.next = popped.next
        popped.next.prev = node
        self.length -= 1
        return popped.value

    def popleft(self):
        """Remove and return first item."""
        if not self.head:
            raise IndexError("pop from empty LinkedList")
        if len(self) == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length = 0
            return popped.value
        popped = self.head
        self.head = popped.next
        self.head.prev = None
        self.length -= 1
        return popped.value

    def index(self, value):
        """Return first index of value."""
        index_ = 0
        node = self.head
        while node:
            if node.value == value:
                return index_
            node = node.next
            index_ += 1
        raise ValueError(f"{value} is not in list")

    def insert(self, index, value):
        """Insert value before index."""
        if len(self) == 0 or index >= len(self):
            return self.append(value)
        if index == 0:
            return self.appendleft(value)
        node = self.head
        new_node = Node(value)
        for i in range(index - 1):
            node = node.next
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        new_node.prev = node
        self.length += 1

    def remove(self, value):
        """Remove first occurrence of value."""
        if not self.head:
            raise ValueError("LinkedList is empty")
        if self.head.value == value:
            self.popleft()
            return
        node = self.head.next
        while node:
            if node.value == value:
                if not node.next:
                    self.pop()
                    return
                node.prev.next = node.next
                node.next.prev = node.prev
                self.length -= 1
                return
            node = node.next
        raise ValueError(f"{value} not in LinkedList")

    def reverse(self):
        """Reverse LinkedList in place."""
        if not self.head or len(self) == 1:
            return self
        node = self.head
        while node:
            node.next, node.prev = node.prev, node.next
            node = node.prev
        self.head, self.tail = self.tail, self.head

    def clear(self):
        """Remove all items from LinkedList."""
        self.head = None
        self.tail = None

    def copy(self):
        """Return a copy of the LinkedList."""
        copy_ = LinkedList()
        for node in self:
            copy_.append(node.value)
        return copy_

    def count(self, value):
        """Return number of occurrences of value."""
        count_ = 0
        for node in self:
            if node.value == value:
                count_ += 1
        return count_

    def extend(self, iterable):
        """Extend LinkedList by appending elements from the iterable."""
        if isinstance(iterable, LinkedList):
            for i in iterable:
                self.append(i.value)
        else:
            for i in iterable:
                self.append(i)

    def sum(self, start=0):
        """Return the sum of the LinkedList. Optional start index (default 0)."""
        if not self.head:
            return 0
        sum_ = 0
        node = self.head
        for i in range(start):
            node = node.next
        while node:
            sum_ += node.value
            node = node.next
        return sum_

    def merge_sort(self):  # for my own twisted amusement
        """Sort in place."""
        if not self.head.next:
            return self
        left, right = self._halve()
        left.merge_sort()
        right.merge_sort()
        left._merge(right)

    def _merge(self, other):
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
                left_node.prev = node
                left_node = left_node.next
                node = node.next
            else:
                node.next = right_node
                right_node.prev = node
                right_node = right_node.next
                node = node.next
        if left_node:
            node.next = left_node
            left_node.prev = node
            return
        if right_node:
            node.next = right_node
            right_node.prev = node
            self.tail = other.tail

    def _halve(self):
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
        right.head.prev = None
        right.tail = self.tail
        self.tail = slow
        slow.next = None
        return self, right
