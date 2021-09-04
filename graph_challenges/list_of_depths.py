from typing import List

#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# List of Depth


class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)

    def __str__(self):
        return "({val})".format(val=self.val) + str(self.next)


class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth(tree):
    # TODO
    pass


def treeToLinkedList(tree, custDict={}, d=None):
    # TODO
    pass

# "given a BST, design an algorithm which creates a linked list of all the nodes at each depth"
# disregarding the two functions immediately above...


def level_order(root: BinaryTree) -> List[LinkedList]:
    levels = []
    level = [root]
    while level:
        levels.append(level)
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    # convert List[List[BinaryTree]] into List[LinkedList]
    linked_lists = []
    for lst in levels:
        linked_list = LinkedList(lst[0].val)
        for node in lst[1:]:
            linked_list.add(node.val)
        linked_lists.append(linked_list)
    return linked_lists


# now test

tree = BinaryTree(4)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(1)
tree.left.right = BinaryTree(3)
tree.right = BinaryTree(6)
tree.right.left = BinaryTree(5)
tree.right.right = BinaryTree(7)

linked_lists = level_order(tree)

for linked_list in linked_lists:
    print(linked_list)

# appears to work
