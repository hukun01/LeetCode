# 1553. Minimum Number of Days to Eat N Oranges
class Solution:
    '''
    Memoized DFS with tricks.
    Note that any number greater than 1 can become 2's or 3's multiplies,
    after subtracting 1 or 2 from it. Hence there's no need to go deep
    on the search path for (n-1).
    Assuming op1 is minus n by 1, op2 is divide n by 2, op3 is divide n by 3.
    For any number, we can either go op2/op3 if applicable, or go op1 for
    once or twice, then op2/op3.
    '''
    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(self.minDays(n // d) + n % d for d in [2, 3])