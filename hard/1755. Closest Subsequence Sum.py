# 1755. Closest Subsequence Sum
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        '''
        Meet in the middle.
        A straightforward brute force is to try every possible subset sum, and
        use O(2^n) time where n is len(nums). In this problem n is up to 40, so
        2^40 will TLE.
        Similar to 2-end BFS, if we cut the input array in half, and find
        subset sums for the two halves, then each take 2^(n/2) time, up to
        2^20, and the rest is to combine the 2 results.

        Combine: we sort the first half result, and iterate through the second
        half, for each subset sum 'a' in the second half, we binary search the
        first half to find the value closest to 'goal - a', and record the min
        absolute difference. This takes O(n log(n)) time, dominated by the
        subset finding time O(2^(n/2)).

        Time: O(2^(n/2))
        Space: O(2^(n/2))
        '''

        def get_subset_sums(arr):
            sums = {0}
            for a in arr:
                sums |= {a + b for b in sums}
            return sums

        ans = abs(goal)

        mid = len(nums) // 2
        sums_left = sorted(get_subset_sums(nums[:mid]))
        sums_right = get_subset_sums(nums[mid:])
        for a in sums_right:
            remain = goal - a
            i = bisect_left(sums_left, remain)
            if i < len(sums_left):
                ans = min(ans, abs(remain - sums_left[i]))
            ans = min(ans, abs(remain - sums_left[i - 1]))

        return ans