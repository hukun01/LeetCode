class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        '''
        A price is the wage/quality ratio, note that it's per quality unit.
        
        We pay each worker based on his price or a bigger one, so we want to start trying 
        every price * totalQuality, and we want to start trying from the min price, so that
        the wage automatically becomes higher than or equal to a worker's expectation. So we
        need to sort the (price, workerQuality) pair.
        
        We start from the min price, and as we move to the next price, we pay more overall.
        We maintain a max heap of quality (use negative quality with Python's min heap), 
        because when we move to a worker with higher price, his total wage can be lower,
        comparing to a previous worker with very high quality and not so high price.
        So we remove the highest quality when we have more than K candidates.
        If we have exactly K workers, we get the total wages by the qualitySum * currentPrice.
        '''
        pricesAndQualities = sorted([w / q, q] for w, q in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for price, q in pricesAndQualities:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * price)
        return res