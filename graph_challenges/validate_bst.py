#   Created by Elshad Karimov
#   Copyright © AppMillers. All rights reserved.

# Validate BST

# implement a function to check if a binary tree is a BST

# left child has be < parent
# and also < all its ancestors
# check it's less than its parent and the root node
# check the left subtree is valid:
# that each left child is < its parent
# that each right child is > its parent
# that no node is > root
# check the right subtree is valid:
# that each left child is < its parent
# that each right child is > its parent
# that no node is < root
  

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# def isValidBST(root: TreeNode) -> bool:
#     # TODO
#     # this is horrible
#     def in_order(node: TreeNode):
#         nonlocal lst
#         if node:
#             in_order(node.left)
#             lst.append(node.val)
#             in_order(node.right)

#     lst = []
#     in_order(root)    
#     for i in range(1, len(lst)):
#         if lst[i] <= lst[i - 1]:
#             return False
#     return True

    # never mind nonlocal
    # pass the value in properly
    # somehow
    # possible?

def isValidBST(root: TreeNode) -> bool:
    # traverse in-order
    # if node is encountered which is <= preceding node, abort traversal
    # in-order is LNR
    # usually: if node, print node
    # here: if node, update "last" variable IF it is > preceding node, otherwise abort
    
    def in_order(node):
        nonlocal valid
        nonlocal last
        if node and valid:
            in_order(node.left)
            if node.val > last:
                last = node.val
            else:
                valid = False
            in_order(node.right)
        
    valid = True
    last = float("-inf")
    in_order(root)
    return valid

    # haven't tested the one from the course but looks broken
    # (doesn't appear to account for ancestor of right child < root and vice versa)




tree = TreeNode(3)
tree.left = TreeNode(1)
tree.right = TreeNode(5)
tree.right.left = TreeNode(4)


print(isValidBST(tree))












#     return isValidBST(root, root)
#     if not root:
#         return True
#     left_subtree_valid = isValidBST(root.left)
#     right_subtree_valid = isValidBST(root.right)
#     # or something

# def _isValidBST(node: TreeNode, root: TreeNode) -> bool:
#     if not node:
#         return True
#     left_subtree_valid = _isValidBST(node.left, root)
#     right_subtree_valid = _isValidBST(node.right, root)
#     if left_subtree_valid and right_subtree_valid:
#         both_subtrees_valid = True
#     # below needs work
#     # whether the child should be more or less than root depends on whether it is to left or right
#     # 
#     if node.left:
#         if node.left.val < node.val and node.left.val < root.val:
#             left_node_valid = True
#     if node.right:
#         if node.right.val < node.val and node.right.val > root.val:
#             right_node_valid = True
#     if left_node_valid and right_node_valid:
#         both_children_valid = True
#     if both_subtrees_valid and both_children_valid:
#         return True
#     return False
    

# # establish the subtree is valid
# # then establish the child itself is valid
# # if a left child, it must be less than its parent
# # and also less than the root of the tree
# # bloody recursion

    

