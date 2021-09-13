#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Validate BST

# write an algorithm to find the in-order successor of a given node in a BST

class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node   # this means each inserted Node has a parent attribute. not entirely transparent Mr K
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node


def inOrderSuccessor(root, n):
    # TODO
    # idiotic from-the-hip approach
    # (didn't realise that each inserted node has a parent attribute)
    def in_order(node):
        nonlocal in_order_list
        if node:
            in_order(node.left)
            in_order_list.append(node.data)
            in_order(node.right)

    in_order_list = []

    in_order(root)
    # should binary search as list is sorted but cba
    return in_order_list[in_order_list.index(n) + 1]

def in_order_successor(root, n):
    # key insights from the course: if a node has a right subtree, successor is the smallest value in that tree
    # if not, it's the nearest ancestor that is greater in value
    def min_right_subtree(node):
        node = node.right
        while node.left:
            node = node.left
        return node

    def nearest_greater_ancestor(node):
        parent = node.parent
        while parent.data < node.data:
            parent = parent.parent  # brilliant
        return parent

    # find n
    node = root
    while node.data != n:
        if n < node.data:
            node = node.left
        if n > node.data:
            node = node.right
    
    if node.right:
        return min_right_subtree(node).data
    else:
        return nearest_greater_ancestor(node).data



tree = Node(4)
for i in "213657":
    insert(tree, int(i))

# for i in range(1, 7):
#     print(inOrderSuccessor(tree, i))

for i in range(1, 7):
    print(in_order_successor(tree, i))



