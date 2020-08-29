# 1406. Stone Game III
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        Similar to 1140. Stone Game II.
        1/4 DFS with memoization.
        
        DFS returns the max gain that the current player can get by starting from i,
        so it's the max(total number of stones from i to end (denoted by suffixSums[i])
        minus the max stone the other player can get) with all possible steps the current
        player can make.
        '''
        # this is the suffix sums.
        stoneValue = list(itertools.accumulate(stoneValue[::-1]))[::-1]

        @lru_cache(None)
        def dfs(i):
            if i == len(stoneValue):
                return 0
            maxScores = -math.inf
            for x in range(i, min(i + 3, len(stoneValue))):
                maxScores = max(maxScores, stoneValue[i] - dfs(x + 1))
            return maxScores
        alice = dfs(0)
        bob = stoneValue[0] - alice
        if alice == bob:
            return "Tie"
        elif alice > bob:
            return "Alice"
        else:
            return "Bob"
        '''
        2/4 DFS with optimized memoization (but still not O(1) space).
        Like the other DP solutions point out, dp[i] relies on dp[i+1], dp[i+2], dp[i+3].
        We try to apply the same idea in DFS cache.

        Let's try to set the maxsize of LRU cache to be 3 to keep dp[i+1], dp[i+2], dp[i+3].

        Note that in below recursive call stack, each entry depends on its next 3 entries,
        since this is running with LRU cache, the most recent entries will be saved.
        In below example, when we finish D1, we have dfs(7), dfs(4), dfs(1)
        entries left in the cache. The entries here from left to right is the eldest to the newest.
        At this moment, we have computed all other entries, but discarded due to cache size.
        Now we need to compute D2, we need dfs(3), dfs(4), dfs(5),..., dfs(n) again.
        
        Apparently, with this access pattern and the cache size, the cache is not working.

        dfs(0) -> dfs(1), dfs(2), dfs(3)
            dfs(1) -> dfs(2), dfs(3), dfs(4)      D1
                dfs(2) -> dfs(3), dfs(4), dfs(5)     
                    ...dfs(n) -> 0
                dfs(3) -> dfs(4), dfs(5), dfs(6)
                dfs(4) -> dfs(5), dfs(6), dfs(7)
            dfs(2) -> dfs(3), dfs(4), dfs(5)      D2
            dfs(3) -> dfs(4), dfs(5), dfs(6)

        However, if we reverse the order in the iteration of (i+1, i+2, i+3), we do below DFS.
        When we are done with dfs(3), we have dfs(5), dfs(4), dfs(3)
        entries left in the cache. 
        Now we compute D2, which uses dfs(5), dfs(4), dfs(3), we just hit cache.
        And we update the cache to have dfs(4), dfs(3), dfs(2).
        Next we compute D3, which uses dfs(4), dfs(3), dfs(2), hit cache again.
        And we update the cache to have dfs(3), dfs(2), dfs(1).

        dfs(0) -> dfs(3), dfs(2), dfs(1)
            dfs(3) -> dfs(6), dfs(5), dfs(4)      D1
                dfs(6) -> dfs(9), dfs(8), dfs(7)
                    ...
                dfs(5) -> dfs(8), dfs(7), dfs(6)
                dfs(4) -> dfs(7), dfs(6), dfs(5)
            dfs(2) -> dfs(5), dfs(4), dfs(3)      D2
            dfs(1) -> dfs(4), dfs(3), dfs(2)      D3
        
        LRU cache with 3 entries is sufficient for our DFS.
        According to LC judge, the memory usage is reduced from 140MB to 80MB.
        '''
        stoneValue = list(itertools.accumulate(stoneValue[::-1]))[::-1]
        @lru_cache(3) # 1/2 diffs than normal DFS: just need 3 entries
        def dfs(i):
            if i == len(stoneValue):
                return 0
            maxScores = -math.inf
            # 2/2 diffs than normal DFS: reverse the iteration order
            for x in reversed(range(i, min(i + 3, len(stoneValue)))):
                maxScores = max(maxScores, stoneValue[i] - dfs(x + 1))
            return maxScores
        alice = dfs(0)
        bob = stoneValue[0] - alice
        if alice == bob:
            return "Tie"
        elif alice > bob:
            return "Alice"
        else:
            return "Bob"
        '''
        3/4 DP.
        Let dp[i] be the max stones a player can get by starting from i.
        dp[i] = max(sum(stoneValue[i:]) - dp[i + k] for k in range(1, 4))

        Pre-calculate the suffix sums to avoid repetitive calculation.

        Alice's score is dp[0], Bob's score is suffixSums[0] - dp[0]
        '''
        n = len(stoneValue)
        suffixSum = [0 for _ in range(n+1)]
        dp = [0 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            suffixSum[i] = suffixSum[i+1] + stoneValue[i]
        for i in range(n-1, -1, -1):
            dp[i] = stoneValue[i] + suffixSum[i+1] - dp[i+1]
            for k in range(i+1, min(n, i+3)):
                dp[i] = max(dp[i], suffixSum[i] - dp[k+1])
        alice = dp[0]
        bob = suffixSum[0] - alice
        if alice == bob:
            return "Tie"
        elif alice > bob:
            return "Alice"
        else:
            return "Bob"
        '''
        1/4 O(1) space DP
        Let dp[i] be the highest extra score of Alice if we start from i.
        From the end to the front, dp[i] is the max of below 3 options:
        Take A[i], win take - dp[i+1]
        Take A[i] + A[i+1], win take - dp[i+2]
        Take A[i] + A[i+1] + A[i+2], win take - dp[i+3]

        Although dp[i] is Alice's extra score, it can be used as Bob's extra score,
        when we compute dp[i-1] for Alice. dp[i] actually just denote the optimal
        extra score one can get based on dp[i+1], dp[i+2], and dp[i+3].
        '''
        dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))

        if dp[0] == 0:
            return "Tie"
        elif dp[0] > 0:
            return "Alice"
        else:
            return "Bob"