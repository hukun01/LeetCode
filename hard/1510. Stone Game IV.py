# 1510. Stone Game IV
'''
DP.
Key is to start trying from bigger number, to reduce search space.

Note that we can either leave the method and cache as a module method,
or add the cache decorator to the solution method, this way we reuse the
cache across all test cases.
'''

class Solution:
    @cache
    def winnerSquareGame(self, n: int) -> bool:
        for i in range(int(n ** 0.5), 0, -1):
            if not self.winnerSquareGame(n - i ** 2):
                return True

        return False