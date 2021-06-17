# 787. Cheapest Flights Within K Stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
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
        graph = defaultdict(list)
        for city, next_city, price in flights:
            graph[city].append((next_city, price))

        trips = [(0, src, k + 1)]
        visited = set()
        while trips:
            cost, pos, stops = heappop(trips)
            if pos == dst:
                return cost
            if (pos, stops) in visited:
                continue
            visited.add((pos, stops))
            if stops == 0:
                continue
            for nex, price in graph[pos]:
                heappush(trips, (cost + price, nex, stops - 1))

        return -1