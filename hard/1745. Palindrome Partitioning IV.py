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
        f = [[False] * n for _ in range(n)]

        for size in range(n):
            for i in range(n - size - 1, -1, -1):
                j = i + size
                f[i][j] = (i + 1 >= j - 1 or f[i+1][j-1]) and s[i] == s[j]

        for i in range(n-2):
            for j in range(i + 1, n - 1):
                if f[0][i] and f[i+1][j] and f[j+1][n-1]:
                    return True

        return False