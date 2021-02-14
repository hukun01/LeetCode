# 685. Redundant Connection II
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        Union Find.
        In general, the redundant edge forms an undirected cycle, namely, some
        non-root node would have 2 indegree, or root would have 1 indegree.
        Specifically, there are 3 issue types that the redundant edge causes.
        1. cycle formed by root and a non-root node.
        2. cycle formed by non-root node and its ancestor.
        3. cycle formed by 2 non-root nodes that only share root.
        In case1, we can delete any edge inside the cycle, so we delete the
        first one in 'edges'. In this case there's no node with 2 indegree.
        In case2, we need to delete the extra edge that's inside the cycle.
        In case3, we can delete any of the 2 extra edges, just delete the first
        edge in 'edges'.

        To determine which edge is extra, we need to track the direct parents
        for each node, and when a node has 2 direct parents, the 2 edges from
        the parents are candidates for deletion, called edge1 and edge2.

        Go through every edge (parent, kid), if kid already has a parent, this
        is case2 or case3. If kid has no parent, try union them, and if union
        fails, we know there's a cycle elsewhere, record the last edge in cycle.
        Note we are not sure that the last edge in cycle belongs to which case.

        Now if we have edge1 and edge2, it's case2 or case3. Based on this, if
        the last edge in cycle exists, then it's case3, otherwise case2.
        If we don't have edge1 and edge2, then it's case1, we return the last
        edge in cycle.

        Time: O(n) if we take UF operation as amortized O(1)
        Space: O(n)
        '''
        n = len(edges)
        direct_parent = [0] * (n + 1)
        uf = UnionFind(n + 1)
        last_edge_in_cycle = edge1 = edge2 = None
        for parent, kid in edges:
            if direct_parent[kid] != 0:
                edge1 = [direct_parent[kid], kid]
                edge2 = [parent, kid]
            else:
                direct_parent[kid] = parent
                if not uf.union(parent, kid):
                    last_edge_in_cycle = [parent, kid]

        if edge1 and edge2:
            if last_edge_in_cycle:
                return edge1
            return edge2
        return last_edge_in_cycle

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