# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        It uses three indices i0, i1 and i2, maintaining the invariant that i1 <= i2.
        i1 is the position of the number under consideration. And i0 is the boundary for the numbers less than the mid value.
        i2 holds the lower boundary of numbers greater than mid.
        '''
        i2 = len(nums) - 1
        i0 = i1 = 0
        while i1 <= i2:
            if nums[i1] == 0:
                nums[i0], nums[i1] = nums[i1], nums[i0]
                i0 += 1
                i1 += 1
            elif nums[i1] == 1:
                i1 += 1
            elif nums[i1] == 2:
                nums[i2], nums[i1] = nums[i1], nums[i2]
                i2 -= 1