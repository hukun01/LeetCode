# 1245. Tree Diameter
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        '''
        1/2 BFS twice.
        The first BFS finds the farthest node A, starting from any node.
        The second BFS finds the farthest node B, starting from A.
        The distance between A and B is the longest path.
        '''
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(src):
            visited = {src}
            q = deque([(src, 0)])  # (vertex, distance)
            farthestNode, farthestDist = -1, 0
            while q:
                farthestNode, farthestDist = q.popleft()
                for v in graph[farthestNode]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, farthestDist + 1))
            return farthestNode, farthestDist

        farthestNode, _ = bfs(0)
        _, dist = bfs(farthestNode)
        return dist
        '''
        2/2 Tree + recursion.
        Diameter is the length sum of longest 2 paths that share the same root.
        Note that any node can be the root, and the two ends of the diameter
        path are (grand)children of the root.
        '''
        n = len(edges) + 1
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        self.diameter = 0
        def get_depth(root, parent):
            depths = [0, 0]
            for child in graph[root]:
                if child == parent:
                    continue
                child_depth = get_depth(child, root)
                heappush(depths, child_depth)
                heappop(depths)
            longest_path_via_root = sum(depths) + 1
            self.diameter = max(self.diameter, longest_path_via_root - 1)
            return depths[-1] + 1
        get_depth(0, -1)
        return self.diameter