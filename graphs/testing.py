# simple graph class

from collections import deque


class Graph:
    """unweighted graph represented as a dict of sets"""

    def __init__(self, graph_dict=None):
        if not graph_dict:
            self.graph_dict = {}
        self.graph_dict = graph_dict

    def add_edge(self, node_1, node_2):
        self.graph_dict[node_1].add(node_2)

    def breadth_first_search(self, root, value):
        # traverse graph in level order (rows, left-right)
        # using a queue
        q = deque()
        q.append(root)
        visited = set()
        while q:
            node = q.popleft()
            if node == value:
                return f"{value} is in graph. You know, you could just use in"
            if not node in visited:
                visited.add(node)
            for i in self.graph_dict[node]:
                if i not in visited:
                    q.append(i)
        return f"{value} is not in graph. No really, just use in"
        # went off-piste - was meant to be a traversal

    def depth_first_search(self, root):
        # traverse using a stack - explores as far as possible along each branch before backtracking
        s = []
        s.append(root)
        visited = set()
        while s:
            node = s.pop()
            if node not in visited:
                print(node)
                visited.add(node)
            for i in self.graph_dict[node]:
                if i not in visited:
                    s.append(i)
        # gives random order traversals, because of the dict-of-SETS representation of graph below
        # some redundancy here, see topological-sort.py


graph_dict = {
    "a": {"b", "c"},
    "b": {"a", "d", "e"},
    "c": {"a", "e"},
    "d": {"b", "e", "f"},
    "e": {"d", "f"},
    "f": {"d", "e"}
}

graph = Graph(graph_dict)

# for i in "abcdefg":
#     print(graph.breadth_first_search("a", i))

graph.depth_first_search("a")
