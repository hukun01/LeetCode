# 1192. Critical Connections in a Network
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Tarjan's algorithm to find SCC (Strongly Connected Component).

        Since the edges are unidirectional, SCC here isn't the strict SCC in
        its original definition. Instead, SCC here is the component with a
        cycle, in other words, each node can reach others in at least 2 paths.

        The critical connections are the ones that are not part of any SCCs.
        We use Tarjan's algorithm to find SCCs, during this process, we can
        collect the edges that are not part of any SCCs.

        Time: O(E+V)
        Space: O(V)

        Video reference: https://www.youtube.com/watch?v=wUgWX0nc4NY
        '''
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        UNVISITED = -1
        depths = [UNVISITED] * n

        def dfs(node, par=None, d=0):
            depths[node] = d
            for nei in graph[node]:
                if nei == par:
                    continue
                if depths[nei] == UNVISITED:
                    dfs(nei, node, d + 1)
                depths[node] = min(depths[node], depths[nei])

            # We just found a SCC and current node is the start of it, now the
            # par-node connection is an edge external to this SCC, hence it's
            # critical.
            if depths[node] == d and par is not None:
                self.ans.append((par, node))

        self.ans = []
        dfs(0)
        return self.ans