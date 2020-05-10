# 137. Single Number II
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Since every number appears 3 times except for one, from the binary perspective,
        assumed 32 bits integer, every bit appears 3*n times, except for some bits that appear exactly once.
        Thus, treat this integer array as a bit matrix, each number is represented in binary form in each row,
        if we accumulate every bit vertically, and module each sum by 3, the result would be either 0 or 1.
        And 1 is one bit of the single number.

        Note that in Python, due to its arbitrary precision feature, negative numbers are represented differently
        than that in other languages like Java or C++. To handle this, we need to explicitly count the number of
        negatives to determine whether the single number is negative. And we need to handle all numbers using
        their absolute value.

        This solution can be generalized to solving the problem in which every number appears X times except one,
        which appears Y times.
        Again, one number in each row, then each column's bit sum is either nX or nX+Y. The rest is the same as above.
        '''
        negativeCount = sum(i <= 0 for i in nums)
        sign = -1 if negativeCount % 3 == 1 else 1
        ans = 0
        for i in range(32):
            bit = 0
            for n in nums:
                bit += (abs(n) >> i) & 1
            ans |= (bit % 3) << i
        return ans * sign