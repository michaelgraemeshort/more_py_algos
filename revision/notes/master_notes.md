# Things to Remember

## Linked Lists

- kth-to-last element of a singly linked list - use two pointers

- Partitioning a linked list around a given value such that all elements of less than that value come before, and all elements of more come after: concatenate three lists - less, equal and more

- Intersection of two linked lists https://www.geeksforgeeks.org/write-a-function-to-get-the-intersection-point-of-two-linked-lists/

## Stacks and Queues

- Describe how you could use a single Python list to implement three stacks:
- By dividing the list into three, then writing a lot of irritating logic

- How would you design a stack with a `min` method that returns (but does not remove) the stack's minimum value?
- And runs in constant time 
- A linked list, in which each node knows the minimum value of the stack up to and including itself
- Elshad has a different solution, can't be bothered to figure it out though

- Make a queue using two stacks
- Dequeue is the hard part
- Reverse the order of one stack by popping all of its elements into the other
- Then pop the top (formerly bottom) item off the other
- If pushing more items on to the stack, first transfer the elements back to the first stack

- Animal Shelter
- Various ways to solve, not too difficult

## Binary Trees 

- Pre-order: NLR. Explores leaves last. Can be used to copy a tree.
- In-order: LNR. Gets BST values in non-decreasing order.
- Post-order: LRN. Explores leaves first. Can be used to delete a tree from leaf to root.
- Linked list representation:
    - Insertion: Traverse in level order, assign first empty child pointer to new value
    - Deletion:
        - To avoid gaps, such that tree shrinks from last (i.e. bottom right) node:
        - Find the node to be deleted and the last node
        - Replace with node to be deleted with the last node 
        - Delete the last node 
    - Some operations not as space-efficient as array representation
- Array representation:
    - Formulae are used to calculate the indices of a node's relatives
    - Formulae: https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/CompleteTree.html
    - Start at index 1, not 0, to simplify the above

## Binary Search Trees

- Insertion, traversal, search not difficult
- Deletion is the harder one
- If the node to be deleted has no children, just remove the pointer to it
- If it has one child, point its parent at that child
- If it has two children:
    - Get the minimum value from the right subtree, or the maximum from the left
    - Delete the node with that value
    - Replace the value of the node to be deleted with that value
- Don't forget to account for if-node-is-root in each of the above

## AVL Trees

- Just look at https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
- And memorise the procedure for rebalancing a node in LL, LR, RL and RR conditions (/figure out as required- not difficult)
- AVL tree nodes need a height attribute
- Update height, get balance, and rebalance as required

## Heaps

- Array representation most common
- Insertion: add value to end of tree, swap up as required to restore heap invariant
- Removal:
    - replace node to be removed (usually the root node) with the last node
    - Delete last node
    - Swap newly positioned node up or down as required to restore heap invariant
- https://hg.python.org/cpython/file/2.7/Lib/heapq.py (later rewritten in C)

## Tries

- "A sort of K-ary search tree", often used for string-related functions such as autocomplete and spellchecking

## Hash Tables 

