from collections import deque

class AVLNode:
    def __init__(self, data): # type hint? data: int?
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

    def __contains__(self, value):
        if self.data == value:
            return True
        if self.data > value and self.left:
            return self.left.__contains__(value)
        if self.data < value and self.right:
            return self.right.__contains__(value)
        return False

    def pre_order(self): # NLR
        print(self)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
    
    def in_order(self): # LNR
        if self.left:
            self.left.in_order()
        print(self)
        if self.right:
            self.right.in_order()

    def post_order(self): # LRN
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self)

    def level_order(self):
        pass # TBC

# test tree    

root = AVLNode(4)
root.left = AVLNode(2)
root.left.left = AVLNode(1)
root.left.right = AVLNode(3)
root.right = AVLNode(6)
root.right.left = AVLNode(5)
root.right.right = AVLNode(7)

for i in range(9):
    print(i in root)

# traversals - pre, post, in, level
# search
# plagiarise from BST section

# pre-order = NLR
# print the node, if it exists
# then print its left child, then its right