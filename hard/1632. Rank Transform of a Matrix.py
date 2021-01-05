# 1632. Rank Transform of a Matrix
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        1/2 Array.
        Collect elements and their positions. Sort by element, and assign
        ranks to them. Note that for the same value there can be multiple
        positions, and the ranks can be different, and in this case the
        rank needs to be the max one.
        '''
        R, C = len(matrix), len(matrix[0])

        val_to_pos = defaultdict(list)
        for r in range(R):
            for c in range(C):
                val_to_pos[matrix[r][c]].append((r, c))

        # the max (rank, val) for each row
        row_max = [(0, -math.inf) for _ in range(R)]
        col_max = [(0, -math.inf) for _ in range(C)]
        ans = [[0] * C for _ in range(R)]

        for val in sorted(val_to_pos.keys()):
            for _ in range(len(val_to_pos[val])):
                # Keep updating the ranks or this val until there's no more rank updaet.
                update = False
                for r, c in val_to_pos[val]:
                    rank = max(row_max[r][0] + (val > row_max[r][1]), col_max[c][0] + (val > col_max[c][1]))
                    if ans[r][c] < rank:
                        ans[r][c] = rank
                        row_max[r] = (rank, val)
                        col_max[c] = (rank, val)
                        update = True
                if not update: break

        return ans
        '''
        2/2 Union Find.
        The key is to group points with the same values by their rows and cols.
        Instead of point-point connection which would be too many, we track the
        row level connections and col level connections. For the same point,
        its row -> col. If there's another point with the same value in the
        same row, we will have row -> col -> col2. If there's another point
        with the same value in the same col, we will have
        (row, row2) -> col -> col2. This takes much less space.

        The UF here is a bit different than the regular template. The UF here
        uses dict as it has negative numbers as keys.
        '''
        R = len(matrix)
        C = len(matrix[0])

        # implement find and union
        def find(UF, x):
            if x != UF[x]:
                UF[x] = find(UF, UF[x])
            return UF[x]

        def union(UF, x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(UF, x)] = find(UF, y)

        # link row and col together
        UFs = defaultdict(defaultdict)  # UFs[val]: the Union-Find of value val
        for r in range(R):
            for c in range(C):
                val = matrix[r][c]
                # union row r to col c, '~c = -c - 1', this is to distinguish c from r.
                union(UFs[val], r, ~c)

        # put points into `value2index` dict, grouped by connection
        value2index = defaultdict(lambda: defaultdict(list))
        for r in range(R):
            for c in range(C):
                val = matrix[r][c]
                group_root = find(UFs[val], r)
                value2index[val][group_root].append((r, c))

        answer = [[0] * C for _ in range(R)]  # the required rank matrix
        rowmax = [0] * R  # rowmax[r]: the max rank in r row
        colmax = [0] * C  # colmax[c]: the max rank in c col
        for val in sorted(value2index.keys()):
            # update connected points with the same value
            for points in value2index[val].values():
                rank = max(max(rowmax[r], colmax[c]) + 1 for r, c in points)
                for r, c in points:
                    answer[r][c] = rank
                    rowmax[r] = max(rowmax[r], rank)
                    colmax[c] = max(colmax[c], rank)

        return answer