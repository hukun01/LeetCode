class Solution:    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
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