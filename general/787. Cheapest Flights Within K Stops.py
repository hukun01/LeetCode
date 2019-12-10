class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        We start from src and try to 'go back' to dst. 
        
        Use a heap to store (price, city, stepsLeft), if stepsLeft == 0, we can't continue from this city.
        We may reach dst early with a higher price, we would keep it in the heap,
        and still explore the other cheaper options first within the stepsLeft.
        Hence, when we get to the dst, we know the price is the lowest one.
        '''
        edges = collections.defaultdict(dict)
        for c1, c2, price in flights:
            edges[c1][c2] = price
        heap = [(0, src, K + 1)]
        while heap:
            price, city, k = heapq.heappop(heap)
            if city == dst:
                return price
            if k > 0:
                for nextCity in edges[city]:
                    heapq.heappush(heap, (price + edges[city][nextCity], nextCity, k - 1))
        return -1