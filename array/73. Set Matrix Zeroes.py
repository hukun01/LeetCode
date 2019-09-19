class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        Use the first row and first col to store the states of each row and col.
        Note that the first row itself and the first col itself will use the same cell, the origin,
        so use that cell for the first row, and use a single var for the first col.
        Since we handle the first col separately, we need to skip the first col when iterating.
        Also note that when we use the states, we need to go from bottom right to top left, such that
        we don't erase our own footprint.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        
        firstColIsZero = False
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            if matrix[r][0] == 0:
                firstColIsZero = True
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = matrix[r][0] = 0

        for r in reversed(range(rows)):
            for c in reversed(range(1, cols)):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
            if firstColIsZero:
                matrix[r][0] = 0