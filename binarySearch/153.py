class Solution:
    def findMin(self, nums):
        """
        Keywords: sorted.

        :type nums: List[int]
        :rtype: int
        """
        iMin, iMax = 0, len(nums) - 1
        while iMin < iMax:
            i = (iMin + iMax) // 2
            # compare middle with iMax instead of iMin to avoid stuck due to round-down
            if nums[i] > nums[iMax]:
                iMin = i + 1
            else:
                iMax = i
        
        return nums[iMin]