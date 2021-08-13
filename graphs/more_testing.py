from collections import defaultdict
import heapq


class disjoint_set:
    # this is excellent https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
    # using hash table
    # could use list
    parents = {}
    ranks = {}

    def __init__(self, nodes):
        for node in nodes:
            self.parents[node] = node    # parent for each node is initialised to itself
            self.ranks[node] = 0

    def find(self, node):
        # returns the root of the subset containing node
        # path compression: if node is not root, change its parent to root
        # benefiting subsequent find operations
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node_1, node_2):
        # union by rank
        # attaches smaller tree to root of larger tree
        # minimises tree depth
        # improves search time complexity to O(log(n))
        x = self.find(node_1)
        y = self.find(node_2)
        if self.ranks[y] > self.ranks[x]:
            self.parents[x] = y
        elif self.ranks[x] > self.ranks[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            self.ranks[y] += 1


class Graph:
    # sod "vertices"
    def __init__(self):                       # examples:
        self.nodes = set()                    # {"a", "b", "c"}
        self.neighbours = defaultdict(list)   # {"a": ["b", "c"], "b": ["c"]}
        self.edge_lengths = dict()            # {("a", "b"): 3, ("a", "c"): 5, ("b", "c"): 4}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, length):
        self.neighbours[from_node].append(to_node)   # this is possible because self.neighbours is a defaultdict(list)
        self.edge_lengths[(from_node, to_node)] = length

    def dijkstra(self, start):
        # returns the shortest path lengths and routes from start node to ALL other nodes
        unvisited = self.nodes.copy()
        shortest_path_lengths = {node: float("inf") for node in sorted(list(self.nodes))}
        prior_node = {node: None for node in sorted(list(self.nodes))}
        shortest_path_lengths[start] = 0
        node = start
        priority_queue = []
        while unvisited:
            unvisited.remove(node)
            for neighbour in self.neighbours[node]:
                path_length = shortest_path_lengths[node] + self.edge_lengths[(node, neighbour)]
                if path_length < shortest_path_lengths[neighbour]:
                    shortest_path_lengths[neighbour] = path_length
                    prior_node[neighbour] = node
                    heapq.heappush(priority_queue, (shortest_path_lengths[neighbour], neighbour))
            if priority_queue:
                node = heapq.heappop(priority_queue)[1]
        return shortest_path_lengths, prior_node

    def bellman_ford(self, start):
        # iterate through edges
        # update shortest paths as appropriate
        # if changes still being made after len(self.nodes) iterations, negative cycle must be present
        # otherwise longest possible path will require (len(self.nodes) - 1) iterations (i.e. edge traversals) to find
        # haven't tested this on a graph with a negative cycle so beware
        # or any other graphs than the one below, for that matter
        shortest_path_lengths = {node: float("inf") for node in sorted(list(self.nodes))}
        shortest_path_lengths[start] = 0
        iterations = 0
        updating = True
        while updating and iterations <= len(self.nodes):
            updating = False
            iterations += 1
            for edge in self.neighbours:
                for neighbour in self.neighbours[edge]:
                    length = shortest_path_lengths[edge] + self.edge_lengths[(edge, neighbour)]
                    if length < shortest_path_lengths[neighbour]:
                        shortest_path_lengths[neighbour] = length
                        updating = True
        return "negative cycle present" if updating else shortest_path_lengths

    def adjacency_matrix(self):
        # returns a 2D list representation of self
        # IF graph nodes are "a", "b", etc
        matrix = [[float("inf") for i in range(len(self.nodes))] for j in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            matrix[i][i] = 0
        for i, j in self.edge_lengths.keys():
            # convert to integers
            matrix[ord(i) - 97][ord(j) - 97] = self.edge_lengths[(i, j)]
        # print matrix
        # for row in matrix:
        #     print(row)
        return matrix

    def floyd_warshall(self):
        # basic implementation
        # iterates through 2D array of path lengths
        # and on each iteration compares existing path length with path length via another node
        # iterates through all the other nodes
        # basically, on each iteration, you test if adding another node to the path shortens it
        # so you can't get to a longer path before testing its shorter component paths
        shortest_path_lengths = self.adjacency_matrix()
        number_of_nodes = len(self.nodes)
        for k in range(number_of_nodes):
            for i in range(number_of_nodes):
                for j in range(number_of_nodes):
                    shortest_path_lengths[i][j] = min(shortest_path_lengths[i][j],
                                                      shortest_path_lengths[i][k] + shortest_path_lengths[k][j])
        return shortest_path_lengths

    def kruskal(self):  # NEEDS TESTING and probably refactoring
        # organise edge lengths
        key_value_swap = {self.edge_lengths[key]: key for key in self.edge_lengths}
        lengths = sorted(list(key_value_swap.keys()))
        kvs = {key_value_swap[length]: length for length in lengths}
        ds = disjoint_set(self.nodes)
        unvisited = self.nodes.copy()
        minimum_spanning_tree = []
        while unvisited:
            for vertices in kvs:
                if ds.find(vertices[0]) == ds.find(vertices[1]):
                    # cycle detected, do not add to spanning tree
                else:
                    ds.union(vertices[0], vertices[1])
                    minimum_spanning_tree.append(vertices)
                    for vertex in vertices:
                        unvisited.remove(vertex)
        cost = 0
        for edge in minimum_spanning_tree:
            cost += self.edge_lengths(edge)
        return cost, minimum_spanning_tree


class disjoint_set:
    # this is excellent https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
    # using hash table
    # could use list
    parents = {}
    ranks = {}

    def __init__(self, nodes):
        for node in nodes:
            self.parents[node] = node    # parent for each node is initialised to itself
            self.ranks[node] = 0

    def find(self, node):
        # returns the root of the subset containing node
        # path compression: if node is not root, change its parent to root
        # benefiting subsequent find operations
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node_1, node_2):
        # union by rank
        # attaches smaller tree to root of larger tree
        # minimises tree depth
        # improves search time complexity to O(log(n))
        x = self.find(node_1)
        y = self.find(node_2)
        if self.ranks[y] > self.ranks[x]:
            self.parents[x] = y
        elif self.ranks[x] > self.ranks[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            self.ranks[y] += 1

# disjoint (non-overlapping) sets: a group of sets in which no item can be in more than one set
# AKA union-find data structure
# useful for cycle detection
# kruskal's:
# create a disjoint set - each vertex in its own subset
# iterate through edges of graph, in order of increasing weight
# for each edge, use the find operation to check if its vertices are in different sets
# by comparing their parents (same parent, same set)
# if different, perform union operation
# by taking the root of the subset containing each vertex, and making one the parent of the other
# thus building sets of connected vertices
# if False, the edge connects vertices that are already in the same set, creating a cycle
# for example, if 1, 2, and 3 are connected, you cannot add an edge connecting 1 and 3 without creating a cycle

graph = Graph()

# for i in "abcdefg":
#     graph.add_node(i)

# graph.add_edge("a", "b", 2)
# graph.add_edge("a", "c", 5)
# graph.add_edge("b", "c", 6)
# graph.add_edge("b", "d", 1)
# graph.add_edge("b", "e", 3)
# graph.add_edge("c", "f", 8)
# graph.add_edge("d", "e", 4)
# graph.add_edge("e", "g", 9)
# graph.add_edge("f", "g", 7)

# print(graph.dijkstra("a"))
# print(graph.bellman_ford("a"))

# graph.adjacency_matrix()

for i in "abcd":
    graph.add_node(i)

graph.add_edge("a", "b", 6)
graph.add_edge("b", "a", 6)
graph.add_edge("a", "c", 3)
graph.add_edge("c", "a", 3)
graph.add_edge("a", "d", 1)
graph.add_edge("d", "a", 1)
graph.add_edge("b", "c", 2)
graph.add_edge("c", "b", 2)
graph.add_edge("c", "d", 1)
graph.add_edge("d", "c", 1)

argh = graph.floyd_warshall()
for row in argh:
    print(row)