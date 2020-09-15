# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        Brute force + Kruskal algorithm.
        Use Kruskal to find the optimal MST weight.
        Iterate through the edges, try removing each edge, and
        get the new MST weight2, if weight2 is larger, then
        the edge is critical. Otherwise, if we include the edge,
        and get the new MST weight3, and weight3 == optimal, then
        this edge is pseudo critical.
        '''
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x: x[2])

        # Note that the index here is the edges' index, not the recorded
        # index in each edge, because we need to add pre_edge's weight
        # and union its vertices sufficiently (otherwise we have to pass
        # in the a, b, and w, along with the edge_idx.
        def get_mst_weight(blocked, pre_edge):
            uf = UnionFind(n)
            weight = 0
            if pre_edge != -1:
                weight += edges[pre_edge][2]
                uf.union(edges[pre_edge][0], edges[pre_edge][1])
            for i in range(len(edges)):
                if i == blocked:
                    continue
                a, b, w, _ = edges[i]
                if uf.union(a, b):
                    weight += w
            if uf.component_count != 1:
                return math.inf
            return weight
        optimal_weight = get_mst_weight(-1, -1)
        critical, pseudo = [], []
        for i in range(len(edges)):
            if optimal_weight < get_mst_weight(i, -1):
                critical.append(edges[i][3])
            elif optimal_weight == get_mst_weight(-1, i):
                pseudo.append(edges[i][3])
        return [critical, pseudo]

class UnionFind:
    def __init__(self, n):
        self.component_count = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    # return true if two are newly unioned, false if already unioned.
    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return False
        if self.size[x0] < self.size[y0]:
            x0, y0 = y0, x0
        self.parents[y0] = x0
        self.size[x0] += self.size[y0]
        self.component_count -= 1
        return True