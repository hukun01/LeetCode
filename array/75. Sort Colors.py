class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # when seeing 0, move it to head, when seeing 2 move it to tail, keep 1 there
        i, head, tail = 0, 0, len(nums)-1
        while i <= tail:
            if nums[i] == 0:
                nums[i], nums[head] = nums[head], nums[i]
                head += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1
            else:
                i += 1