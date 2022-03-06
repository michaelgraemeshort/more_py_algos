from collections import defaultdict
# from queue import PriorityQueue  # uses the heapq module  # nope, can't work it
import heapq


class Graph:  # weighted directed graph
    def __init__(self):
        self.nodes = set()  # {"a", "b"}
        self.neighbours = defaultdict(list)  # {"a": ["b"]}
        self.edge_lengths = {}  # {"a, b": 3}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, origin, destination, weight):
        # add undirected functionality?
        self.neighbours[origin].append(destination)
        self.edge_lengths[(origin, destination)] = weight

    def dijkstra(self, start):
        unvisited = self.nodes.copy()
        shortest_path_lengths = {
            node: float("inf") for node in sorted(list(self.nodes))
        }
        previous_node = {
            node: None for node in sorted(list(self.nodes))
        }  # sorted so prints in alphabetical order
        shortest_path_lengths[start] = 0
        node = start
        priority_queue = []
        while unvisited:
            unvisited.remove(node)
            for neighbour in self.neighbours[node]:
                if neighbour in unvisited:  # need to check this
                    path_length = (
                        shortest_path_lengths[node] + self.edge_lengths[(node, neighbour)]
                    )
                    if path_length < shortest_path_lengths[neighbour]:
                        shortest_path_lengths[neighbour] = path_length
                        previous_node[neighbour] = node
                        heapq.heappush(priority_queue, (shortest_path_lengths[neighbour], neighbour))
            if priority_queue:
                node = heapq.heappop(priority_queue)[1]
        return shortest_path_lengths, previous_node

        
    def bellman_ford(self, start):    
        shortest_path_lengths = {node: float("inf") for node in sorted(list(self.nodes))}
        previous_node = {
            node: None for node in sorted(list(self.nodes))
        }
        shortest_path_lengths[start] = 0
        iterations = 0
        updating = True
        while updating and iterations <= len(self.nodes):
            updating = False
            iterations += 1
            for node in self.neighbours:
                for neighbour in self.neighbours[node]:
                    path_length = shortest_path_lengths[node] + self.edge_lengths[(node, neighbour)]
                    if path_length < shortest_path_lengths[neighbour]:
                        shortest_path_lengths[neighbour] = path_length
                        previous_node[neighbour] = node
                        updating = True
        return "negative cycle present" if updating else shortest_path_lengths, previous_node




graph = Graph()
graph.add_node("a")
graph.add_node("b")
graph.add_node("c")
graph.add_edge("a", "b", 3)
graph.add_edge("a", "c", 2)
graph.add_edge("b", "c", -2)
print(graph.nodes)
print(graph.edge_lengths)
print(graph.dijkstra("a"))
