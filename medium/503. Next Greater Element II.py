# 503. Next Greater Element II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        Monotonic non-increasing stack.

        Similar to 496. Next Greater Element I, 
        but here we don't need a dict, and we store the index in the stack. 
        Same as 739. Daily Temperatures.
        '''
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n):
            actual_i = i % n
            while stack and nums[stack[-1]] < nums[actual_i]:
                ans[stack.pop()] = nums[actual_i]
            stack.append(actual_i)

        return ans