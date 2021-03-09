# 1462. Course Schedule IV
class Solution:
    def checkIfPrerequisite(self, n: int, P: List[List[int]], Q: List[List[int]]) -> List[bool]:
        '''
        1/2 DFS
        Build a graph with each prereq mapping to its next.
        DFS from node a and see if b is one of its nexts, or its next's next.
        '''
        next_nodes = defaultdict(list)
        for a, b in P:
            next_nodes[a].append(b)

        @cache
        def dfs(start, end):
            if start == end:
                return True
            return any(dfs(nex, end) for nex in next_nodes[start])
        return [dfs(a, b) for a, b in Q]
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