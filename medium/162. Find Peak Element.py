class Solution:
    def findPeakElement(self, nums):
        '''
        Binary search.
        Find mid, if mid is in a descending region, peak is in the left half;
        if mid in a ascending region, peak is in right half.
        '''
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[m + 1]:
                h = m
            else:
                l = m + 1
        return l
