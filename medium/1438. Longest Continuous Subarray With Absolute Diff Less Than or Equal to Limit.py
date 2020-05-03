# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        Use two sliding windows to record the max and min, when
        their diff is greater than limit, pop out the left side.
        '''
        maxW = collections.deque()
        minW = collections.deque()
        i = 0
        for j, a in enumerate(nums):
            while len(maxW) and a > maxW[-1]: maxW.pop()
            while len(minW) and a < minW[-1]: minW.pop()
            maxW.append(a)
            minW.append(a)
            if maxW[0] - minW[0] > limit:
                if maxW[0] == nums[i]: maxW.popleft()
                if minW[0] == nums[i]: minW.popleft()
                i += 1
        return len(nums) - i