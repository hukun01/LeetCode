class Solution:    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        1/2 Using DFS
        To build the graph, encode each directed edge with (nextId, val) and reversed edge in a dict.
        Then do a DFS on the graph to find the path from a -> b.
        '''
        maps = collections.defaultdict(set)
        for i in range(len(equations)):
            a, b = equations[i]
            edgeAtoB = (b, values[i])
            maps[a].add(edgeAtoB)
            edgeBtoA = (a, 1 / values[i])
            maps[b].add(edgeBtoA)
        
        def dfs(a, b, currVal, visitedNodes):
            for edge in maps[a]:
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
        2/2 Using Union Find
        '''
        uf = {}
        def find(a):
            if uf[a][0] != a:
                pA, vA = find(uf[a][0])
                uf[a] = (pA, uf[a][1] * vA)
            return uf[a]
        for (a, b), v in zip(equations, values):
            if a not in uf and b not in uf:
                uf[a] = (b, v)
                uf[b] = (b, 1.0)
            elif a not in uf:
                uf[a] = (b, v)
            elif b not in uf:
                uf[b] = (a, 1/v)
            else:
                pA, vA = find(a)
                pB, vB = find(b)
                uf[pA] = (pB, v * vB / vA)
        ans = []
        for a, b in queries:
            if a not in uf or b not in uf:
                ans.append(-1)
            else:
                pA, vA = find(a)
                pB, vB = find(b)
                if pA != pB:
                    ans.append(-1)
                else:
                    ans.append(vA / vB)
        return ans