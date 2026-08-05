#Dijkstra's Algorithm
"""
This algorithm is used to find the shortest path in the graph with weights on edges. 

BFS works well if the edges of the graph is unweighted, but it fails to account for weights and that's where Dijkstra's algorithm comes into play. 

It's very similar to traditional BFS, just with a few tweaks.

Coming to the implementation: We use a minHeap instead of a queue for doing our search.

Time Complexity: E * log V
"""

# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the
# graph. There are n nodes in the graph.
# O(E * logV), O(E * logE) is also correct.

import heapq

def shortestPath(edges, n, src):

    #building the adjList
    adjList = {}
    for i in range(1,n+1):
        adjList[i] = []

    #s = source, d = des and w = weight
    for s, d, weight in edges:
        adjList[src].append((d,weight))

    #Heap is going to contain a tuple of (weight, node)
    heap = [(0,src)]
    res = {}

    while heap:

        w1, n1 = heapq.heappop(heap)

        if n1 not in res:
            res[n1] = w1

        for n2, w2 in adjList[n1]:

            if n2 not in res:
                heapq.heappush(heap, (w1 + w2, n2))

    return res


    



