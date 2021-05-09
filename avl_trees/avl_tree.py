# juicy stuff further down
# todo: docstrings, error handling

from collections import deque
from random import shuffle


class AVLTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)


class AVLTree:
    def __init__(self, root):
        self.root = AVLTreeNode(root)

    def __contains__(self, value):
        return self._contains(self.root, value)

    def _contains(self, node, value):
        if node:
            if node.data == value:
                return True
            elif node.data > value:
                return self._contains(node.left, value)
            elif node.data < value:
                return self._contains(node.right, value)
        return False

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, node):
        # LNR
        if node:
            self._in_order(node.left)
            print(node)
            self._in_order(node.right)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, node):
        # NLR
        if node:
            print(node)
            self._pre_order(node.left)
            self._pre_order(node.right)

    def post_order(self):
        self._post_order(self.root)

    def _post_order(self, node):
        # LRN
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node)

    def level_order(self):
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

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def get_min_value_node(self, node):
        if not node.left:
            return node
        return self.get_min_value_node(node.left)

# consider this tree for the following, where T1, T2, T3 and T4 are subtrees:
#
#        z                            y
#       / \     rotate_right(z)     /   \
#      y   T4   --------------->   x     z
#     / \                         / \   / \
#    x   T3                      T1 T2 T3  T4
#   / \
# T1   T2
#
# adapted from https://www.geeksforgeeks.org/avl-tree-set-1-insertion/

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        # perform rotation
        y.left = z
        z.right = T2
        # update heights. z before its new parent y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        # return the new root
        if z is self.root:
            self.root = y
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right
        # perform rotation
        y.right = z
        z.left = T3
        # update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        # return the new root
        if z is self.root:
            self.root = y
        return y

    def rebalance(self, node, balance):
        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

    def insert(self, value):
        # does NOT notify you if the node you try to insert is already in the tree
        self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return AVLTreeNode(value)
        if value < node.data:
            node.left = self._insert(node.left, value)
        elif value > node.data:
            node.right = self._insert(node.right, value)
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        balance = self.get_balance(node)
        if balance > 1 or balance < -1:
            return self.rebalance(node, balance)
        return node

    def delete(self, value):
        # does NOT notify you if the node you try to delete isn't in the tree
        self._delete(self.root, value)

    def _delete(self, node, value):
        if not node:
            return node  # return None?
        elif value < node.data:
            node.left = self._delete(node.left, value)
        elif value > node.data:
            node.right = self._delete(node.right, value)
        else:  # value == node.data
            if not node.left:  # handles both 1) no left child, and 2) leaf node
                temp = node.right
                if node is self.root:
                    self.root = temp
                node = None  # ?unnecessary
                return temp
            elif not node.right:
                temp = node.left
                if node is self.root:
                    self.root = temp
                node = None
                return temp
            # else: (i.e. has two children)
            min_right_subtree = self.get_min_value_node(node.right)
            node.data = min_right_subtree.data
            node.right = self._delete(node.right, min_right_subtree.data)
        self.update_height(node)
        balance = self.get_balance(node)
        if balance > 1 or balance < -1:
            return self.rebalance(node, balance)
        return node


# rudimentary testing
tree = AVLTree(5)
l = list(range(10))
shuffle(l)
for i in l:
    tree.insert(i)

tree.delete(11)
print("---")
tree.in_order()