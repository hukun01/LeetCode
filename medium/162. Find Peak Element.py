class Solution:
    def findPeakElement(self, nums):
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[m + 1]:
                h = m
            else:
                l = m + 1
        return l