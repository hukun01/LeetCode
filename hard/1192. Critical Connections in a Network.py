# 1192. Critical Connections in a Network
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Tarjan's algorithm to find SCC (Strongly Connected Component).

        Since the edges are undirected, SCC here isn't the strict SCC in
        its original definition. Instead, SCC here is the component with a
        cycle, in other words, each node can reach others in at least 2 paths.
        And undirected is simpler than directed graph, in which we would need
        the full Tarjan's algorithm that also checks each SCC separately.

        The critical connections are the ones that are not part of any SCCs.
        We use Tarjan's algorithm to find SCCs, during this process, we can
        collect the edges that are not part of any SCCs.

        Regarding Tarjan's SCC algorithm, it uses a DFS to find the low-link
        of each node. The low-link is the smallest depth of a node.
        1. Start from any node, iterate through its neighbors and do DFS if the
           neighbor's low-link hasn't been set, and increment the low-link;
        2. Upon DFS recursion finishes, set the current node's low-link using
           the min(depths[current], depths[neighbor]);
        3. During this process, when a node's neighbor has already been visited
           in the earlier depth, this node would use the earlier depth as well,
           and propagate the low-link back. Eventually, the whole SCC would
           have the same low-link. Hence, after the traversing all nodes, we
           get a low-link/depths array in which each SCC shares the same depth.

        Time: O(E+V)
        Space: O(V)

        Video reference: https://www.youtube.com/watch?v=wUgWX0nc4NY
        '''
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        UNVISITED = -1
        depths = [UNVISITED] * n

        def dfs(node, par=None, d=0):
            depths[node] = d
            for nei in graph[node]:
                if nei == par:
                    continue
                if depths[nei] == UNVISITED:
                    dfs(nei, node, d + 1)
                depths[node] = min(depths[node], depths[nei])

            # We just found a SCC and current node is the start of it, now the
            # par-node connection is an edge external to this SCC, hence it's
            # critical.
            if depths[node] == d and par is not None:
                self.ans.append((par, node))

        self.ans = []
        dfs(0)
        return self.ans