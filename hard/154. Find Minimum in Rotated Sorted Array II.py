class Solution:
    def findMin(self, nums):
        """
        When nums[m] == nums[h], we don't know which side 
        the min could be in, so have to do a linear scan.

        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            elif nums[m] == nums[h]:
                break 
            else:
                h = m
        
        return min(nums[l:h+1])