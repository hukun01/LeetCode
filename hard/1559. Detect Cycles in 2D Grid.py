# 1559. Detect Cycles in 2D Grid
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        '''
        Union find.
        We keep unioning the cells with same value from current position to
        left and top neighbors. At each position (r, c), if
        grid(r-1, c) == grid(r, c-1) == grid(r, c),
        and the two neighbors are connected, there must be a shared parent
        between them. Hence, there must be a cycle.

        In general, UF helps implementing cycle detection in undirected graph.
        '''
        R, C = len(grid), len(grid[0])
        def get_id(r, c):
            return r * C + c
        uf = UnionFind(R * C)
        for r in range(R):
            for c in range(C):
                letter = grid[r][c]
                if  r > 0 and grid[r-1][c] == letter and \
                    c > 0 and grid[r][c-1] == letter and \
                    uf.find(get_id(r-1, c)) == uf.find(get_id(r, c-1)):
                        return True
                for nr, nc in (r - 1, c), (r, c - 1):
                    if 0 <= nr < R and 0 <= nc < C and letter == grid[nr][nc]:
                        uf.find_and_union(get_id(nr, nc), get_id(r, c))

        return False

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