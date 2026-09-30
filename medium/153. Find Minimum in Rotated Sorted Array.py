class Solution:
    def findMin(self, nums: list[int]) -> int:
        '''
        Binary search.

        The input array is either fully sorted, or split into two sorted parts.
        
        1. If the mid is larger than the high, then the rotation point is
        at the right, so we set l = m + 1.
        2. If the mid is lower than the high, it can mean two cases:
            2a. there's no rotation at the left, the min is the low, aka, in [l, m];
            2b. the rotation is at the left, the min is somewhere in [l, m].
            So we can set h = m.
        '''
        l = 0
        h = len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] <= nums[h]:
                h = m
            else:
                l = m + 1

        return nums[l]
