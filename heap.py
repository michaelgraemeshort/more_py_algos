# a heap is a kind of complete binary tree
# two flavours: min and max heap
# min heap: value of parent node is less than or equal to values of child nodes
# max heap: the opposite
# represent as binary tree or array
# latter easier?
# in real life: use the heapq module

class MinHeap:
    def __init__(self, max_size):
        self.l = [None] * max_size
        self.max_size = max_size
        self.size = 0

    def min(self):
        return self.l[0]

    def level_order(self):
        for i in self.l:
            print(i)

    def insert(self, value):
        # add value to end of tree
        # if it violates the min heap property, swap it and its parent until the property is restored
        # sod recursion
        if self.size == self.max_size:
            raise IndexError("heap is full")
        self.l[self.size] = value
        if self.size != 0:
            index_of_value = self.size
            index_of_parent = (index_of_value - 1) // 2
            parent = self.l[index_of_parent]
            while parent and parent > value:
                self.l[index_of_parent] = self.l[index_of_value]
                self.l[index_of_value] = parent
                index_of_value = index_of_parent
                index_of_parent = (index_of_value - 1) // 2
                parent = self.l[index_of_parent]
        self.size += 1

    def remove(self, value):
        pass


heap = MinHeap(5)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(2)
heap.insert(1)
heap.insert(0)
heap.level_order()
    