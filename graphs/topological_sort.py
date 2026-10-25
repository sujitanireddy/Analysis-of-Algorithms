"""
Topological Sort (DFS)
Reference - https://neetcode.io/courses/advanced-algorithms/17

Topological sort is a way of sorting a directed acyclic graph (DAG) such that each node comes before its dependent nodes. It does not work on un-directed graphs.

For example: Course Schedule 2 problem where we have to give the sequence of the courses that has to be finished.

We good deep and accumulate the nodes coming back and keep track so that we don't visit them again and this works for disjointed graphs as well.

Usually the ordering is in reverse and we have to return the reverse of it, but for course schedule problem it works out not having to reverse it.

TC: O(V + E)

Note: There is alsoKahn’s (BFS): computing indegrees is O(E). Each node enters and leaves the queue once (O(V)). Each edge decrements an indegree once (O(E)).

"""

def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adjList = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        res = []
        visit = set()
        processed = set()

        def dfs(c):
            
            if c in visit:
                return False

            if c in processed:
                return True

            visit.add(c)
            
            for nei in adjList[c]:
                if not dfs(nei):
                    return False
            
            visit.remove(c)
            processed.add(c)
            res.append(c)
            
            return True

        for c in range(numCourses):
            if c not in processed:
                if not dfs(c):
                    return []

        return res