# 839. Similar String Groups
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        '''
        Union Find.
        We need to put similar words in their groups with UF.

        We can either enumerate all the possible similar word with time N(W^3),
        or we can iterate through all the other words to find the similar ones with
        time (N^2)W.
        Comparing N * (W^3) and (N^2) * W, aka, W^2 and N. We need to switch to
        different approaches depending on which one is greater.
        '''
        N, W = len(A),len(A[0])
        def similar(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2)) <= 2

        uf = UnionFind(N)

        if N <= W**2:
            for (i1, a), (i2, b) in itertools.combinations(enumerate(A), 2):
                if similar(a, b):
                    uf.union(i1, i2)
        else:
            A_map = {a:i for i,a in enumerate(A)}
            for i1, a in enumerate(A):
                for i in range(W - 1):
                    for j in range(i + 1, W):
                        b = a[:i] + a[j] + a[i+1:j] + a[i] + a[j+1:]
                        if b in A_map and (i2 := A_map[b]) != i1:
                            uf.union(i1, i2)
        return uf.component_count

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