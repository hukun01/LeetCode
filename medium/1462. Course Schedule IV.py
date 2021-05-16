# 1462. Course Schedule IV
class Solution:
    def checkIfPrerequisite(self, n: int, P: List[List[int]], Q: List[List[int]]) -> List[bool]:
        '''
        1/3 DFS
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
        2/3 Floyd-Marshall algorithm.
        '''
        graph = [[False] * n for _ in range(n)]
        for a in range(n):
            graph[a][a] = True
        for a, b in P:
            graph[a][b] = True
        for c in range(n):
            for a in range(n):
                for b in range(n):
                    graph[a][b] = graph[a][b] or (graph[a][c] and graph[c][b])
        ans = []
        for a, b in Q:
            ans.append(graph[a][b])
        return ans
        '''
        3/3 Topological sort in BFS style.
        Do a topological sort, during which we collect the prerequisites set
        for each node.

        Time: O(np) where p is the average number of prerequisites for a node.
        Space: O(n^2)
        '''
        graph = defaultdict(list)
        in_degree = [0] * n
        pres = [set() for _ in range(n)]
        for a, b in P:
            graph[a].append(b)
            in_degree[b] += 1
            pres[b].add(a)
        queue = deque(b for b, degree in enumerate(in_degree)
                      if degree == 0)
        while queue:
            a = queue.popleft()
            for b in graph[a]:
                pres[b] |= pres[a]
                in_degree[b] -= 1
                if in_degree[b] == 0:
                    queue.append(b)
        return [a in pres[b] for a, b in Q]