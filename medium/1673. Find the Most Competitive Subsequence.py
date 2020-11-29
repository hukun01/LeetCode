# 1673. Find the Most Competitive Subsequence
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        Greedy with Conditional Mono Stack.
        Identical to 402. Remove K Digits.
        '''
        stack = []
        n = len(nums)
        for i, a in enumerate(nums):
            while stack and stack[-1] > a and len(stack) - 1 + n - i >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(a)
        return stack