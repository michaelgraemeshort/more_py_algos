#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Minimal Binary Search Tree

# given a sorted array with unique integer elements, write an algorithm to create a BST with minimal height

class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def minimalTree(sortedArray):   # NB this is not a method of class BSTNode
    # TODO
    # e.g. [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # not sure what this has to do with graphs
    # sorted, so no need to create an AVL tree class
    # binary search-style...?
    # take middle value, make it root
    # take middle value of values to left, make it left child, and also root of subtree
    # recursion
    if not sortedArray:
        return None # e.g. left_child = None
    # otherwise return the middle the middle value
    # but not before identifying the child nodes
    middle = len(sortedArray) // 2
    root = BSTNode(sortedArray[middle])
    root.left = minimalTree(sortedArray[:middle])
    root.right = minimalTree(sortedArray[middle + 1:])
    return root


arr = list(range(1, 10))
tree = minimalTree(arr)
print(tree.data)
print(tree.left.data)
print(tree.right.data)
print(tree.left.left.data)
print(tree.left.right.data)
print(tree.left.left.left.data)
print(tree.right.left.data)
print(tree.right.right.data)
print(tree.right.left.left.data)