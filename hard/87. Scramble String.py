# 87. Scramble String
class Solution:
    '''
    Memoized DFS.
    The base case is that if len(s1) == 1, whether s1 == s2.
    And of course we need to check sorted(s1) == sorted(s2) to ensure the
    possibility is there for a match.
    The recurisve case is to try each cut position, and there are 2 cases:
        1. (s1[:cut], s2[:cut]) and (s1[cut:], s2[cut:])
        2. (s1[:cut], s2[-cut:]) and (s1[cut:], s2[:-cut])

    If any recursion returns a True, we can return True.

    A trick for calling a method within itself, is to do `f = self.method`, and
    do `f(x1, x2)` later where it is equivalent to `self.method(x1, x2)`.
    '''
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n <= 1:
            return s1 == s2
        f = self.isScramble
        for cut in range(1, n):
            if f(s1[:cut], s2[:cut]) and f(s1[cut:], s2[cut:]) or \
               f(s1[:cut], s2[-cut:]) and f(s1[cut:], s2[:-cut]):
                return True
        return False