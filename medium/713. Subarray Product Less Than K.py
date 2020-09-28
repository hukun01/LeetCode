# 713. Subarray Product Less Than K
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Sliding window.
        Maintain a window, in which the number of good subarrays are defined
        by (right - left + 1), meaning all the subarrays ending at nums[right].
        Keep shrinking the window by moving left index to right, if the product
        is too big. Note that we also need to ensure left < right in case k is
        smaller than any number and the product is always too big.
        A critical condition for this to work is that all nums are positive,
        otherwise we hit divide-by-zero error when moving left index.
        '''
        ans = left = 0
        curr_product = 1
        for i, a in enumerate(nums):
            curr_product *= a
            while left <= i and curr_product >= k:
                curr_product //= nums[left]
                left += 1
            ans += i - left + 1
        return ans