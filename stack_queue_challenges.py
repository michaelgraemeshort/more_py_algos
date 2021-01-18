# describe how you could use a single Python list to implement three stacks
# by dividing the stack into three, then writing a lot of irritating logic
# that I am about to write

class ThreeStacksInOneList:
    # whyyy
    def __init__(self, max_size):
        # start simple. assume multiple of 3
        self.max_size = max_size
        self.l = [None for i in range(max_size)]
        self.max_substack_size = max_size // 3
        self.substack_1_size = 0
        self.substack_2_size = 0
        self.substack_3_size = 0

    def __str__(self):
        x = 0
        result = []
        for i in range(3):
            result.append(str(self.l[x:x + self.max_substack_size]))
            x += self.max_substack_size
        result = " | ".join(result)
        return result

    def is_empty(self, substack):
        pass

    def is_full(self, substack):
        pass

    def push(self, stack, item):
        pass

    def pop(self, stack):
        pass

    def peek(self, stack):
        pass

    def clear(self, stack):
        pass


wtf = ThreeStacksInOneList(9)
print(wtf)

