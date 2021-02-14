# 787. Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        Dijkstra.

        Use a heap to store (price, city, stepsLeft), if stepsLeft == 0, we
        can't continue from this city.
        We may reach dst early with a higher price, we would keep it in the
        heap, and still explore the other cheaper options first within the
        stepsLeft. Hence, when we get to the dst, we know the price is the
        lowest one.

        Time: O(n log(n))
        Space: O(n)
        '''
        maps = defaultdict(list)
        for city, nextCity, price in flights:
            maps[city].append((price, nextCity))
        trips = [(0, src, K + 1)]
        while trips:
            cost, city, hops = heappop(trips)
            if city == dst:
                return cost
            if hops > 0:
                for price, nextCity in maps[city]:
                    heappush(trips, (cost + price, nextCity, hops - 1))
        return -1