- Hash a key (for example, using Python's built-in hash function) and mod the result by the number of buckets in the hash table to yield an index
- Then store the key and value in the bucket at that index
- If you don't store both, you'll have a hard time managing collisions

## Sorting Algorithms

- Insertion sort and (modified) bubble sort are O(n) if array is already sorted
- Selection sort is O(n^2) no matter what
- Selection sort is also unstable, unlike bubble and insertion sort 
- Basically, selection sort has no redeeming features, on the face of it 
- Comparison based sorting: elements of an array are compared with each other 
- Non-comparison based sorting: elements are not compared with each other
- Need to look into that (how can you not compare elements with each other?)
- Examples of non-comparison based sorting: radix sort, counting sort, bucket sort
- Insertion sort is also "online", i.e. can accept new data while sorting is ongoing
- Because new elements added to the right of the array will be swapped back into position
- So broadly insertion > modified bubble > selection
- Quicksort often performs better IRL than merge and heap sorts
- Big-O notation abstracts away constant terms, which can be significant
- Heap sort: create min heap, extract root until exhausted
- Miscellanea:
    - Quicksort and heap sort are not stable, but can run in-place
    - Quicksort worst-case time complexity can be O(n^2), depending on input (sorted array) and implementation (not shuffling the array prior to sorting, not picking a pivot at random)
    - Merge sort preferred for linked lists owing to slow random access (return to this)
- Todo: revise radix, bucket and counting sorts

## Searching Algorithms

- Linear search is trivially easy
- Code binary search now and then
- Disregard others for now (niche)

## Graphs

- Memorise the terminology (flashcards?)
- Weighted, unweighted, directed, undirected, cyclic, acyclic, etc
- Connected: there is a path between every pair of vertices, i.e. every vertex is reachable 
- Otherwise unconnected
- Strongly connected: there is a path between every pair of vertices in *both* directions
- Represent as adjacency list or adjacency matrix
- *Simple* graphs: no multiple edges (two or more edges that connect the same two vertices) or loops (edges that connect a vertex to itself)
- Graphs that contain the above are *multigraphs*
- *Complete*: every vertex is connected to every other vertex
- BFS and DFS are O(V+E) for adjacency list representation, and O(V^2) for adjacency matrix 

## Dijkstra

- Just visits available nodes in order of increasing distance from the source until it reaches the desired node (as in Dijkstra's original algorithm) or more commonly all nodes (producing a shortest path tree)
- Like breadth-first search, except "distance" is measured in edge weights rather than nodes
- So you need a queue (like BFS) but it needs to be ordered by increasing distance from the source (unlike BFS)
- i.e. a priority queue, in which the node most proximal to the source takes priority
- Priority queue: think (min) heap
- Need to maintain two hash tables:
    - One to record shortest-yet-discovered path length for each node
    - One to record the previous node on that path for each node
- You can then trace the shortest path from a given node back to the source via those previous nodes (again, like BFS)
- No negative edges, because does not try to find a shorter path to nodes which have already been visited
- (You can modify the algorithm so it does revisit nodes, as I did inadvertently, but is then slower)
- Time complexity of O(V^2) for adjacency matrix graph representation
- Time complexity of O(ElogV) for adjacency list representation using binary heap
- Or O(E + VlogV) using a Fibonacci heap
- Faster than Bellman Ford (O(VE))

## Bellman Ford

- Just iterates through every edge in the graph, over and over again, asking each time if the path through the origin to the destination is shorter than the current shortest known path
- There might be no known path to the origin, leading to "is infinity plus 6 less than infinity" type calculations, hence poorer time complexity
- But also means negative edges don't break the algorithm, as edges are revisited until shorter paths are no longer being discovered, a la modified bubble sort
- The algorithm should run at most len(nodes) - 1 times (the longest possible path between nodes has this many edges, at least one being discovered per cycle)
- If the algorithm is still making changes beyond this, a negative cycle must be present
- So can be used to detect negative cycles

## Floyd Warshall

- All-pairs shortest path finding algorithm
- O(n^3) as uses three nested for loops
- Iterates through a 2D array of path lengths
- And on each iteration compares existing path length with path length via another node (the outermost loop)
- Iterates through all the other nodes
- Basically, on each iteration, you test if adding another node to the path shortens it
- So you can't get to a longer path before testing its shorter component paths
- Does not return details of the paths themselves, but can be simply modified to do so
- Many esoteric applications

## Disjoint Set

- Disjoint (non-overlapping) sets: a group of sets in which no item can be in more than one set
- (Just a set divided into subsets, which can join subsets together and tell you which subset a given element belongs to)
- Subsets with more than one item are arranged as trees, with a root and descendants - each descendant carrying a reference to its parent (or the root, if its parent is not that)
- The root acts as the representative of the subset
- So if two elements have the same representative, they belong to the same subset
- AKA union-find data structure as supports union and find operations on subsets
- Union operation merges two subsets into one. The representative of the larger tree becomes the representative of the smaller one, if employing union by rank, which you should to improve search time complexity
- Find operation returns the representative of the node in question. Path compression is beneficial here
- Useful for cycle detection, e.g...
- In the case of a Kruskal's, do not add an edge to the spanning tree if it connects two vertices that have the same representative, i.e. are already in the tree. Because that would create a cycle
- Or just use Python's built-in set type

## Kruskal

- Sort edges in ascending order of weight, add to tree until all nodes connected (V - 1 edges in the tree)
- DO NOT add an edge if it creates a cycle
- O(ElogE) - the sorting of the edges dominates the runtime
- Therefore, better in graphs with fewer edges, i.e. sparse graphs
- Or if the edges are already sorted
- Disjoint set won't work for directed graphs as doesn't account for edge direction - the set of nodes in the MST contains just those nodes and not the directions of the edges that connect them https://stackoverflow.com/questions/61167751/can-we-detect-cycles-in-directed-graph-using-union-find-data-structure 
- (Use BFS or DFS instead)

## Prim

- Very much like Dijkstra
- Just keeps adding the nearest unvisited node to the tree
- O(ElogV), or O(E + VlogV) with Fibonacci heap, like Dijkstra


## Problems

- To be solved using greedy, divide-and-conquer and dynamic approaches where possible 
- Activity Selection Problem
- Coin Change Problem
- Fractional Knapsack Problem 
- Number Factor
- House Robber
- Convert one string to another 
- Zero One Knapsack
- Longest Common Subsequence 
- Longest Palindromic Subsequence
- Minimum cost to reach the last cell
- Number of ways to reach the last cell at a given cost

## Dynamic Programming

- Optimal substructure property: optimal solution can be obtained by using optimal solutions to subproblems
- Overlapping subproblems property: the same subproblems keep occurring

## Backtracking

- N Queens
- That array partitioning problem from SoloLearn


