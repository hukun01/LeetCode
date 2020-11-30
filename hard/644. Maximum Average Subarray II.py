# 644. Maximum Average Subarray II
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''
        Binary search + sliding window.
        Intuition on binary search:
        The range of averages is [min(nums), max(nums)], and whether an average
        can be supported is a monotonic function - if x can be supported, then
        all averages smaller than x can be supported as well. This means that
        binary search can be used on finding the max possible average in the
        range.
        Intuition on sliding window:
        To determine whether an average x can be supported by some subarray
        with at least k elements, we need to use a special sliding window that
        has two parts - 'curr' and 'prev'. These two sliding windows both
        record the sums of deltas (nums[i] - x). 'curr' is the current sliding
        window with at least k elements, ending at 'i', 'prev' is the previous
        sliding window. Initially, 'curr' covers [0, i], 'prev' covers
        [0, i - k]. If 'prev' is negative, that means its average is less than
        x, so we can remove it from 'curr', and reset 'prev' to 0. Whenever
        'curr' is positive, we have a good subarray whose average is above x.

        Time: O(nlog(m)) where n is the length of nums, m is the difference
        between min(nums) and max(nums).
        Space: O(1)
        '''
        def has_avg_above(x):
            '''
            Check whether there's a subarray whose average is bigger than
            'avg', and with at least k elements.
            '''
            curr = sum(nums[:k]) - k * x
            if curr >= 0:
                return True
            prev = 0
            for i in range(k, len(nums)):
                curr += nums[i] - x
                prev += nums[i - k] - x
                if prev < 0:
                    curr -= prev
                    prev = 0
                if curr >= 0:
                    return True
            return False

        l, h = min(nums), max(nums)
        while h - l >= 1e-5:
            m = (l + h) / 2
            if has_avg_above(m):
                l = m
            else:
                h = m
        return l