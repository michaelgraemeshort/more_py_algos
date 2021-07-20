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