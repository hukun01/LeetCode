# 1697. Checking Existence of Edge Length Limited Paths
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        '''
        Sort + Union Find.
        It's easy to recognize this is an UF related problem, the key is to
        look at the queries first, and only union nodes whose distance is less
        than the query limit. There is no point adding nodes that exceed the
        limit. To do this, we sort queries by limit, sort edgeList by distance,
        and iterate through queries, for each query, we add all edges whose
        distance is less than this query's limit. After adding all feasible
        edges, we now check whether there's a path between the nodes in query.

        Time: O(n log(n))
        Space: O(n)
        '''
        edgeList.sort(key=lambda e: e[2])
        for i, q in enumerate(queries):
            q.append(i)
        queries.sort(key=lambda q: q[2])

        ans = [False] * len(queries)
        e_i = 0
        uf = UnionFind(n)
        for u, v, l, q_id in queries:
            while e_i < len(edgeList) and edgeList[e_i][2] < l:
                uf.union(edgeList[e_i][0], edgeList[e_i][1])
                e_i += 1
            ans[q_id] = uf.find(u) == uf.find(v)
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