class Solution(object):
    def searchRange(self, nums, target):
        """
        Use one function - find lower bound - to find {target}, and {target + 1},
        then its [index1, index2 - 1], if index1 exists.

        Can also use bisect.bisect_left and bisect.bisect_right.

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findLowerBound(nums, target):
            l, h = 0, len(nums)
            while l < h:
                m = (h + l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    h = m
            return l
        
        start = findLowerBound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        # if target + 1 would cause overflow, we just handle it as a special case
        return [start, findLowerBound(nums, target + 1) - 1]