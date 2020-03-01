# 33.Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        """
        Use infinity to mask the side we don't need to check.
        Let's say nums looks like this: [12, 13, 14, 15, 0, 1, 2, 3].
        If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
        [12, 13, 14, 15, inf, inf, inf, inf]

        If target is let's say 2, then we adjust nums to this:
        [-inf, -inf, -inf, -inf, 0, 1, 2, 3]
        """
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            # compare target to nums[0], and then compare mid to nums[0],
            # to determine if target and mid is on the same side (skewed or not).
            # temp is used to represent the inf or -inf as the boundary
            if target < nums[0]: 
                if nums[mid] < nums[0]: 
                    temp = nums[mid]
                else:
                    temp = -float('inf')
            elif target == nums[0]:
                return 0
            else: 
                if nums[mid] >= nums[0]: 
                    temp = nums[mid]
                else:
                    temp = float('inf')
            
            if temp < target:
                l = mid + 1
            elif temp > target: 
                h = mid -1 
            else:
                return mid
            
        return -1