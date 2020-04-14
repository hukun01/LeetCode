# 525. Contiguous Array
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Since there are only two possible values, we can keep track of
        a relative count, for example, the count of extra ones seen so far.
        If the count of extra ones in [:i] == that in [:j] inclusive,
        then in (i: j] there must be no extra ones, also, no extra zeros.
        And (i: j] would be a valid subarray.

        Note that to cover subarrays that start with 0th element, we need to
        initialize the count:index mapping with {0: -1}.
        '''
        seenCounts = { 0: -1 }
        ans = extraOnes = 0
        for i, n in enumerate(nums):
            if n == 1:
                extraOnes += 1
            else:
                extraOnes -= 1
            if extraOnes in seenCounts:
                ans = max(ans, i - seenCounts[extraOnes])
            else:
                seenCounts[extraOnes] = i
        return ans