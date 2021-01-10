# 1722. Minimize Hamming Distance After Swap Operations
class Solution:
    def minimumHammingDistance(self, S: List[int], T: List[int], A: List[List[int]]) -> int:
        '''
        UnionFind.

        The allowed swaps can make anything interchangeable inside the
        connected groups. Use an UF to represent those groups. For each group,
        keep a Counter() to record what's available in S, as there can be
        duplicate values. Then go through T, and find the group from S, and
        see if S has this value, if not increment ans (mismatch) by 1.

        Time: O(n + a) where n is len(S), a is len(A)
        Space: O(n)
        '''
        n = len(S)
        uf = UnionFind(n)
        for a, b in A:
            uf.union(a, b)

        root2freqs = defaultdict(Counter)
        for i in range(n):
            root2freqs[uf.find(i)][S[i]] += 1
            
        ans = 0
        for i in range(n):
            t = T[i]
            root = uf.find(i)
            if root2freqs[root][t] == 0:
                ans += 1
            else:
                root2freqs[root][t] -= 1

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