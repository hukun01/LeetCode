# 957. Prison Cells After N Days
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        '''
        Note that there are 8 cells with 2 states in each cell, so
        in total there are at most 2 ^ 8 = 256 states.
        As N can go up to 10 ^ 9, the prison states must form a cycle.
        Find out the cycle size, and fast forward the N.
        '''
        def get_next(cells):
            next_cells = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                next_cells[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            return next_cells
        seen = dict()
        for i in range(N):
            if (key := str(cells)) in seen:
                cycle_size = i - seen[key]
                N = (N - i) % cycle_size
                for _ in range(N):
                    cells = get_next(cells)
                break
            seen[key] = i
            cells = get_next(cells)
        return cells