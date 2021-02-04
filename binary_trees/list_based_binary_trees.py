class BinaryTree:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.l = [None for i in range(max_size + 1)]
        self.insert_at = 1

    def __contains__(self, value):
        return self.contains(value)

    def level_order(self):
        for i in self.l[1:]:
            print(i)

    def pre_order(self, node_index=1):
        # NLR
        # if node_index goes out of range, do nothing
        # print node
        # call pre_order on node.left
        # left child is self.l[index of node * 2]
        # call pre_order on node.right
        # which is self.l[index of node * 2 + 1]
        if node_index > self.max_size:
            return
        print(self.l[node_index])
        self.pre_order(node_index * 2)
        self.pre_order(node_index * 2 + 1)

    def in_order(self, node_index=1):
        # LNR
        if node_index > self.max_size:
            return
        self.in_order(node_index * 2)
        print(self.l[node_index])
        self.in_order(node_index * 2 + 1)

    def post_order(self, node_index=1):
        # LRN
        if node_index > self.max_size:
            return
        self.post_order(node_index * 2)
        self.post_order(node_index * 2 + 1)
        print(self.l[node_index])

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def insert(self, value):
        if self.is_full():
            raise IndexError("tree is full")
        self.l[self.insert_at] = value
        self.size += 1
        self.insert_at += 1

    def contains(self, value):
        # or just use in operator
        if self.is_empty():
            return False
        for i in self.l:
            if i == value:
                return True
        return False

    def remove(self, value):
        # removes first occurrence of value
        # somewhat unnecessary error handling
        try:
            i = self.l.index(value)
        except ValueError:
            raise ValueError(f"{value} is not in tree")
        self.l[i] = None

    def clear(self):
        self.l = [None for i in range(self.max_size + 1)]
