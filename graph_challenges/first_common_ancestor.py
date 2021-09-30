#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# First Common Ancestor

# find the LOWEST common ancestor of two nodes in a binary tree
# NOT necessarily a BST
# avoid storing additional nodes in memory
# the LCA of a node and its ancestor is that node

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def findFirstCommonAncestor(n1: int, n2: int, root: Node) -> Node:
    # searches left and right subtrees recursively
    # returns n1 or n2, if found
    # or root if both found
    # otherwise None    
    # DOES NOT PASS course test, don't know why
    if not root:
        return None
    if root.value in (None, n1, n2):
        return root
    left = findFirstCommonAncestor(n1, n2, root.left)
    right = findFirstCommonAncestor(n1, n2, root.right)
    if left and right:  # if n1 and n2, or n2 and n1
        return root
    else:
        return left or right


tree = Node(4)
tree.left = Node(2)
tree.right = Node(6)
# tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.left = Node(5)
tree.right.right = Node(7)

print(findFirstCommonAncestor(3, 7, tree).value)