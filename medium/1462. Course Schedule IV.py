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
        '''
        3/3 Topological sort.


        Time: O(np) where p is the average number of prerequisites for a node.
        Space: O(n^2)
        '''
        graph = defaultdict(list)
        in_degree = [0] * n
        pres = [set() for _ in range(n)]
        for pre, course in P:
            graph[pre].append(course)
            in_degree[course] += 1
            pres[course].add(pre)
        queue = deque(course for course, degree in enumerate(in_degree)
                      if degree == 0)
        while queue:
            pre = queue.popleft()
            for course in graph[pre]:
                pres[course] |= pres[pre]
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)
        return [pre in pres[course] for pre, course in Q]