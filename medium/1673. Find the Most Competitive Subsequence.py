# 1673. Find the Most Competitive Subsequence
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        '''
        Greedy with Conditional Mono Stack.
        Identical to 402. Remove K Digits.
        '''
        stack = []
        remove = len(nums) - k
        for a in nums:
            while stack and remove and stack[-1] > a:
                stack.pop()
                remove -= 1
            stack.append(a)
        return stack[:-remove] if remove else stack
