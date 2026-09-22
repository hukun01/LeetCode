class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        '''
        Use a UF to keep track of the components in the graph.
        
        Note that the positions can have duplicate entries, when seeing an entry that's
        visited, just add the current UF component_count and skip the rest.
        '''
        uf = UnionFind()
        ans = []
        seen = set()
        for r, c in positions:
            if (r, c) in seen:
                ans.append(uf.component_count)
                continue
            uf.parents[(r,c)] = (r,c)
            uf.component_count += 1
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r0, c0 = r + dr, c + dc
                if (r0, c0) in seen:
                    uf.union((r, c), (r0, c0))
            seen.add((r, c))
            ans.append(uf.component_count)
        
        return ans


class UnionFind:
    def __init__(self):
        self.component_count = 0
        self.parents = {}
        self.size = defaultdict(lambda: 1)

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
