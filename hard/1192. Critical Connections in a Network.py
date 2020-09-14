# 1192. Critical Connections in a Network
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Tarjan's algorithm.
        '''
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        level = [0] * n

        def dfs(node, par=None, d=1):
            level[node] = d
            for nei in graph[node]:
                if nei == par:
                    continue
                if level[nei] == 0:
                    dfs(nei, node, d + 1)
                level[node] = min(level[node], level[nei])
            if par is not None and level[node] == d:
                self.ans.append((par, node))

        self.ans = []
        dfs(0)
        return self.ans