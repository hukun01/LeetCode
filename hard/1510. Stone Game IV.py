# 1510. Stone Game IV
'''
DP.
Leave the method and cache as a module method, this way we reuse the cache
across all test cases.
'''

@functools.lru_cache(None)
def alice_win(n):
    if n == 0:
        return False

    # Trying i from bigger to smaller, to reduce search space.
    for i in range(int(n ** 0.5), 0, -1):
        if not alice_win(n - i * i):
            return True
    return False
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return alice_win(n)