class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        Two keys here:
        1. Update the initial 1s to infinite, so that we know 
           whether a cell is visited or not. At the same time,
           store the 0s to a queue for later traversal.
        2. When updating a neighbor cell, use the current cell's value + 1.
        '''
        rows, cols = len(matrix), len(matrix[0])
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] != 0:
                    matrix[r][c] = float('inf')
                else:
                    queue.append((r, c))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for d in dirs:
                newR = r + d[0]
                newC = c + d[1]
                if 0 <= newR < rows and 0 <= newC < cols and matrix[newR][newC] > matrix[r][c] + 1:
                    queue.append((newR, newC))
                    matrix[newR][newC] = matrix[r][c] + 1
        
        return matrix