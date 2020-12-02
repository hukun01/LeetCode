# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        Difference array.

        Time: O(n)
        Space: O(n)

        Same as 370. Range Addition.
        '''
        diff = [0] * (n+1)
        for i, j, k in bookings:
            diff[i-1] += k
            diff[j]   -= k

        return list(accumulate(diff[:-1]))