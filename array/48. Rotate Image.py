class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Swap top-down, then swap using topLeft-bottomRight diagonal
        """
        matrix.reverse()
        n = len(matrix)
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]