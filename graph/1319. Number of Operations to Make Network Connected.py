# 1319. Number of Operations to Make Network Connected
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        1/2 Count the number of connected components in the graph

        To connect two networks, we need one cable.
        Find the #1 of connected networks, the operation count is (#1 - 1).
        Hence the key is to find out the number of connected components in the graph.
        '''
        if len(connections) < n - 1:
            return -1
        # otherwise, there must be an answer, because the connections count >=
        # the biggest possible number of connected components in the graph.
        graph = collections.defaultdict(set)
        for c1, c2 in connections:
            graph[c1].add(c2)
            graph[c2].add(c1)
        
        seen = set()
        def dfs(c):
            if c in seen:
                return 0
            seen.add(c)
            for neighbor in graph[c]:
                dfs(neighbor)
            return 1
        return sum(dfs(c) for c in range(n)) - 1

        '''
        2/2 Count the number of connected components and extra edges with Union Find.
        '''
        parents = list(range(n))
        def findParent(c):
            if c != parents[c]:
                parents[c] = findParent(parents[c]) # path compression
            return parents[c]

        extraEdgeCount = 0
        for c1, c2 in connections:
            p1 = findParent(c1)
            p2 = findParent(c2)
            if p1 == p2:
                extraEdgeCount += 1
            else:
                parents[p1] = p2

        connectedNetworkCount = sum(parents[c] == c for c in range(n))
        if extraEdgeCount < connectedNetworkCount - 1:
            return -1
        return connectedNetworkCount - 1