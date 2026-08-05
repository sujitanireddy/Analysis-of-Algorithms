#Dijkstra's Algorithm
"""
This algorithm is used to find the shortest path in the graph with weights on edges. 

BFS works well if the edges of the graph is unweighted, but it fails to account for weights and that's where Dijkstra's algorithm comes into play. 

It's very similar to traditional BFS, just with a few tweaks.

Coming to the implementation: We use a minHeap instead of a queue for doing our search.

Time Complexity: E * log V
"""

