# 518. Coin Change 2
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        DP.
        1/3 2-D array.
        dp[i][j] is the number of combinations to
        make amount j with the first i coins.
        State transition:
        1. not using i-th coin, there are dp[i-1][j] ways;
        2. using i-th coin, dp[i][j-coins[i-1]]
        '''
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        dp[0][0] = 1
        for i in range(1, len(coins) + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[len(coins)][amount]
        '''
        2/3 Reduce to 1-D based on above 2-D.
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i-c]
        return dp[amount]
        '''
        3/3 Another style: DFS with memoization.
        '''
        @functools.lru_cache(None)
        def dfs(val, idx):
            if val == 0:
                return 1
            if val < 0 or idx < 0:
                return 0
            # first item is the number if not using coins[idx] at all;
            # second item is to use coins[idx].
            return dfs(val, idx - 1) + dfs(val - coins[idx], idx)
            
        return dfs(amount, len(coins) - 1)