# 1510. Stone Game IV
'''
DP.
Key is to start trying from bigger number, to reduce search space.

Note that we can either leave the method and cache as a module method,
or add the cache decorator to the solution method, this way we reuse the
cache across all test cases.
'''

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        return any(not self.winnerSquareGame(n - x ** 2)
                   for x in range(int(n ** 0.5), 0, -1))