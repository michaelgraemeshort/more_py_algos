# describe how you could use a single Python list to implement three stacks
# by dividing the stack into three, then writing a lot of irritating logic

class ThreeStacksInOneList:
    def __init__(self, max_size):
        # assume multiple of 3
        self.max_size = max_size
        self.l = [None for i in range(max_size)]
        self.max_stack_size = max_size // 3
        self.stack_1_size = 0
        self.stack_1_top = 0
        self.stack_2_size = 0
        self.stack_2_top = self.max_stack_size
        self.stack_3_size = 0
        self.stack_3_top = self.max_stack_size * 2
        self.top_d = {1: self.stack_1_top,
                      2: self.stack_2_top,
                      3: self.stack_3_top}
        self.size_d = {1: self.stack_1_size,
                       2: self.stack_2_size,
                       3: self.stack_3_size}

    def __str__(self):
        x = 0
        result = []
        for i in range(3):
            result.append(str(self.l[x:x + self.max_stack_size]))
            x += self.max_stack_size
        result = " | ".join(result)
        return result

    def is_empty(self, stack: int):
        return self.size_d[stack] == 0

    def is_full(self, stack):
        return self.size_d[stack] == self.max_stack_size

    def push(self, stack, item):
        if self.is_full(stack):
            raise ValueError(f"Stack {stack} is full")
        self.l[self.top_d[stack]] = item
        self.top_d[stack] += 1
        self.size_d[stack] += 1

    def pop(self, stack):
        if self.is_empty(stack):
            raise ValueError(f"Stack {stack} is empty")
        item = self.l[self.top_d[stack] - 1]
        self.l[self.top_d[stack] - 1] = None
        self.top_d[stack] -= 1
        self.size_d[stack] -= 1
        return item

    def peek(self, stack):
        return self.l[self.top_d[stack]]

    def clear(self, stack):
        self.l.clear()
