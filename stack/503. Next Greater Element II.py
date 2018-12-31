class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        Similar to 496. Next Greater Element I, 
        but here we don't need a dict, and we store the index in the stack. 
        Same as 739. Daily Temperatures.
        """
        stack = []
        ans = [-1 for n in nums]
        for i in range(len(nums) * 2):
            i = i % len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                ans[idx] = nums[i]
            stack.append(i)
        return ans