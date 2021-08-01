from collections import defaultdict
import heapq


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
        # iterates through 2D array of path lengths
        # and on each iteration compares existing path length with path length via another node
        # iterates through all the other nodes
        # for example, might compare the direct path from A to C with the path A -> B -> C and later A -> D -> C
        # but: if A -> D -> C is shortest, and this is discovered late in the process...
        # then any other paths that rely on A -> C that have already been determined will not be the shortest
        # clearly this is not a problem, but why
        # if the shortest path from A to B is via C, and later discover that A to C can be shortened via D, how to update A to B?
        # in that case the shortest path won't be via C, it will be via C AND D
        # so not a problem
        shortest_path_lengths = self.adjacency_matrix()
        number_of_nodes = len(self.nodes)
        for k in range(number_of_nodes):
            for i in range(number_of_nodes):
                for j in range(number_of_nodes):
                    shortest_path_lengths[i][j] = min(shortest_path_lengths[i][j],
                                                      shortest_path_lengths[i][k] + shortest_path_lengths[k][j])
        return shortest_path_lengths


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