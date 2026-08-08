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