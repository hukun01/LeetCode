# 1745. Palindrome Partitioning IV
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        '''
        DP.
        Pre-compute whether each substring is a palindrome, this takes O(n^2)
        time. Then go through all possible middle interval, note that the
        middle interval can split the string into 3 intervals. Now check
        whether all 3 intervals are palindrome.

        Time: O(n^2)
        Space: O(n^2)
        '''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                if s[l] == s[r]:
                    if l + 1 <= r - 1:
                        dp[l][r] = dp[l + 1][r - 1]
                    else:
                        dp[l][r] = True

        for l in range(1, n - 1):
            for r in range(l, n-1):
                if dp[0][l - 1] and dp[l][r] and dp[r + 1][n - 1]:
                    return True

        return False