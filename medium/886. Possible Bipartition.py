# 886. Possible Bipartition
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        '''
        DFS.
        Simplified graph coloring problem. Build the graph, in which an edge
        represents the dislike between two nodes. DFS on the graph and ensure
        each node is assigned to one color, while all its neighbors are
        assigned to the other color.
        '''
        graph = defaultdict(set)
        for i, j in dislikes:
            graph[i].add(j)
            graph[j].add(i)

        # DFS returns whether a node and a color is compatible after exploring
        # the cases that all neighbors assigned to the other color.
        colors = dict()
        def dfs(node, c):
            if node in colors:
                return colors[node] == c
            colors[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        for node in range(1, N + 1):
            if node not in colors and not dfs(node, 0):
                return False
        return True