# 33. Search in Rotated Sorted Array
class Solution(object):
    def search(self, nums: List[int], target: int) -> int:
        '''
        1/2 Binary Search
        Use infinity to mask the side we don't need to check.
        Let's say nums looks like this: [12, 13, 14, 15, 0, 1, 2, 3].
        If target is let's say 14, then we adjust nums to this, where "inf" means infinity:
        [12, 13, 14, 15, inf, inf, inf, inf]

        If target is let's say 2, then we adjust nums to this:
        [-inf, -inf, -inf, -inf, 0, 1, 2, 3]
        '''
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
        '''
        2/2 Binary Search another style.
        We are trying to check if target is in [l, h], by checking below.
        First check whether target == nums[m], if so we are done.

        If the [l, m] is sorted:
            if target is in [l, m), make h = m - 1;
            else make l = m + 1.
        Otherwise, [m, h] must be sorted:
            if target is in (m, h], make l = m + 1;
            else make h = m - 1.
        '''
        l, h = 0, len(nums) - 1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    h = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[h]:
                    l = m + 1
                else:
                    h = m - 1
        return -1