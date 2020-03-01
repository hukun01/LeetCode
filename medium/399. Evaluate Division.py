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

        parents = {}
        
        def find(operand):
            if operand != parents[operand][0]:
                p = find(parents[operand][0])
                parents[operand][0] = p[0]
                parents[operand][1] *= p[1]
            return parents[operand]
        
        for i, e in enumerate(equations):
            a, b = e
            k = values[i]
            if a not in parents and b not in parents:
                parents[a] = [b, k]
                parents[b] = [b, 1.0]
            elif a not in parents:
                parents[a] = [b, k]
            elif b not in parents:
                parents[b] = [a, 1.0 / k]
            else:
                pA = find(a)
                pB = find(b)
                if pA != pB:
                    pA[0] = pB[0]
                    pA[1] *= k * pB[1]
                
        ans = []
        for q in queries:
            a, b = q
            if a not in parents or b not in parents:
                ans.append(-1.0)
                continue
            if find(a)[0] == find(b)[0]:
                ans.append(parents[a][1] / parents[b][1])
            else:
                ans.append(-1.0)
        return ans
        '''