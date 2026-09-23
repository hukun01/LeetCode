# 210. Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Topological sorting.
        '''
        preCount = Counter()
        successors = defaultdict(list)
        for a, b in prerequisites:
            preCount[a] += 1
            successors[b].append(a)
        
        ans = []
        taken = 0
        free = set(range(numCourses)) - preCount.keys()
        while free:
            b = free.pop()
            taken += 1
            ans.append(b)
            for a in successors[b]:
                preCount[a] -= 1
                if preCount[a] == 0:
                    free.add(a)
        
        if taken == numCourses:
            return ans
        return []
