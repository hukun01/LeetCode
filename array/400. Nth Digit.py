# 400. Nth Digit
class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        1. Find the x-th interval that the n-th digit falls into;
        2. Find the number and position of the digit.

        The first interval is [1, 9] with length 9, the second one is [10, 99] with length 90,
        the xth interval is [start, start + length - 1] with length 9 * start, and start = 10**(x - 1).
        '''
        n -= 1
        for digits in range(1, 11):
            start = 10 ** (digits - 1)
            if n < 9 * start * digits:
                return int(str(start + n // digits)[n % digits])
            n -= 9 * start * digits