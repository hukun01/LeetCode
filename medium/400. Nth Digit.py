# 400. Nth Digit
class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        1. Find the x-th bucket that the n-th digit falls into;
        2. Find the number and position of the digit.

        The first bucket is [1, 9] with length 9,
        the second one is [10, 99] with length 90,...

        The x-th bucket is [start, start + bucket)
        with bucket = 9 * start * x, and start = 10**(x - 1).
        '''
        n -= 1
        for digits in range(1, 11):
            start = 10 ** (digits - 1)
            bucket = 9 * start * digits
            if n < bucket:
                return int(str(start + n // digits)[n % digits])
            n -= bucket
        '''
        Another implementation.
        '''
        n -= 1
        base = 1
        block_size = 9
        digits = 1
        total_digits = 0
        while n > total_digits + block_size * digits:
            total_digits += block_size * digits
            digits += 1
            base += block_size
            block_size *= 10
        k = n - total_digits
        num_idx = k // digits
        digit_idx = k % digits
        return str(base + num_idx)[digit_idx]