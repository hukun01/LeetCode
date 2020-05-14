# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        '''
        Sliding window.
        This problem is simple because all numbers are positive. We can start
        shrinking the window from its left side once we reach s in the total,
        because the total is monotonically growing as we move to the right.
        And shrinking left is a way of exploring the possibilities of dropping smaller
        numbers from left that would still keep the total above s.
        '''
        ans = math.inf
        total = 0
        w = deque()
        for a in nums:
            w.append(a)
            total += a
            while total >= s:
                ans = min(ans, len(w))
                total -= w.popleft()
        return 0 if math.isinf(ans) else ans