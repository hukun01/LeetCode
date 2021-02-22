# 882. Reachable Nodes In Subdivided Graph
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        '''
        Dijkstra.
        From each node we want to reach as far as possible. Hence, we want to
        use less moves, aka, find the shortest path.
        The connection points 'con' on each edge is like the weight or cost to
        pass that edge. In a weighted graph, Dijkstra can find the shortest
        path.
        Note that we need to cover the overlapped connection points from two
        sides of an edge, so we keep the leftover moves *from each node, and
        in the final step, we add the leftover moves from left and right nodes,
        but only count in at most 'con' nodes.

        Time: O(E log V)
        Space: O(E + V)
        '''
        graph = defaultdict(dict)
        for a, b, con in edges:
            graph[a][b] = graph[b][a] = con

        pq = [(-maxMoves, 0)]
        seen = Counter()
        while pq:
            moves_left, node = heappop(pq)
            moves_left = -moves_left

            if node in seen:
                continue

            seen[node] = moves_left

            for nex in graph[node]:
                con = graph[node][nex]
                if moves_left > con and nex not in seen:
                    heappush(pq, (-(moves_left - con - 1), nex))

        ans = len(seen)
        for a, b, con in edges:
            ans += min(seen[a] + seen[b], con)

        return ans