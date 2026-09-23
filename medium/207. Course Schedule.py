# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        1/2 Topological sorting
        Note that the original problem description has a confusing prerequisite
        order. [a, b] means "b is a prereq for a". In our code we model it as 
        "a -> b" aka "a is a prereq for b", so we use [b, a] when traversing prerequisites.
        '''
        pre_count = defaultdict(int)
        succs = defaultdict(list)
        for b, a in prerequisites:
            pre_count[b] += 1
            succs[a].append(b)
        free = set(range(numCourses)) - set(pre_count)
        taken = 0
        while free:
            a = free.pop()
            taken += 1
            for b in succs[a]:
                pre_count[b] -= 1
                if pre_count[b] == 0:
                    free.add(b)
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
