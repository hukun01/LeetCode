# 1573. Number of Ways to Split a String
class Solution:
    def numWays(self, s: str) -> int:
        '''
        Math.
        Two cases:
        1. If there's no '1' in the input, any valid cut is good, so
           math.comb(n-1, 2).
        2. Otherwise, we need to do two cuts. There are x options to do
           cut1, when the '1's count == ones/3; there are y options to
           do cut2, when the '1's count == ones/3 * 2. The answer is x*y.
        '''
        MOD = 10 ** 9 + 7
        ones, n = s.count('1'), len(s)
        if ones == 0:
            return math.comb(n-1, 2) % MOD
        if ones % 3 != 0:
            return 0
        parts = ones // 3
        count = cut1 = cut2 = 0
        for char in s:
            if char == '1':
                count += 1
            if count == parts:
                cut1 += 1
            elif count == 2 * parts:
                cut2 += 1
        return cut1 * cut2 % MOD