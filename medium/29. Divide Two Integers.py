# 29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        Exponential search (similar to binary search).
        This only works with the given condition of truncation.
        Repeatedly compare the (dividend >> bit) with divisor, with
        bit from [31, 0], whenever the left is bigger, we can subtract
        (divisor << bit) from dividend, and add (1 << bit) to the result.

        Note that we need to deal with overflow as a special case.
        '''
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(31, -1, -1):
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (dividend > 0) == (divisor > 0) else -res