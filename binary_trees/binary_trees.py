from collections import deque

# binary tree


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


# tree = Node(2)
# tree.left = Node(1)
# tree.right = Node(4)
# tree.right.left = Node(3)
# tree.right.right = Node(5)

# pre-order traversal: NLR
# print node
# if left, print left
# otherwise print right
# something something recursion


def pre_order(node):
    print(node)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)


# print the root
# print its left child
# print its right child
# but what if the left child has a left child?
# print that BEFORE printing the right child
# as usual with recursion, consider the simplest case
# then call the function on a subset of the original argument


def in_order(node):
    # LNR
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)


# print the left, then the root, then the right
# in_order calls itself until it hits leftmost leaf node
# then prints that node, then its parent
# then calls itself on the right child
# etc


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)


# post_order(tree)

# post_order(node) prints node, but not until it has printed the left and/or right children, if they exist

# level order traversal
# using a queue for performance
# enqueue root
# print front of queue, then dequeue
# enqueue its children
# repeat until queue is empty


def level_order(node):
    q = deque()
    q.append(node)
    while q:
        print(q[0])
        front = q.popleft()
        if front.left:
            q.append(front.left)
        if front.right:
            q.append(front.right)


def search(node, value):
    """Return True if value is present in node or any of its children. Otherwise, False."""
    q = deque()
    q.append(node)
    while q:
        front = q.popleft()
        if front.data == value:
            return True
        if front.left:
            q.append(front.left)
        if front.right:
            q.append(front.right)
    return False


def insert(node, value):
    # traverses in level order, points first empty child slot at value
    q = deque()
    q.append(node)
    while q:
        front = q.popleft()
        if not front.left:
            front.left = Node(value)
            return
        else:
            q.append(front.left)
        if not front.right:
            front.right = Node(value)
            return
        else:
            q.append(front.right)


def delete(node, value):
    # replace data of node to be deleted with data of last node, when traversed in level order
    # deal with case of node with no children later
    # problem: can't just delete the last node, need to know its parent
    # so store the last node that has children in a variable
    # the last child of that node is the last node, in level order
    # this does not seem to be the usual way but works, I think
    q = deque()
    q.append(node)
    target = None
    last_parent = False
    previous_front = None
    # traverse in level order. aim to find node with specified value, and the last node that has children
    while q:
        front = q.popleft()
        # check if front is target node. if so, store in "target" variable
        if not target and front.data == value:
            target = front
        # check if front has children. if not, store previous front in "last_parent" variable
        if not last_parent and not front.left and not front.right:
            last_parent = previous_front
        # continue traversal
        if front.left:
            q.append(front.left)
        if front.right:
            q.append(front.right)
        previous_front = front
    if not target:
        raise ValueError(f"{value} not in tree")
    target.data = front.data
    if last_parent.right:
        last_parent.right = None
    else:
        last_parent.left = None


# # in_order(tree)
# for i in "abcde":
#     insert(tree, i)
# # level_order(tree)
# pre_order(tree)

tree = Node("root")
for i in range(10):
    insert(tree, i)
delete(tree, 11)
level_order(tree)