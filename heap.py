# a heap is a kind of complete binary tree
# two flavours: min and max heap
# min heap: value of parent node is less than or equal to values of child nodes
# max heap: the opposite
# represent as binary tree or array
# latter easier?
# in real life: use the heapq module
# https://www.geeksforgeeks.org/binary-heap/#:~:text=A%20Binary%20Heap%20is%20a,be%20stored%20in%20an%20array.

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
        # when testing: level order may not necessarily be in ascending order
        # as the value of a node's left child is permitted to be more than the right
        if self.size == self.max_size:
            raise IndexError("heap is full")
        self.l[self.size] = value
        if self.size != 0:
            index_of_value = self.size
            index_of_parent = (index_of_value - 1) // 2
            parent = self.l[index_of_parent]
            while parent != None and parent >= 0 and parent > value:
                self.l[index_of_parent] = self.l[index_of_value]
                self.l[index_of_value] = parent
                index_of_value = index_of_parent
                index_of_parent = (index_of_value - 1) // 2
                parent = self.l[index_of_parent]
        self.size += 1

    def remove(self):
        # replace node to be removed with the last node
        # usually the root node. just do that for starters
        # delete last node
        # if necessary, swap newly repositioned node up or down to make the heap valid
        root = self.l[0]
        if root is None:
            raise IndexError("heap is empty")
        # get the last node
        last_node = self.l[self.size - 1]
        # replace the root with it
        self.l[0] = last_node
        # delete the last node
        self.l[self.size - 1] = None
        # swap the new root down to where it belongs
        # if there are two children and the heap is invalid, swap the smaller one upwards, obviously
        # this won't create a height imbalance because swapping, not adding
        # refactor this, it's despicable
        index = 0
        node = self.l[index]
        try:
            left_child = self.l[2 * index + 1]
        except IndexError:
            left_child = None
        try:
            right_child = self.l[2 * index + 2]
        except IndexError:
            right_child = None
        while left_child is not None or right_child is not None:
            if left_child is not None and right_child is not None:
                smaller_child = min(left_child, right_child)
                if node > smaller_child:
                    # swap
                    self.l[0] = smaller_child
                    if smaller_child == self.l[2 * index + 1]:
                        self.l[2 * index + 1] = node
                        index = self.l[2 * index + 1]
                    else:
                        self.l[2 * index + 2] = node
                        index = self.l[2 * index + 2]
                    try:
                        left_child = self.l[2 * index + 1]
                    except IndexError:
                        left_child = None
                    try:
                        right_child = self.l[2 * index + 2]
                    except IndexError:
                        right_child = None
                else:
                    break
            elif left_child is not None:
                if node > left_child:
                    # swap
                    self.l[0] = left_child
                    self.l[2 * index + 1] = node
                    index = self.l[2 * index + 1]
                    try:
                        left_child = self.l[2 * index + 1]
                    except IndexError:
                        left_child = None
                    try:
                        right_child = self.l[2 * index + 2]
                    except IndexError:
                        right_child = None
                else:
                    break
            else:
                if node > right_child:
                    self.l[0] = right_child
                    self.l[2 * index + 2] = node
                    index = self.l[2 * index + 2]
                    try:
                        left_child = self.l[2 * index + 1]
                    except IndexError:
                        left_child = None
                    try:
                        right_child = self.l[2 * index + 2]
                    except IndexError:
                        right_child = None
                else:
                    break
        self.size -= 1
        return root

    # other heap operations: change a node's value, merge heaps
    # useful: https://brilliant.org/wiki/heaps/


heap = MinHeap(10)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(2)
heap.insert(0)
heap.insert(1)
# heap.level_order()

root = heap.remove()
# print(root)
root = heap.remove()
root = heap.remove()
root = heap.remove()
root = heap.remove()
root = heap.remove()


heap.level_order()
    