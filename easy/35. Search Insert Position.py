class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
        A key is to set h to be len(nums), because the insertion position can be
        the array tail.
        '''
        l = 0
        h = len(nums)
        while l < h:
            m = (l+h)//2
            if target > nums[m]:
                l = m + 1
            else: 
                h = m
        return l
