# 1545. Find Kth Bit in Nth Binary String
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return 2 * f(n - 1) + 1

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        '''
        The key of this problem is to not generate the whole sequences, that's
        too brutal.
        '''
        def dfs(n, k):
            l = f(n)
            if l == 1:
                return 0
            m = (1 + l) // 2
            if k == m:
                return 1
            if k < m:
                return dfs(n - 1, k)
            else:
                return 1 - dfs(n - 1, l - k + 1)
        return str(dfs(n, k))