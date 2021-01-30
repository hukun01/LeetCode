# 785. Is Graph Bipartite?
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        Same as 886. Possible Bipartition.
        '''
        node_to_color = {}
        def dfs(node, color):
            if node in node_to_color:
                return node_to_color[node] == color
            node_to_color[node] = color
            return all(dfs(nei, color ^ 1) for nei in graph[node])

        for i in range(len(graph)):
            if i not in node_to_color and not dfs(i, 0):
                return False
        return True