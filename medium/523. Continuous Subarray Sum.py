# 523. Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        When iterating the array, we don't have to check every possible
        subarray sums.
        Based on modulus attribute: (x + n*k) % k = x,
        in which x can be 0, 1, ..., k-1.
        When we see x in 'seen', our target must be (x + n*k) because
        it is monotonically increasing.

        Note that we need to check the existing sum's last index, in order
        to determine whether the subarray has at least 2 elements.
        '''
        seen = { 0: -1 }
        runningSum = 0
        for i, n in enumerate(nums):
            runningSum += n
            if k != 0:
                runningSum %= k
            if runningSum in seen:
                if i - seen[runningSum] > 1:
                    return True
            else:
                seen[runningSum] = i
        return False