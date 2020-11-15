# 1658. Minimum Operations to Reduce X to Zero
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        '''
        Sliding window.
        This problem can be transformed into another: find the
        longest subarray whose sum is (total - x).
        We can use a sliding window to find the sizes of all
        windows whose sum is the target, then keep the max size.

        A key condition is that all numbers here are positive,
        otherwise the sliding window cannot grow with monotonically
        increasing sum.
        Time: O(n) where n is the size of the input array.
        Space: O(1)
        '''
        target = sum(nums) - x
        ans = -1
        left_idx = 0
        cur = 0
        for i, a in enumerate(nums):
            cur += a
            while left_idx <= i and cur > target:
                cur -= nums[left_idx]
                left_idx += 1
            if cur == target:
                ans = max(ans, i - left_idx + 1)
        return len(nums) - ans if ans != -1 else -1