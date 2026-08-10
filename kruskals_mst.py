class UnionFind:

    #Initialize parent and rank hashmaps where each node is the parent of itself and all the ranks start at 0. Rank is height
    def __init__(self, n):
        self.parent = {}
        self.rank = {}

        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0

    #Finding the root of the node
    def find(self, n):
        while n!= self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    #Union'ing both the nodes
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2: return False #Cycle detected. Basically both the parents of the given node are the same that means they are already connected.  

        #Union by rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1

        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2 

        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        return True


"""
Kruskal's (Minimum Spanning Tree Algorithm)
Reference -> https://neetcode.io/courses/advanced-algorithms/16

We choose the smallest edge and keep adding to MST if we can union them. 

Union Find is going to help us if we detect a cycle. If a cycle is detected, that means that we cannot add that to MST. 

Kruskasl's is also a greedy algorithm similar to Prims, it performs better in sparser graphs where as Kruskals works better in denser graphs.

TC: O(ElogV)
"""


# Given an list of edges of a connected undirected graph, with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree. edges = (src,des,weight)

import heapq
import 

def minimum_spanning_tree(edges, n):

    minHeap = []

    for n1, n2, weight in edges:
        heapq.heappush(minHeap, (weight, n1, n2))

    mst = []

    unionFind = UnionFind(n)

    while len(mst) < n - 1:
        weight, n1, n2 = heapq.heappop(minHeap)

        if not unionFind.union(n1,n2):
            continue

        mst.append(n1,n2)

    return mst