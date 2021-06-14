# 857. Minimum Cost to Hire K Workers
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        '''
        Greedy + Heap.
        A price is the wage/quality ratio, note that it's per quality unit.
        
        We pay each worker based on his price or a bigger one, the total cost
        is price * totalQuality, so we try prices from the min price. As the
        price goes up, the wage automatically becomes higher than or equal to
        all previous workers' expectation. So we need to sort the
        (price, workerQuality).

        Every worker has his price, we must increase our price to match the
        next worker, when we try to add him to the group.
        We maintain a max heap of quality (use negative quality with Python's
        min heap), because when we move to a worker with higher price, his
        total cost can be lower, comparing to a previous worker with very high
        quality and not so high price (which is updated to the higher price).
        So we remove the highest quality when we have more than K candidates.
        If we have exactly K workers, we get the total wages by the totalQuality * price.

        Time: O(n log(n)) where n is len(wage)
        Space: O(n)
        '''
        prices_qualities = sorted([w / q, q] for w, q in zip(wage, quality))
        ans = inf
        qSum = 0
        qHeap = []
        for price, q in prices_qualities:
            heappush(qHeap, -q)
            qSum += q
            if len(qHeap) > K:
                qSum += heappop(qHeap)
            if len(qHeap) == K:
                ans = min(ans, qSum * price)
        return ans