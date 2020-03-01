class Solution:
    def findMin(self, nums):
        """
        Keywords: sorted.

        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            # compare middle with h instead of l to avoid stuck due to round-down
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        
        return nums[l]