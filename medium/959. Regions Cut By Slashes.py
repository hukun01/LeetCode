# 959. Regions Cut By Slashes
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        '''
        UnionFind

        Each cell (r, c) id i = r * N + c
        Each cell has 4 subcells divided by 'x', from 0 to 3.
        if cell is '/', we connect 0 and 3, 1 and 2, 
        if cell is '\', we connect 0 and 1, 2 and 3, 
        Also for each cell, connect 0 and upper cell's 2, and
        3 and left cell's 1.

        Time: O(n^2)
        Space: O(n^2)
        '''
        n = len(grid)
        uf = UnionFind(n * n * 4)
        def get_cell_id(r, c):
            return 4 * (r * n + c)

        for r in range(n):
            for c in range(n):
                cell = get_cell_id(r, c)
                if grid[r][c] == '/':
                    uf.union(cell, cell + 3)
                    uf.union(cell + 1, cell + 2)
                elif grid[r][c] == '\\':
                    uf.union(cell, cell + 1)
                    uf.union(cell + 2, cell + 3)
                else:
                    uf.union(cell, cell + 1)
                    uf.union(cell, cell + 2)
                    uf.union(cell, cell + 3)

                if r - 1 >= 0:
                    uf.union(cell, get_cell_id(r - 1, c) + 2)
                if c - 1 >= 0:
                    uf.union(cell + 3, get_cell_id(r, c - 1) + 1)

        return uf.component_counts

class UnionFind:
    
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.component_counts = n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x0 = self.find(x)
        y0 = self.find(y)
        if x0 == y0:
            return
        if self.sizes[x0] < self.sizes[y0]:
            x0, y0 = y0, x0
        self.sizes[x0] += self.sizes[y0]
        self.parents[y0] = x0
        self.component_counts -= 1