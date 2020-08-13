# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        Fenwick tree, Binary Indexed Tree (BIT).
        '''
        deltas = [0] * (n+1)
        for i, j, k in bookings:
            deltas[i-1] += k
            deltas[j]   -= k

        return [*itertools.accumulate(deltas[:-1])]