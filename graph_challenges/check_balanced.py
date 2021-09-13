#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Balanced Tree

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# implement a function to check if a binary tree is balanced
# i.e. heights of subtrees of any node do not differ by > 1
# notes below


def isBalanced(root):
    return _isBalanced(root) > 0


def _isBalanced(root):
    if not root:
        return 0
    left_subtree_height = _isBalanced(root.left)
    right_subtree_height = _isBalanced(root.right)
    if left_subtree_height == -1 or right_subtree_height == -1:
        return -1
    if abs(left_subtree_height - right_subtree_height) > 1:
        return -1
    return max(left_subtree_height, right_subtree_height) + 1


# test

tree = Node(2)
tree.left = Node(1)
tree.left.left = Node(2)

print(isBalanced(tree))


# hash table? node: height from bottom up?
# get height of a given node by...?
# add one to height of child with greater height
# how to start at the bottom?
# level order traversal backwards?
# another hash table of node: children?
# no as not all unique values
# could use node memory addresses rather than values
# off-piste, probably
# top-down:
# get height of left subtree
# get height of right subtree
# compare
# get height of subtree by:
# get height of left subtree
# get height of right subtree
# recursion
# base case: subtree does not exist - height == 0
# otherwise, height += 1, or something
# the problem: isBalanced should return a bool, but height is an int
# helper function?
