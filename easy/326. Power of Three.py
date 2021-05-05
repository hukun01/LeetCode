# 326. Power of Three
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        Math.

        A naive way is to do math.log(n, base=3), and check whether the result
        is an integer. However, we need to be careful with the returned
        floating number, and compare within some epsilon. Also, log()
        implementation varies per language so does its performance.

        A better way as below.
        In a 32-bit signed integer, the max is 2^31-1. Within this bound, the
        max power of three is 3^19 (=1162261467), so the possible power of
        three numbers are 3^0, 3^1, ..., 3^19.
        Since 3 is a prime number, the above candidates are the same as the
        divisors of 3^19. Thus, we just need to check n > 0 and 3^19 % n == 0.
        Note that this is the same as the naive log() way, but without floating
        number issue.

        This works for any prime number, not just 3.

        Time: O(1)
        Space: O(1)
        '''
        return n > 0 and 1162261467 % n == 0