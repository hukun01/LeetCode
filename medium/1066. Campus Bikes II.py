class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        1/2 State compression DP.
        Use a dp(w_i, used_bikes) to represent the assignment up to w_i and
        taken bikes represented by bits.
        For each w_i, iterate through all available bikes.

        Time: O(W 2^B) where W is len(workers), B is len(bikes)
        Space: O(W 2^B)
        '''
        dist = lambda w, b: abs(w[0] - b[0]) + abs(w[1] - b[1])

        @lru_cache(None)
        def dfs(w_i, used_bikes):
            if w_i == len(workers):
                return 0
            ans = inf
            for b_i in range(len(bikes)):
                if (new_used_bikes := used_bikes | (1 << b_i)) != used_bikes:
                    new_dist = dist(workers[w_i], bikes[b_i])
                    ans = min(ans, new_dist + dfs(w_i + 1, new_used_bikes))
            return ans
        return dfs(0, 0)
        '''
        2/2 Priority queue.
        Similar to above idea. We treat (w_i, used_bikes) as a node in the
        graph, and use dijkstra's algorithm to find the shortest path(sum).

        The key is to have a seen set to avoid going down the same search
        paths that were seen before.

        Time: O(W 2^B log(B!/(B-W)!)) where log(B!/(B-W)!) is the worst case
              of the priority queue size. Note that as B <= 10, log(B!) < 7.
              We also return early, so the actual time is much better.
        Space: O(W 2^B)
        '''
        dist = lambda w, b: abs(w[0] - b[0]) + abs(w[1] - b[1])
        pq = [(0, 0, 0)] # sum, w_i, used_bikes
        B = len(bikes)
        W = len(workers)
        seen = set()
        while pq:
            dist_sum, w_i, used_bikes = heappop(pq)
            if w_i == W:
                return dist_sum
            if (w_i, used_bikes) in seen:
                continue
            seen.add((w_i, used_bikes))
            for b_i in range(B):
                if (new_used_bikes := used_bikes | (1 << b_i)) != used_bikes:
                    new_dist = dist(workers[w_i], bikes[b_i])
                    heappush(pq, (dist_sum + new_dist, w_i + 1, new_used_bikes))