# 503. Next Greater Element II
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        Similar to 496. Next Greater Element I, 
        but here we don't need a dict, and we store the index in the stack. 
        Same as 739. Daily Temperatures.
        '''
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(1, n*2):
            actualIdx = i % n
            while stack and nums[stack[-1]] < nums[actualIdx]:
                ans[stack[-1]] = nums[actualIdx]
                stack.pop()
            stack.append(actualIdx)
        return ans