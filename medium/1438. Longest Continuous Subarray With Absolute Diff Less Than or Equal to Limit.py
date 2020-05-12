# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        Use two sliding windows to record the max and min, when
        their diff is greater than limit, pop out the left side.
        '''
        ans = left = 0
        maxW = collections.deque() # maxW[0] tracks the max since 'left' index
        minW = collections.deque() # minW[0] tracks the min since 'left' index
        for right, a in enumerate(nums):
            # Note that in below 2 loops, only 1 will run in each iteration
            while maxW and maxW[-1] < a:
                maxW.pop()
            while minW and minW[-1] > a:
                minW.pop()
            maxW.append(a)
            minW.append(a)
            if maxW[0] - minW[0] > limit:
                if maxW[0] == nums[left]:
                    maxW.popleft()
                if minW[0] == nums[left]:
                    minW.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans