class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
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