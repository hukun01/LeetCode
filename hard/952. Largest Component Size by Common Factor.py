# 952. Largest Component Size by Common Factor
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        '''
        UnionFind + math.
        Find all the factors of each number from [1, sqrt(num)],
        and union (factor, num). Note that we also union the
        (complement factor, num), as the complement factor may be
        greater than factor, e.g., 6's factor is 2 in [1, sqrt(6)],
        while the complement factor is 3.
        '''
        uf = UnionFind(max(A)+1)
        for a in A:
            for factor in range(2, int(sqrt(a))+1):
                if a % factor == 0:
                    uf.find_and_union(a, factor)
                    uf.find_and_union(a, a // factor)

        group_count = Counter()
        for a in A:
            group_id = uf.find(a)
            group_count[group_id] += 1

        return max(group_count.values())

class UnionFind:
    def __init__(self, n):
        self.component_count = n
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parents[y] = x
        self.size[x] += self.size[y]
        self.component_count -= 1

    # return true if two are newly unioned, false if already unioned.
    def find_and_union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 != y0:
            self.union(x0, y0)
            return True
        return False