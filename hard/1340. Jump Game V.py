# 1340. Jump Game V
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        '''
        1/2 DFS on graph.
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
        
        @functools.lru_cache(None)
        def dfs(i):
            return 1 + max(map(dfs, jumps[i]), default = 0)
        
        return max(map(dfs, range(N)))
        '''
        2/2 DP with monotonic stack.
        Let f[i] be the answer if we start jumping at index i.
        All f[i] starts with 1 based on the problem description.
        f[i] = max(f[i], f[j]) for all j on the left within d distance, and arr[j] < arr[i];
        f[i] = max(f[i], f[j]) for all j on the right within d distance, and arr[j] < arr[i].
        '''
        dp = [1] * (len(arr) + 1)
        stack = []
        for i, n in enumerate(arr + [1000000]):
            while stack and arr[stack[-1]] < n:
                same_height = [stack.pop()]
                while stack and arr[stack[-1]] == arr[same_height[0]]:
                    same_height.append(stack.pop())
                for j in same_height:
                    # jump to left
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    # jump to right
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])