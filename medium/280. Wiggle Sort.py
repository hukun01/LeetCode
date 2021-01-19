# 280. Wiggle Sort
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        If i is even, we want it to be smaller than its neighboars, so 
        if nums[i] <= nums[i + 1], we are good. Otherwise, nums[i] > nums[i + 1],
        we swap them, and now i-th is smaller. And we already ensure that the
        previous i-th <= (i - 1)th, since now i-th is further smaller,
        it will still be smaller than (i - 1)th.

        Similar logic applies to the case when i is odd.

        Time: O(n) where n is len(nums)
        Space: O(1)
        '''
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]