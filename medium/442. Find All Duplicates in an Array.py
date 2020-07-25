# 442. Find All Duplicates in an Array
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        Use nums[idx] to store the count of number with value (idx+1).
        0 means the number is used, use negative count to avoid conflict
        with actual values.
        '''
        i = -1
        while (i := i + 1) < len(nums):
            pos = nums[i] - 1
            if pos < 0:
                continue
            if nums[pos] <= 0:
                nums[pos] -= 1
                nums[i] = 0
            else:
                nums[i], nums[pos] = nums[pos], -1
                i -= 1
        return [i + 1 for i, n in enumerate(nums) if n == -2]