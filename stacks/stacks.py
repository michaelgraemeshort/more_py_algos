class Stack:
    def __init__(self, l=None):
        self.l = l
    
    def __str__(self):
        if not self.l:
            return "stack is empty"
        return "\n".join(reversed([str(i) for i in self.l]))

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


s = Stack([1, 2, 3])
s2 = Stack()

print(s)
print()
s.clear()
print(s)
