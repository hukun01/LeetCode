# 886. Possible Bipartition
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        '''
        DFS.
        Bipartite means 2-colored.
        Simplified graph coloring problem. Build the graph, in which an edge
        represents the dislike between two nodes. DFS on the graph and ensure
        each node is assigned to one color, while all its neighbors are
        assigned to the other color.

        Time: O(N + E) where E is the number of edges
        Space: O(N + E)
        Same as 785. Is Graph Bipartite?
        '''
        graph = defaultdict(set)
        for a, b in dislikes:
            graph[a].add(b)
            graph[b].add(a)

        # DFS returns whether a node and a color is compatible after exploring
        # the cases that all neighbors assigned to the other color.
        node_to_color = dict()
        def dfs(node, color):
            if node in node_to_color:
                return node_to_color[node] == color
            node_to_color[node] = color
            return all(dfs(nei, color ^ 1) for nei in graph[node])

        for node in range(1, N + 1):
            if node not in node_to_color and not dfs(node, 0):
                return False
        return True