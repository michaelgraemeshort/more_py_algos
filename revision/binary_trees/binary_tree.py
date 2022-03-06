# linked list based implementation

from collections import deque  # for level order traversal


class Node:
    """Node for BinaryTree class."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    """Linked list-based binary tree implementation."""

    def __init__(self):
        self.root = None

    def __contains__(self, value):
        queue = deque()
        queue.append(self.root)
        while queue:
            if queue[0].value == value:
                return True
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def pre_order(self):
        self._pre_order(self.root)
        print()

    def _pre_order(self, node):
        if node:
            print(node, end=" ")
            self._pre_order(node.left)
            self._pre_order(node.right)

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node, end=" ")
            self._in_order(node.right)

    def post_order(self):
        self._post_order(self.root)
        print()

    def _post_order(self, node):
        if node:
            self._post_order(node.left)
            self._post_order(node.right)
            print(node, end=" ")

    def level_order(self):
        if not self.root:
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            print(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, value):
        # traverses in level order, points first free child pointer at value
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if not node.left:
                node.left = new_node
                return
            else:
                queue.append(node.left)
            if not node.right:
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def delete(self, value):
        # find the node to be deleted and the last node
        # replace with node to be deleted with the last node
        # delete the last node
        node_to_delete, parent_of_last_node, last_node = self._get_nodes(value)
        if not node_to_delete:
            raise ValueError(f"{value} not in BinaryTree")
        if not parent_of_last_node:  # one node tree
            self.root = None
            return
        node_to_delete.value = last_node.value
        if parent_of_last_node.right:
            parent_of_last_node.right = None
        else:
            parent_of_last_node.left = None

    def _get_nodes(self, value):    # was tired
        """
        Returns references to:
        1) The node with the given value, if present
        2) The parent of the last node in the tree
        3) The last node in the tree
        """
        node_to_delete = None
        queue = deque()
        queue.append(self.root)
        prev_node = None
        parent_of_last_node = None
        while queue:
            node = queue.popleft()
            if node.value == value:
                node_to_delete = node
            if not parent_of_last_node:
                if not node.left and not node.right:
                    parent_of_last_node = prev_node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            prev_node = node
        last_node = node
        return node_to_delete, parent_of_last_node, last_node
