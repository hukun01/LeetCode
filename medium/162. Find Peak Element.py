class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if m + 1 == len(nums):
                return m
            if nums[m] > nums[m + 1]:
                # go left
                h = m
            else: # nums[m] < nums[m + 1]
                # go right
                l = m + 1
        return l