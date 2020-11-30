# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        Difference array.
        This is the inverse of prefix sums:  diff[i] = nums[i] - nums[i - 1].
        Based on this we know: 
            1. nums[i] = diff[i] + nums[i - 1]
            2. nums[0] = diff[0]
        Then we can get nums by accumulating diff.
        Difference array provides O(1) update to any intervals in an array,
        with the cost of O(n) query. Hence, this technique is often used in
        scenarios where frequent update operations are applied to various
        intervals. And our goal is to get the result array AFTER all the
        operations.

        Time: O(n)
        Space: O(n)
        '''
        diff = [0] * (n+1)
        for i, j, k in bookings:
            diff[i-1] += k
            diff[j]   -= k

        return list(itertools.accumulate(diff[:-1]))