# 399. Evaluate Division
class Solution:    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        1/3 Using DFS
        To build the graph, encode each directed edge with (nextId, val) and
        reversed edge in a dict.
        Then do a DFS on the graph to find the path from a -> b.
        '''
        graph = defaultdict(set)
        for i in range(len(equations)):
            a, b = equations[i]
            edgeAtoB = (b, values[i])
            graph[a].add(edgeAtoB)
            edgeBtoA = (a, 1 / values[i])
            graph[b].add(edgeBtoA)

        def dfs(a, b, currVal, visitedNodes):
            for edge in graph[a]:
                if a == b:
                    return currVal
                nextNode, val = edge
                if nextNode in visitedNodes:
                    continue
                visitedNodes.add(nextNode)
                myVal = dfs(nextNode, b, currVal * val, visitedNodes)
                if myVal != -1.0:
                    return myVal
            return -1.0

        ans = []
        for query in queries:
            a, b = query
            ans.append(dfs(a, b, 1.0, set([a])))
            
        return ans
        '''
        2/3 Using Union Find
        '''
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = (x, 1.0)
            if parent[x][0] != x:
                p, v = parent[x]
                p0, v0 = find(p)
                '''
                x/p = v
                p/p0 = v0
                x/p0 = x/p * p/p0 = v * v0
                '''
                parent[x] = (p0, v * v0)
            return parent[x]

        def union(x, y, v):
            x0, v0 = find(x)
            y0, v1 = find(y)
            if x0 == y0:
                return
            '''
            x, x0
            x/x0 = v0
            
            y, y0
            y/y0 = v1

            x/y  = v
            y0/x0= ((x/x0) / (y/y0)) / (x/y)
                 = v0 / v1 / v
            '''
            parent[y0] = (x0, v0 / v1 / v)
        
        for (x, y), v in zip(equations, values):
            union(x, y, v)
        
        ans = []
        for x, y in queries:
            if x not in parent or y not in parent:
                ans.append(-1)
                continue
            x0, v0 = find(x)
            y0, v1 = find(y)
            if x0 != y0:
                ans.append(-1)
            else:
                # x / x0 = v0
                # y / y0 = v1
                # x / y = ?
                # (x / x0) / (y / y0) = (x / y) * (y0 / x0) = v0 / v1
                # x0 == y0
                ans.append(v0 / v1)
        return ans
        '''
        3/3 Floyd-Warshall.
        '''
        a_over_b = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            a_over_b[a][a] = a_over_b[b][b] = 1.0
            a_over_b[a][b] = val
            a_over_b[b][a] = 1 / val
        for k in a_over_b:
            for i in a_over_b[k]:
                for j in a_over_b[k]:
                    a_over_b[i][j] = a_over_b[i][k] * a_over_b[k][j]
        return [a_over_b[a].get(b, -1.0) for a, b in queries]