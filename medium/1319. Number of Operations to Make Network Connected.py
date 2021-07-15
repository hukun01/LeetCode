# 1319. Number of Operations to Make Network Connected
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        '''
        1/2 Count the number of connected components in the graph

        To connect n machines together, we need at least n-1 cables.
        Hence if we have n-1 or more connections, we are guaranteed to find an
        answer.
        Use Union Find to find the number of connected components X, and the
        number of cables will be X - 1.
        Hence the key is to find out the number of connected components in the graph.
        '''
        if len(connections) < n - 1:
            return -1

        uf = list(range(n))
        def find(a):
            if uf[a] != a:
                uf[a] = find(uf[a])
            return uf[a]
        for c1, c2 in connections:
            p1 = find(c1)
            p2 = find(c2)
            uf[p1] = p2
        roots = [find(i) for i in range(n)]
        return len(set(roots)) - 1

        '''
        2/2 Similar logic can be done by DFS.
        '''
        if len(connections) < n - 1:
            return -1

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