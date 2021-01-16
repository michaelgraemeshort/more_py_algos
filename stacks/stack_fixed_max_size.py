class Stack:
    def __init__(self, max_size, l=None):
        self.max_size = max_size
        self.l = l

    def __str__(self):
        if not self.l:
            return "stack is empty"
        return "\n".join(reversed([str(i) for i in self.l]))

    def is_full(self):
        if not self.l:
            return "stack is empty"
        return len(self.l) == self.max_size

    def is_empty(self):
        return not bool(self.l)

    def push(self, item):
        self.l.append(item)

    def pop(self):
        if self.is_empty:
            raise IndexError("pop from empty stack")
        return self.l.pop()

    def peek(self):
        if self.is_empty:
            raise IndexError("stack is empty")
        return self.l[-1]

    def clear(self):
        self.l.clear()


s = Stack(2, [1, 2])
s2 = Stack(2)

print(s.is_empty())
print(s2.is_empty())