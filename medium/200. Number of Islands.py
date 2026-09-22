# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Union Find.
        This can be solved by DFS/BFS as well, but UF is more natural, and
        UF can solve follow-ups like how to merge/break islands, or count new
        ones if we can make lands (aka, fill the sea), for example, 305. Number of Islands II.
        '''
        R, C = len(grid), len(grid[0])
        uf = UnionFind()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '0':
                    continue
                uf.parents[(r,c)] = (r,c)
                uf.component_count += 1
                if c - 1 >= 0 and grid[r][c-1] == '1':
                    uf.union((r,c), (r,c-1))
                if r - 1 >= 0 and grid[r-1][c] == '1':
                    uf.union((r,c), (r-1,c))
        
        return uf.component_count

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
