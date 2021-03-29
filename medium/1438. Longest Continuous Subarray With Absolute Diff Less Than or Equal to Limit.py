# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        Sliding windows.

        Use two sliding windows to record the max and min, when their diff is
        greater than limit, pop out the left side from both windows.

        Time: O(n) where n is len(nums)
        Space: O(n)
        '''
        max_q = deque()
        min_q = deque()
        left = ans = 0
        for right, a in enumerate(nums):
            while max_q and nums[max_q[-1]] <= a:
                max_q.pop()
            max_q.append(right)

            while min_q and nums[min_q[-1]] >= a:
                min_q.pop()
            min_q.append(right)

            if nums[max_q[0]] - nums[min_q[0]] > limit:
                if max_q[0] == left:
                    max_q.popleft()
                if min_q[0] == left:
                    min_q.popleft()
                left += 1

            ans = max(ans, right - left + 1)

        return ans