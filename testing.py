# see more_testing

from collections import deque
from collections import defaultdict
import heapq


class Graph:
    # sod "vertices"
    def __init__(self):                 # examples:
        self.nodes = set()              # {"a", "b", "c"}
        self.edges = defaultdict(list)  # {"a": ["b", "c"], "b": ["c"]}
        self.edge_lengths = dict()      # {("a", "b"): 3, ("a", "c"): 5, ("b", "c"): 4}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, length):
        self.edges[from_node].append(to_node)   # this is possible because self.edges is a defaultdict(list)
        self.edge_lengths[(from_node, to_node)] = length

    def dijkstra(self, start):
        # returns the shortest path lengths and routes from start node to ALL other nodes
        unvisited = self.nodes.copy()
        shortest_path_lengths = {node: None for node in self.nodes}
        prior_node = shortest_path_lengths.copy()
        shortest_path_lengths[start] = 0
        node = start
        priority_queue = []
        # visit the first node
        while unvisited:
            unvisited.remove(node)
            # visit its neighbours, update shortest path lengths and prior nodes
            for edge in self.edges[node]:
                # only update shortest path length for a node if the path is indeed shorter, or if None
                # same applies to priority queue
                path_length = shortest_path_lengths[node] + self.edge_lengths[(node, edge)]
                if not shortest_path_lengths[edge] or path_length < shortest_path_lengths[edge]:
                    shortest_path_lengths[edge] = path_length
                    prior_node[edge] = node
                    heapq.heappush(priority_queue, (shortest_path_lengths[edge], edge))
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
        shortest_path_lengths = {node: float("inf") for node in self.nodes}
        shortest_path_lengths[start] = 0
        iterations = 0
        updating = True
        while updating and iterations <= len(self.nodes):
            updating = False
            iterations += 1
            for edge in self.edges:
                for neighbour in self.edges[edge]:
                    length = shortest_path_lengths[edge] + self.edge_lengths[(edge, neighbour)]
                    if length < shortest_path_lengths[neighbour]:
                        shortest_path_lengths[neighbour] = length
                        updating = True
        return "negative cycle present" if updating else shortest_path_lengths





        # nodes = self.nodes.copy()
        # shortest_path_lengths = {node: float("inf") for node in nodes}
        # node = start
        # nodes.remove(node)
        # nodes = deque(nodes)
        # nodes.appendleft(start)
        # shortest_path_lengths[node] = 0
        # for nd in nodes:
        #     for neighbour in self.edges[nd]:
        #         path = shortest_path_lengths[nd] + self.edge_lengths[(nd, neighbour)]
        #         if path < shortest_path_lengths[neighbour]:
        #             shortest_path_lengths[neighbour] = path
        # return shortest_path_lengths







graph = Graph()

for i in "abcdefg":
    graph.add_node(i)

graph.add_edge("a", "b", 2)
graph.add_edge("a", "c", 5)
graph.add_edge("b", "c", 6)
graph.add_edge("b", "d", 1)
graph.add_edge("b", "e", 3)
graph.add_edge("c", "f", 8)
graph.add_edge("d", "e", 4)
graph.add_edge("e", "g", 9)
graph.add_edge("f", "g", 7)

print(graph.dijkstra("a"))
print(graph.bellman_ford("a"))