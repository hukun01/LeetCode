class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        1/2 BFS.
        Two keys here:
        1. Update the initial 1s to infinite, so that we know 
           whether a cell is visited or not. At the same time,
           store the 0s to a queue for later traversal.
        2. When updating a neighbor cell, use the current cell's value + 1.
        '''
        queue = deque()
        R = len(matrix)
        C = len(matrix[0])
        for row in range(R):
            for col in range(C):
                if matrix[row][col] > 0:
                    matrix[row][col] = float('inf')
                else:
                    queue.append((row, col))

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            row, col = queue.popleft()
            for d in dirs:
                newRow = row + d[0]
                newCol = col + d[1]
                if newRow < 0 or newRow >= R or newCol < 0 or newCol >= C:
                    continue
                if matrix[newRow][newCol] <= matrix[row][col] + 1:
                    continue
                matrix[newRow][newCol] = matrix[row][col] + 1
                queue.append((newRow, newCol))
        return matrix