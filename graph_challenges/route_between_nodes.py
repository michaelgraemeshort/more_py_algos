#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

# SSSP. unweighted, so use BFS

from collections import deque

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        # TODO
        kyoo = deque([[startNode]])
        while kyoo:
            path = kyoo.popleft()
            for connection in self.gdict[path[-1]]:
                if connection == endNode:
                    return True
                new_path = path.copy()
                new_path.append(connection)
                kyoo.append(new_path)
        return False

        
