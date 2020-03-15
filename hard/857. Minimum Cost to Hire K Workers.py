# 857. Minimum Cost to Hire K Workers
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        '''
        A price is the wage/quality ratio, note that it's per quality unit.
        
        We pay each worker based on his price or a bigger one, so we want to start trying 
        every price * totalQuality, from the min price. As the price goes up, the wage
        automatically becomes higher than or equal to a worker's expectation. So we
        need to sort the (price, workerQuality) pair.

        Every worker has his price, we must increase our price to match the next worker,
        when we try to add him to the group.
        We maintain a max heap of quality (use negative quality with Python's min heap), 
        because when we move to a worker with higher price, his total wage can be lower,
        comparing to a previous worker with very high quality and not so high price.
        So we remove the highest quality when we have more than K candidates.
        If we have exactly K workers, we get the total wages by the qualitySum * currentPrice.
        '''
        pricesAndQualities = sorted([w / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qSum = 0
        qHeap = []
        for price, q in pricesAndQualities:
            heapq.heappush(qHeap, -q)
            qSum += q
            if len(qHeap) > K:
                qSum += heapq.heappop(qHeap)
            if len(qHeap) == K:
                res = min(res, qSum * price)
        return res