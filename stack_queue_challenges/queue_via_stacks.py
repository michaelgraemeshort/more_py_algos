# implement a queue using two stacks

class QueueViaStacks:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def enqueue(self, item):
        self.stack_one.append(item)

    def dequeue(self):
        if not self.stack_one and not self.stack_two:
            raise IndexError("dequeue from empty queue")
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
        return self.stack_two.pop()

# proof of concept only