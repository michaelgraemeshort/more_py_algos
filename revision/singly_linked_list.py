# singly linked list class with common operations, loosely modelled on built-in list type
# Todo: tests, error handling


class Node:
    """Node for LinkedList class."""
    def __init__(self, value):
        self.value = value
        self.next = None

    # implementing the below to enable max and min functions

    def __lt__(self, other):
        return True if self.value < other.value else False

    # def __le__(self, other):
    #     return True if self.value <= other.value else False 

    # def __eq__(self, other):
    #     return True if self.value == other.value else False  

    # def __ne__(self, other):
    #     return True if self.value != other.value else False 

    def __gt__(self, other):
        return True if self.value > other.value else False 

    # def __ge__(self, other):
    #     return True if self.value >= other.value else False

    def __str__(self):
        return str(self.value)


class LinkedList:
    """Singly-linked list with tail."""
    def __init__(self, iterable=None):
        if not iterable:
            self.head, self.tail = None, None
            self.length = 0
            return 
        node = Node(iterable[0])
        self.head = node
        self.length = 1
        for i in iterable[1:]:
            node.next = Node(i)
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
        """Returns value in self."""
        for node in self:
            if node.value == value:
                return True 
        return False

    def __getitem__(self, index):
        """Return self[index]. Negative indices NOT supported."""
        if isinstance(index, int):
            if not self.head or index >= len(self):
                raise IndexError("index out of range")
            if index < 0:
                raise IndexError("cannot index LinkedList by negative number")
            node = self.head
            for i in range(index):
                node = node.next 
            return node.value
        if isinstance(index, slice):
            output = []
            start = 0 if not index.start else index.start
            stop = len(self) if not index.stop or index.stop >= len(self) else index.stop   # nasty
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
        raise TypeError(f"List indices must be integers or slices")

    def __delitem__(self, index):
        """Delete self[item]. Negative indices NOT supported."""
        if not self.head or index >= len(self):
            raise IndexError("index out of range")
        if index < 0:
            raise IndexError("cannot index LinkedList by negative number")
        if index == 0:
            self.popleft()
            return 
        if index == len(self) - 1:
            self.pop()
            return 
        previous_node = self.head 
        node = self.head.next
        for i in range(index - 1):
            previous_node = node
            node = node.next
        previous_node.next = node.next

    def __add__(self, other):
        """Returns self + other."""
        # to behave like built-in list, should not modify self, but rather return concatenated list
        result = LinkedList()
        result.extend(self)
        result.extend(other)
        return result
        # self.tail.next = other.head 
        # self.tail = other.tail
        # return self

    def __iadd__(self, other):
        """Return self += other."""
        return self.__add__(other)

    def __mul__(self, value):
        """Return self * value."""
        result = LinkedList()
        for i in range(value):
            result.extend(self)
        return result
        # if value == 0:
        #     return self.clear()
        # if value == 1:
        #     return self
        # copy_1 = self.copy()
        # for i in range(value - 1):
        #     copy_2 = copy_1.copy()
        #     self += copy_2
        # return self

    def __imul__(self, value):
        """Return self *= value."""
        return self.__mul__(value)

    def __str__(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
        return str(output)

    def append(self, value):
        """Append object to the right of the LinkedList."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1

    def appendleft(self, value):
        """Append object to the left of the LinkedList."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1

    def pop(self, index=None):
        """Remove and return item at index (default last)."""
        if not self.head:
            raise IndexError("pop from empty LinkedList")
        if len(self) == 1:
            node = self.head
            self.head = None 
            self.tail = None 
            return node.value 
        previous_node = self.head
        node = self.head.next
        if index == 0:
            return self.popleft()
        if index == len(self) - 1 or not index: 
            while node.next:
                previous_node = node
                node = node.next 
            self.tail = previous_node 
            self.tail.next = None
            self.length -= 1
            return node.value
        for i in range(index - 1):
            previous_node = node 
            node = node.next
        previous_node.next = node.next 
        return node.value      
            
    def popleft(self):
        """Remove and return first item."""
        if not self.head:
            raise IndexError("pop from empty LinkedList")
        if len(self) == 1:
            return self.pop()
        node = self.head 
        self.head = node.next 
        self.length -= 1
        return node.value

    def index(self, value):
        """Return first index of value."""
        index_ = 0
        node = self.head 
        while node:
            if node.value == value:
                return index_
            node = node.next 
            index_ += 1 
        raise ValueError(f"{value} is not in LinkedList")

    def insert(self, index, value):
        """Insert value before index."""
        if len(self) == 0 or index >= len(self):
            self.append(value)
            return 
        if index == 0:
            self.appendleft(value)
            return 
        new_node = Node(value)
        previous_node = self.head 
        node = self.head.next 
        for i in range(index - 1):
            previous_node = node 
            node = node.next 
        previous_node.next = new_node 
        new_node.next = node 
        self.length += 1

    def remove(self, value):
        """Remove first occurrence of value."""
        if not self.head:
            raise ValueError(f"{value} not in LinkedList")
        if len(self) == 1:
            self.pop()
            return 
        if self.head.value == value:
            self.head = self.head.next 
            self.length -= 1
            return 
        previous_node = self.head 
        node = self.head.next 
        while node:
            if node.value == value:
                if not node.next:
                    self.pop()
                    # previous_node.next = None     # remove this stuff if tests work out
                    # self.tail = previous_node
                    # self.length -= 1
                    # return 
                previous_node.next = node.next 
                self.length -= 1
                return 
            previous_node = node 
            node = node.next 
        raise ValueError(f"{value} not in LinkedList")

    def reverse(self):
        """Reverse LinkedList in place."""
        if len(self) in (0, 1):
            return self
        self._reverse(self.head, self.head.next)
        self.head, self.tail = self.tail, self.head
        self.tail.next = None 

    def _reverse(self, node, next_node):
        if next_node.next:
            self._reverse(node.next, next_node.next)
        next_node.next = node

    def clear(self):
        """Remove all items from LinkedList."""
        ll.head = None
        ll.tail = None

    def copy(self):
        """"Return a copy of the LinkedList."""
        copy_ = LinkedList()
        copy_.extend(self)
        # for node in self:
        #     copy_.append(node.value)
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
        """Return the sum of the LinkedList. Optional start value (default 0)."""
        output = 0
        node = self.head 
        for i in range(start):
            node = node.next
        while node:
            output += node.value
            node = node.next
        return output 

    def sort(self):
        # TODO: revise Merge Sort, apply to LinkedList
        pass
    
spam = LinkedList(range(5)) 
spam *= 2
print(spam)
print(spam.sum(5))