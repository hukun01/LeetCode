# 1462. Course Schedule IV
class Solution:
    def checkIfPrerequisite(self, n: int, P: List[List[int]], Q: List[List[int]]) -> List[bool]:
        '''
        1/2 DFS
        Build a graph with each node mapping to its prereqs.
        DFS from node i and see if j is one of its prereqs, or its prereq's prereq.
        '''
        graph = defaultdict(list)
        for i, j in P:
            graph[j].append(i)

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return True
            return any(dfs(x, j) for x in graph[i])
        return [dfs(j, i) for i, j in Q]
        '''
        2/2 Floyd-Marshall algorithm.
        '''
        graph = [[False] * n for _ in range(n)]
        for i in range(n):
            graph[i][i] = True
        for i, j in P:
            graph[i][j] = True
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
        ans = []
        for i, j in Q:
            ans.append(graph[i][j])
        return ans