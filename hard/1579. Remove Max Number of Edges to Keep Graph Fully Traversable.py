# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        Union Find.
        Consider UF first whenever the problem is about connectivity.
        We always prefer type3 edges becaus they can be shared.
        Have 2 UFs, one for Alice, one for Bob. Populate them with type3 edges.
        Iterate through type1 and type2 edges, find the redundant edges for
        Alice and Bob, respectively.
        '''
        to_remove = 0
        alice = UnionFind(n)
        bob = UnionFind(n)
        for t, u, v in edges:
            if t != 3:
                continue
            if not alice.union(u-1, v-1) or not bob.union(u-1, v-1):
                to_remove += 1
        for t, u, v in edges:
            if t == 1 and not alice.union(u-1, v-1):
                to_remove += 1
            elif t == 2 and not bob.union(u-1, v-1):
                to_remove += 1
        if alice.component_count == bob.component_count == 1:
            return to_remove
        return -1
        
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