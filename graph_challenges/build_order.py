#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Build Order

# find a build order, or if there isn't one, return an error
# return type not specified

from collections import deque


def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

modified_dependencies = [(j, i) for (i, j) in dependencies] # more helpful


def findBuildOrder(projects, dependencies):
    graph = createGraph(project, modified_dependencies)
    # {'a': ['f'], 'b': ['f'], 'c': ['d'], 'd': ['a', 'b'], 'e': [], 'f': []}    
    # topological sort
    # remove nodes that have no dependencies from graph
    # delete remaining dependencies accordingly
    zero_dependencies = deque()
    build_order = []
    for node in graph:
        if not len(graph[node]):
            zero_dependencies.append(node)
    while zero_dependencies:
        popped = zero_dependencies.popleft()
        build_order.append(popped)
        for node in graph:
            if popped in graph[node]:   # this would be more efficient if graph[node] were a set
                graph[node].remove(popped)
                if not len(graph[node]):
                    zero_dependencies.append(node)
    return build_order


print(findBuildOrder(project, dependencies))