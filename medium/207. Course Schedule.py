# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        1/2 Topological sorting
        '''
        preCount = Counter()
        successors = defaultdict(list)
        for a, b in prerequisites:
            preCount[a] += 1
            successors[b].append(a)
        
        taken = 0
        free = set(range(numCourses)) - preCount.keys()
        while free:
            b = free.pop()
            taken += 1
            for a in successors[b]:
                preCount[a] -= 1
                if preCount[a] == 0:
                    free.add(a)
        
        return taken == numCourses
        '''
        2/2 DFS.
        Build the graph, and ensure no cycles.
        Use DFS with memoization to find cycles.
        Total time is O(E + V) where E is number of edges, V is number of vertices.
        '''
        prereqs = defaultdict(list)
        
        for b, a in prerequisites:
            prereqs[b].append(a)

        path = [False] * numCourses
        
        @lru_cache(None)
        def has_cycle(current):
            if path[current]:
                return True

            path[current] = True

            if any(has_cycle(children) for children in prereqs[current]):
                return True

            path[current] = False
            return False
        
        return not any(has_cycle(current) for current in range(numCourses))
