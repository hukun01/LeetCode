# 343. Integer Break
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        Math.
        Let f be the optimal product, if f >= 4, without losing optimality, we
        can replace f with 2 * (f - 2), because 2*(f-2) = 2f - 4 >= f.
        Since f can do above transform, we never need a factor >= 4, namely, we
        only need 1,2,3. And 1 is wasteful, so we only need 2 and 3.
        How to decide when to use 2 or 3, observe that 2 * 2 * 2 is less than
        3 * 3, so we at most use 2 twos.

        Time: O(log(n))
        Space: O(1)
        '''
        if n <= 3:
            return n - 1

        if n % 3 == 0:
            return pow(3, n // 3)
        elif n % 3 == 1:
            return 4 * pow(3, (n - 4) // 3)
        else:
            return 2 * pow(3, (n - 2) // 3)