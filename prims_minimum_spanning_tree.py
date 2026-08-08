"""
Prims - Minimum Spanning Tree Algorithm
Reference - https://neetcode.io/courses/advanced-algorithms/15

This algorithm finds the minimum weight of the edges that connects all the nodes. It's very similar to Dijkstra's.

A minimum spanning tree is the cheapest path from one node to all the other nodes in the graph.

TC: O(E*logV): In the worst case we will push all the edges into the heap and each push operation is O(log n). And and number of edges can be (V**2) as we know E = (V**2) in a complete
graph so we can reduce that to logV. 

SC: O(E)

Note: Prim's does not work on disconnect graph's as they are not connected building an MST is not possible. 

"""
import heapq

#edges: list of edges [src,des,w], n: no of vertices/nodes
def prims(n, edges):

    #building the adjList (graph representation)
    adjList = {}
    for i in range(1, n+1): #nodes are from 1 to n
        adjList[i] = []
    for src, des, weight in edges:
        adjList[src].append([des,weight])
        adjList[des].append([src,weight])

    minHeap = []
    for nei, weight in adjList[1]:
        heapq.heappush(minHeap, (weight, 1, nei)) #weight, src, des

    visit = set()
    visit.add(1)

    MST = [] #[[src, des]]

    while minHeap:
        weight, src, node = heapq.heappop(minHeap)

        if node in visit:
            continue

        MST.append([src, node])
        visit.add(node)

        for nei, weight in adjList[node]:
            if nei not in visit:
                heapq.heappush(minHeap, (weight, node, nei))

    return MST


    