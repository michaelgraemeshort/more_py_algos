class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left



def post_order(node, output_list):
    if node:
        post_order(node.left, output_list)
        post_order(node.right, output_list)
        output_list.append(node)



tree = Node(4)
tree.left = Node(2)
tree.right = Node(6)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right.left = Node(5)
tree.right.right = Node(7)

post_order_list = []
post_order(tree, post_order_list)

for node in post_order_list:
    pass
    # check node and its descendents for presence of n1 and n2
    # need to get rid of post-order list later - no extra memory usage permitted
    