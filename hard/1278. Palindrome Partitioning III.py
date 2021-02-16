# 1278. Palindrome Partitioning III
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        '''
        DFS with memoization.
        '''
        @cache
        def cost(i, j):
            part = s[i:j]
            return sum(c1 != c2 for c1, c2 in zip(part, reversed(part))) // 2

        n = len(s)
        @cache
        def dfs(start, count):
            if n - start == count:
                return 0

            if count == 1:
                return cost(start, n)

            ans = inf
            for cut in range(start + 1, n - count + 2):
                ans = min(ans, dfs(cut, count - 1) + cost(start, cut))

            return ans

        return dfs(0, k)