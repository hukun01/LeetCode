# 1340. Jump Game V
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        '''
        Build the graph with each index pointing to the first higher point from
        left and right. Then use DFS to find the longest path.
        We need to check both sides, instead of only the lower side, because it's
        possible that the higher side connects to a longer path that's out of
        current reachable distance.
        '''
        jumps = collections.defaultdict(list)
        
        def check(it):
            stack = []
            for i in it:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        jumps[j].append(i)
                stack.append(i)
        N = len(arr)
        check(range(N))
        check(reversed(range(N)))
        
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            cache[i] = 1 + max(map(dfs, jumps[i]), default = 0)
            return cache[i]
        
        return max(map(dfs, range(N)))