# 29. Divide Two Integers
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        1/2 Repeated Exponential Searches.

        The quotient is the number of times we can substract the divisor from
        the dividend.
        From each 

        Time: O(log(n)) where n is length of integers.
        Space: O(1)
        '''
        edge = 1 << 31
        if dividend == -edge and divisor == -1:
            return edge-1

        a, b, ans = abs(dividend), abs(divisor), 0

        # Find the max bit we can possible shift divisor, this is to prevent
        # (b << bit) from exceeding 2**31.
        max_bits = 0
        a0 = a
        b0 = b
        while a0 >= b0:
            max_bits += 1
            b0 <<= 1

        for bit in range(max_bits - 1, -1, -1):
            if a >= (b << bit): # a >= b * 2^bit
                ans += 1 << bit
                a -= b << bit

        return ans if (dividend > 0) == (divisor > 0) else -ans
        '''
        2/2 Exponential search (similar to binary search).

        This only works with the given condition of truncation.
        Repeatedly compare the (dividend >> bit) with divisor, with
        bit from [31, 0], whenever the left is bigger, we can subtract
        (divisor << bit) from dividend, and add (1 << bit) to the result.

        Time: O(log(n)) where n is length of integers.
        Space: O(1)
        '''
        edge = 1 << 31
        if dividend == -edge and divisor == -1:
            return edge-1

        a, b, ans = abs(dividend), abs(divisor), 0
        for bit in range(31, -1, -1):
            if (a >> bit) >= b: # a/2^bit >= b
                ans += 1 << bit
                a -= b << bit

        return ans if (dividend > 0) == (divisor > 0) else -ans