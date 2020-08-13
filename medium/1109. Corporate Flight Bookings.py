# 1109. Corporate Flight Bookings
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        '''
        Fenwick tree, Binary Indexed Tree (BIT).

        Similar to 307. Range Sum Query - Mutable
        '''
        deltas = [0] * (n+1)
        for i, j, k in bookings:
            deltas[i-1] += k
            deltas[j]   -= k

        return list(itertools.accumulate(deltas[:-1]))