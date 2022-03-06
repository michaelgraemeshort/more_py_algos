# BST revision

from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __contains__(self, value):
        return self.contains(value)

    def in_order(self):
        # LNR
        if not self.root:
            return "tree is empty"
        self._in_order(self.root)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node)
            self._in_order(node.right)

    def pre_order(self):
        # NLR
        if not self.root:
            return "tree is empty"
        self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            print(node)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def post_order(self):
        # LRN
        if not self.root:
            return "tree is empty"
        self._post_order(self.root)

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node)

    def level_order(self):
        if not self.root:
            return "tree is empty"
        self._level_order(self.root)

    def _level_order(self, node):
        d = deque()
        d.append(node)
        while d:
            front = d.popleft()
            print(front)
            if front.left:
                d.append(front.left)
            if front.right:
                d.append(front.right)

    def insert(self, value):
        # iterative implementation
        # see py_algos for less space-efficient recursive implementation
        if not self.root:
            self.root = Node(value)
        node = self.root
        while node:
            last_node = node
            if value > node.data:
                node = node.right
            elif value < node.data:
                node = node.left
            else:
                raise ValueError(f"{value} already in tree")
        if value < last_node.data:
            last_node.left = Node(value)
        else:
            last_node.right = Node(value)

    def contains(self, value):
        # or use in operator
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node:
            if value == node.data:
                return True
            if value < node.data:
                return self._contains(node.left, value)
            else:
                return self._contains(node.right, value)
        return False

    def min_right_subtree(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.data

    def delete(self, value):
        if not self.root:
            return "tree is empty"
        self._delete(self.root, None, None, value)

    def _delete(self, node, parent, is_left, value):
        # a monster
        # cases to account for here:
        # 1. node with no children. point parent node left or right at None
        # 2. node with one child. point parent node left or right at child
        # 3. node with two children. see below
        # 4. account for whether node is root in each of the above cases
        if node:
            if value == node.data:
                # if no children
                if not node.left and not node.right:
                    # if not root node
                    if parent:
                        if is_left:
                            parent.left = None
                        else:    
                            parent.right = None
                    else:
                        self.root = None
                # if left child only
                elif node.left and not node.right:
                    # if not root node
                    if parent:
                        if is_left:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    else:
                        self.root = node.left
                        node.left = None
                # if right child only
                elif not node.left and node.right:
                    # if not root node
                    if parent:
                        if is_left:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    else:
                        self.root = node.right
                        node.right = None
                # if two children
                else:
                    # replace node value with minimum value from its right subtree
                    # (or max value from left subtree, but going with the former...)
                    # find and store min value
                    # delete the node with that value
                    # replace the original node's value
                    min_right_sub = self.min_right_subtree(node)
                    self.delete(min_right_sub)
                    node.data = min_right_sub
            elif value < node.data:
                self._delete(node.left, node, True, value)
            elif value > node.data:
                self._delete(node.right, node, False, value)
        else:
            raise ValueError(f"{value} not in tree")

    def clear(self):
        if not self.root:
            return "tree is empty"
        self.root = None
