# 1617. Count Subtrees With Max Distance Between Cities
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        Brute force + tree diameter.
        Try all 2 ** n possible subsets, for each subset, use O(n) bfs to
        find the diameter of the tree based on the subset. Note that the
        subset may not be a valid tree.
        Similar to 1245. Tree Diameter.
        '''
        def bfs(src, cities):
            visited = {src}
            q = deque([(src, 0)])  # (vertex, distance)
            farthestNode, farthestDist = -1, 0
            while q:
                farthestNode, farthestDist = q.popleft()
                for v in graph[farthestNode]:
                    if v not in visited and v in cities:
                        visited.add(v)
                        q.append((v, farthestDist + 1))
            # Can't visit all nodes of the tree -> Invalid tree
            return farthestNode, farthestDist, len(visited) == len(cities)

        def diameterOfTree(cities):
            anyNode = cities[0]
            farthestNode, _, is_valid_tree = bfs(anyNode, cities)
            if not is_valid_tree:
                return 0
            _, dist, _ = bfs(farthestNode, cities)
            return dist

        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
            
        ans = [0] * (n - 1)
        for state in range(1, 2 ** n):
            cities = [i for i in range(n) if (state >> i) & 1 == 1]
            d = diameterOfTree(cities)
            if d > 0: ans[d - 1] += 1
        return ans