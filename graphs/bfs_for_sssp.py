# breadth first search for single source shortest path problem
# which is the problem of finding the shortest path from one vertex to the others
# other ways: Dijkstra's, Bellman Ford
# a modified BFS in which the "parent" of each vertex (other than the root) is recorded
# you can then trace a path from a given node back to the root via its parents
# which yields the shortest path
# because BFS visits other nodes in order of increasing distance from the root

from collections import deque


def bfs_sssp(root, target):
    # do a breadth first search
    # which is basically a level order traversal
    # i.e. involves a queue
    # start with vertex
    # append it to queue
    # pop it out, append it to what would ordinarily be the output list
    # enqueue its children
    # etc, until queue is exhausted
    # but:
    # don't append it to queue if it has already been visited
    # so need a collection of visited nodes to check for this
    # additionally, need a collection of nodes' parents
    # which could then be zipped together with output list
    # yielding (node, parent), (node, parent), etc
    # dict better?
    # then, to get the shortest path from target to root...
    # find the target 
    # find its parent
    # find its parent's parent
    # and so on until you reach root
    # adding to a list as you go
    # then return the reversed list


    q = deque()
    q.append(root)
    visited = set()
    pairs = {}  # parent: child pairs
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            vertices.append(node)
            if not parents:
                parents.append(None)
            else:
                parents.append


connections = {
    "a": ["c"],
    "b": ["c", "d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["f", "h"],
    "f": ["g"],
    "g": [],
    "h": []
}