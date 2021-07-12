# 523. Continuous Subarray Sum
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        When iterating the array, we don't have to check every possible
        subarray sums.
        Based on modulus attribute: (x + n*k) % k = x,
        in which x can be 0, 1, ..., k-1.
        When we see x in 'seen', our target must be (x + n*k) because
        it is monotonically non-decreasing.

        Note that we need to check the existing sum's last index, in order
        to determine whether the subarray has at least 2 elements.
        '''
        seen = { 0: -1 }
        running_sum = 0
        for i, a in enumerate(nums):
            running_sum += a
            if k != 0:
                running_sum %= k
            if running_sum in seen:
                if i - seen[running_sum] > 1:
                    return True
            else:
                seen[running_sum] = i
        return False