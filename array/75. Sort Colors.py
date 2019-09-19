class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # when seeing 0, move it to head, when seeing 2 move it to tail, keep 1 there
        head, tail = 0, len(nums)-1
        for i in range(len(nums)):
            while nums[i] == 2 and i < tail:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
            if nums[i] == 0 and head < len(nums):
                nums[i], nums[head] = nums[head], nums[i]
                head += 1