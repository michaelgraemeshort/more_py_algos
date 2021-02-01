# create MultiStack data structure that creates a new stack if the current one reaches capacity
# push and pop should behave as though there were just a single stack
# follow-up: implement a function which can pop from a specific stack

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.stack_size = 1

    def __str__(self):
        return str(self.value)


class MultiStack:
    def __init__(self, max_size):
        self.head = None
        self.max_size = max_size
        self.stack_list = []

    def __str__(self):
        # top of each stack to the right
        if not self.stack_list:
            return "stack is empty"
        result = []
        for i in self.stack_list:
            nodes = []
            node = i
            while node:
                nodes.append(str(node.value))
                node = node.next
            nodes.reverse()
            result.append(" ".join(nodes))
        return "\n".join(result)

    def push(self, value):
        new_node = Node(value)
        if not self.stack_list:
            self.stack_list.append(new_node)
            return
        top = self.stack_list[-1]
        if top.stack_size < self.max_size:
            new_node.next = top
            new_node.stack_size += top.stack_size
            self.stack_list[-1] = new_node
        else:
            self.stack_list.append(new_node)

    def pop(self, stack_number=None):
        if not self.stack_list:
            raise IndexError("pop from empty stack")
        if stack_number == None:
            stack_number = -1
        top = self.stack_list[stack_number]
        if top.next:
            self.stack_list[stack_number] = top.next
            top.next = None
            return top
        else:
            top.next = None
            return self.stack_list.pop(stack_number)

    def peek(self, stack_number=None):
        if not self.stack_list:
            return "stack is empty"
        if stack_number == None:
            stack_number = -1
        return self.stack_list[stack_number].value

    def clear(self):
        self.stack_list.clear()
        

# could just use a list of lists
# do that later