# 1340. Jump Game V
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        '''
        1/2 DFS on graph.
        Use a monotonic decreasing stack to find the first left higher point
        for each index. Then scan with the reserved direction, to find the
        first right higher point for each index.
        Then use DFS to find the longest path.
        We can't find the first lower point, because there can be better (
        higher than the first lower point but also within d) lower point
        that's further.
        '''
        jumps = defaultdict(list)

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

        @lru_cache(None)
        def dfs(i):
            return 1 + max((dfs(j) for j in jumps[i]), default = 0)

        return max(dfs(i) for i in range(N))
        '''
        2/2 DP with monotonic decreasing stack.
        Let f[i] be the answer if we start jumping at index i.
        All f[i] starts with 1 based on the problem description.
        f[i] = max(f[i], f[j]) for all j on the left within d distance, and arr[j] < arr[i];
        f[i] = max(f[i], f[j]) for all j on the right within d distance, and arr[j] < arr[i].
        The monotonic decreasing stack ensures the relation arr[j] < arr[i].
        '''
        dp = [1] * (len(arr) + 1)
        stack = []
        for i, n in enumerate(arr + [1000000]):
            while stack and arr[stack[-1]] < n:
                same_height_idx = [stack.pop()]
                while stack and arr[stack[-1]] == arr[same_height_idx[0]]:
                    same_height_idx.append(stack.pop())
                for j in same_height_idx:
                    # jump from i to j
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    # jump from stack[-1] to j
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)
            stack.append(i)
        return max(dp[:-1])