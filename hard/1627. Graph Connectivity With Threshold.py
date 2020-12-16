# 1627. Graph Connectivity With Threshold
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        '''
        UF.
        The key is to enumerate all the number pairs that whose common divisor
        is greather than threshold, namely, >= (threshold + 1).
        We can enumerate (a, b) pairs where
        a from range(threshold + 1, n + 1, 1), b from range(a + a, n + 1, a).

        Note that calculating GCD for each pair takes O(log(n)) that would be
        too slow.

        Time: O((n-k) n/k) outer loop is O(n-k), inner loop is O(n/k), UF
              operations are amortized O(1).
        Space: O(n)
        '''
        uf = UnionFind(n + 1)
        for a in range(threshold + 1, n + 1):
            for b in range(a + a, n + 1, a):
                uf.union(a, b)
        return [uf.find(a) == uf.find(b) for a, b in queries]
        
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