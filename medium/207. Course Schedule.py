# 207. Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        1/2 Topological sorting
        '''
        pre_count = defaultdict(int)
        succs = defaultdict(list)
        for b, a in prerequisites:
            pre_count[b] += 1
            succs[a].append(b)
        free = set(range(numCourses)) - set(pre_count)
        taken = []
        while free:
            a = free.pop()
            taken.append(a)
            for b in succs[a]:
                pre_count[b] -= 1
                pre_count[b] or free.add(b)
        return len(taken) == numCourses
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