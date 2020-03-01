class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        It uses three indices i, j and k, maintaining the invariant that i <= j.
        j is the position of the number under consideration. And i is the boundary for the numbers less than the mid value.
        k holds the lower boundary of numbers greater than mid.
        '''
        i = j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1