# 1168. Optimize Water Distribution in a Village
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        '''
        UnionFind.

        The tricky part in this problem is how we use 'wells'. The pipes is a
        list of weighted edges, but the wells is a list of weighted nodes. I'm
        not aware of any algorithm that processes both. Hence we need to
        transform the input to make it easier, aka, edges only. A key trick is
        to make a fake house 0, which is the only house with the well. Then we
        can build edges from house 0 to any house i, and the cost of the edge
        is wells[i-1].
        After this transformation, we now get a list of edges with costs. The
        goal is to find a connected component from this graph with the min
        cost. And this is a Minimum Spanning Tree problem that we can use
        Kruskal to solve, by sorting the edges by cost, and union the nodes.
        Add the cost if the two nodes are newly connected.

        Time: O(n log(n))
        Space: O(n)
        '''
        uf = UnionFind(n+1)
        edges = [(cost, w, 0) for w, cost in enumerate(wells, start=1)]
        edges += [(cost, i, j) for i, j, cost in pipes]
        ans = 0
        for cost, h1, h2 in sorted(edges):
            if uf.union(h1, h2):
                ans += cost
        return ans

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