# 1416. Restore The Array
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        '''
        DP. Similar to decode ways, except that we process the
        string from backwards to iterate each starting point.
        Let dp[i] be the answer for s[i:].
        dp[n] = 1 where n = len(s)
        dp[i] = sum(dp[j] for all valid j) where a valid j means 1 <= int(s[i:j]) <= k
        '''
        n = len(s)
        s = list(map(int, s)) + [math.inf] # for easier implementation
        dp = [0] * n + [1]
        MOD = 10 ** 9 + 7
        for i in range(n - 1, -1, -1):
            num, j = s[i], i + 1
            while 1 <= num <= k and j < len(dp):
                dp[i] = (dp[i] + dp[j]) % MOD
                num = 10 * num + s[j]
                j += 1
        return dp[0]