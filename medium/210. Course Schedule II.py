# 210. Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Topological sorting.
        '''
        pre = defaultdict(int)
        suc = defaultdict(list)
        for a, b in prerequisites:
            pre[a] += 1
            suc[b].append(a)
        free = set(range(numCourses)) - set(pre)
        ans = []
        while free:
            a = free.pop()
            ans.append(a)
            for b in suc[a]:
                pre[b] -= 1
                pre[b] or free.add(b)
        return ans if len(ans) == numCourses else []