# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Build the graph, and ensure no cycles.
        Use DFS with memoization to find cycles.
        Total time is O(E + V) where E is number of edges, V is number of vertices.
        '''
        graph = defaultdict(list)
        
        for i, j in prerequisites:
            graph[i].append(j)

        path = [False] * numCourses
        
        @functools.lru_cache(None)
        def hasCycle(current):
            if path[current]:
                return True

            path[current] = True

            if any(hasCycle(children) for children in graph[current]):
                return True

            path[current] = False
            return False
        
        return not any(hasCycle(current) for current in range(numCourses))