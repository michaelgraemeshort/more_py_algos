
# Heights of subtrees must not differ by more than one
# Four possible ways to break this condition:
#
#    LL   |   RR    |   LR    |   RL
#         |         |         |         
#      3  |  1      |     3   |   1    
#     /   |   \     |    /    |    \   
#    2    |    2    |   1     |     3     
#   /     |     \   |   \     |     / 
#  1      |      3  |    2    |    2    
#
# LL:
# "rotate" unbalanced node to the "right" (clockwise)
#  
#      3
#     /       2
#    2   ->  / \
#   /       1   3
#  1
#
# RR:
# rotate unbalanced node to the left (anticlockwise)
# 
#  1
#   \         2
#    2   ->  / \
#     \     1   3
#      3
#
# LR:
# convert to LL by rotating the child of the unbalanced node to the left
# if the unbalanced node has two children, rotate the one with the greater height
#
#    3        3
#   /        /
#  1   ->   2
#  \       /
#   2     1
#  
# RL:
# convert to RR by rotating the child of the unbalanced node to the right
#
#  1         1
#   \         \
#    3   ->    2
#    /          \
#   2            3
#
# just look at https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# 


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
        d = deque()
        d.append(self)
        while d:
            front = d.popleft()
            print(front)
            if front.left:
                d.append(front.left)
            if front.right:
                d.append(front.right)

    def get_height(self):
        if not self: # no idea if this is going to work
            return 0
        return self.height

    def rotate_right(self):
        # assign node.left to a new variable
        new_root = self.left
        # deal with node.left.right if present. if it isn't...?
        self.left = self.left.right
        # rotate node to its rightful position
        new_root.right = self
        # update node's height
        self.height = 1 + max(self.left.get_height(), self.right.get_height())
        # don't know what this is for, yet. or whether it should be here
        return new_root
        
    def rotate_left(self):
        # the above, but reflected, obviously
        new_root = self.right
        self.right = self.right.left
        new_root.left = self
        self.height = 1 + max(self.left.get_height(), self.right.get_height())
        # don't know what this is for, yet
        return new_root

    def get_balance(self):
        # not sure why this is here, yet
        if not self:
            return 0
        return self.left.get_height() - self.right.get_height() # positive if left-heavy

    def insert(self, value):
        # # assuming self = root of tree
        # if not self: # another mystery and almost certainly inappropriate inclusion
        #     return AVLNode(value)
        # # bollocks to this
        # elif value < self.data:
        #     self.left.insert(value)

        # insert node, update heights (of everything), check balance, rotate if necessary
        # needs work

        new_node = AVLNode(value)

# test tree    

root = AVLNode(4)
root.left = AVLNode(2)
root.left.left = AVLNode(1)
root.left.right = AVLNode(3)
root.right = AVLNode(6)
root.right.left = AVLNode(5)
root.right.right = AVLNode(7)

root.level_order()

# traversals - pre, post, in, level
# search
# plagiarise from BST section

# pre-order = NLR
# print the node, if it exists
# then print its left child, then its right