# 1928. Minimum Cost to Reach Destination in Time
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        '''
        Dijkstra with pruning.

        Usually in Dijkstra problems, we look for shortest distance. In this
        problem, the goal is 2-dimensional: min cost, and shortest distance.
        Getting the min cost has a higher priority, and distance (time) has a
        hard limit that can't be exceeded.

        Initially I put (cur_cost, cur_time, city) to the priority queue, but
        this results in lots of repeated access to the same cities if the cost
        to them is small. But this doesn't help get to the target.

        Instead, I should put (cur_time, cur_cost, city) to the priority queue,
        and just find all the paths that can be done within the time limit, in
        the meantime, keep track of the min_costs to reach each city. And if
        the current cost is >= min_cost, we don't need to explore more from
        this city.
        '''
        n = len(passingFees)
        graph = defaultdict(list)
        for a, b, time in edges:
            graph[a].append((b, time))
            graph[b].append((a, time))

        min_costs = [inf] * n

        pq = [[0, passingFees[0], 0]]
        while pq:
            cur_time, cur_cost, city = heappop(pq)
            if cur_cost >= min_costs[city]: continue
            min_costs[city] = cur_cost

            for nex_city, time in graph[city]:
                if cur_time + time <= maxTime:
                    heappush(pq, [cur_time + time, min_costs[city] + passingFees[nex_city], nex_city])

        return -1 if min_costs[n - 1] == inf else min_costs[n - 1]