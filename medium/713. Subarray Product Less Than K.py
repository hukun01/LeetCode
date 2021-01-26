# 713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Sliding window.
        Maintain a window, in which the number of good subarrays are defined
        by (right - left + 1), meaning all the subarrays ending at nums[right].
        Keep shrinking the window by moving left index to right, if the product
        is too big. Note that we also need to ensure left <= right in case k is
        smaller than any number and the product is always too big.

        A critical condition for this to work is that all nums are positive,
        otherwise we hit divide-by-zero error when moving left index.

        Time: O(n) where n is len(nums)
        Space: O(1)
        '''
        ans = left = 0
        cur_product = 1
        for right, a in enumerate(nums):
            cur_product *= a
            while left <= right and cur_product >= k:
                cur_product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans