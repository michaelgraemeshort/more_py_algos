from collections import deque


class Graph:
    def __init__(self, connections=None):
        if not connections:
            self.connections = {}
        self.connections = connections

    def add_edge(self, node_1, node_2):
        # adds an edge from node_1 to node_2, but NOT from node_2 to node_1
        self.connections[node_1].append(node_2)

    def breadth_first_search(self, root):
        q = deque()
        q.append(root)
        visited = set()
        while q:
            node = q.popleft()
            if node not in visited:
                print(node)
                for connection in self.connections[node]:
                    q.append(connection)
                visited.add(node)

    def depth_first_search(self, root):
        stack = []
        stack.append(root)
        visited = set()
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node)
                for connection in self.connections[node]:
                    stack.append(connection)
                visited.add(node)

    def topological_sort(self):
        # kahn's algorithm?
        # https://www.baeldung.com/cs/dag-topological-sort
        # basically, find nodes that have no incoming edges (in-degree of 0) and remove them
        # recalculate in-degrees as you go
        in_degrees = {key: 0 for key in self.connections}
        for i in self.connections.values():
            for j in i:
                in_degrees[j] += 1
        q = deque()  # only vertices that have NO INCOMING EDGES go here
        for key in in_degrees:
            if in_degrees[key] == 0:
                q.append(key)
        top_sorted = []  # only vertices that have NO INCOMING EDGES go here
        while q:
            # remove vertex from graph
            vertex = q.popleft()
            # get vertex's connections
            for key in self.connections[vertex]:
                # decrement in_degrees correspondingly
                in_degrees[key] -= 1
                # if i now has NO INCOMING EDGES
                if in_degrees[key] == 0:
                    q.append(key)
            # add vertex to output list
            top_sorted.append(vertex)
        return top_sorted

    def sssp_bfs(self, root, target):   # my effort
        """Single source shortest path using breadth first search"""
        parents = {vertex: None for vertex in self.connections}
        q = deque()
        q.append(root)
        visited = set()
        parent = None
        while q:
            node = q.popleft()
            if node not in visited:
                visited.add(node)
                parent = node
                for connection in self.connections[node]:
                    q.append(connection)
                for child in q:
                    if not parents[child]:
                        parents[child] = parent
        if not parents[target]:
            return "no path from root to target"
        shortest_path = [target]
        while parents[target]:
            shortest_path.append(parents[target])
            target = parents[target]
        shortest_path.reverse()
        return shortest_path

    def bfs(self, root, target):    # from the course
        q = deque()
        # note [] below - this is a queue of lists of possible paths from root, in order of increasing length
        q.append([root])
        while q:
            path = q.popleft()
            last_node = path[-1]
            if last_node == target:
                return path
            for connection in self.connections.get(last_node, []):
                # new_path = list(path) # from course. opaque
                # new_path = path[:]    # better
                new_path = path.copy()  # most explicit
                new_path.append(connection)
                q.append(new_path)

    def dijkstra(self, start, end):
        # how
        # something to do with a shortest path tree
        # start at start
        # visit adjacent vertices
        # for each adjacent vertex, record the path length from start
        # once all visited, move on to the nearest vertex
        # visit all of its adjacent vertices
        # calculate, for each, the distance from the start
        # and if you find a shorter path to a vertex, update its shortest path length
        # and also make a note of the preceding vertex
        # e.g. shortest path to E is from D, shortest path to D is from B, etc
        # start with a dict? vertex: shortest path length
        # initialise path lengths to None?
        # another dict? vertex: prior vertex for shortest path
        # going to need another graph class that can handle weighted edges



# connections = {
#     "a": ["b", "c"],
#     "b": ["a", "d", "e"],
#     "c": ["a", "e"],
#     "d": ["b", "e", "f"],
#     "e": ["d", "f"],
#     "f": ["d", "e"]
# }

# DAG, for testing topological sort
# connections = {
#     "a": ["c"],
#     "b": ["c", "d"],
#     "c": ["e"],
#     "d": ["f"],
#     "e": ["f", "h"],
#     "f": ["g"],
#     "g": [],
#     "h": []
# }

# unweighted undirected acyclic graph, for testing BFS for SSSPP
connections = {
    "a": ["b", "c"],
    "b": ["d", "g"],
    "c": ["d", "e"],
    "d": ["f"],
    "e": ["f"],
    "g": ["f"]
}

graph = Graph(connections)
# graph.breadth_first_search("a")
# graph.depth_first_search("a")
# print(graph.topological_sort())
# print(graph.sssp_bfs("a", "b"))
# print(graph.bfs("a", "f"))

