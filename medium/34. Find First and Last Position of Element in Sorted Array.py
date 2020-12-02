# 34. Find First and Last Position of Element in Sorted Array
class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Binary search.
        Use one function - find inclusive lower bound - to find {target}, and
        {target + 1}, then its [index1, index2 - 1], if index1 exists.

        Can also use bisect_left and bisect_right.

        Time: O(n log(n)), where n is len(nums)
        Space: O(1)
        """
        def inclusiveLowerBound(target):
            l, h = 0, len(nums)
            while l < h:
                m = (l + h) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    h = m
            return l
        start = inclusiveLowerBound(target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, inclusiveLowerBound(target + 1) - 1]