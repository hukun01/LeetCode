# 1278. Palindrome Partitioning III
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        '''
        DFS with memoization.
        '''
        @functools.lru_cache(None)
        def cost(i, j):
            return sum(c1 != c2 for c1, c2 in zip(s[i:j+1], s[i:j+1][::-1])) // 2
    
        n = len(s)
        @functools.lru_cache(None)
        def dfs(i, k):
            if n-i == k:
                return 0
            if k == 1:
                return cost(i, n-1)
            ans = math.inf
            for j in range(i+1, n-k+2):
                ans = min(ans, dfs(j, k-1) + cost(i, j-1))
            return ans

        return dfs(0, k)