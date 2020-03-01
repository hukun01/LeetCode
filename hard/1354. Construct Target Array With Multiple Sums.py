# 1354. Construct Target Array With Multiple Sums
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        '''
        Similar to 780. Reaching Points.

        '''
        total = sum(target)
        heap = [-t for t in target]
        heapq.heapify(heap)
        while True:
            a = -heapq.heappop(heap)
            if a == 1:
                return True
            total -= a
            if a <= total:
                return False
            a %= total
            total += a
            heapq.heappush(heap, -a)