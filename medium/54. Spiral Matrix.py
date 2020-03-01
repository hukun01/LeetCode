class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        To make the logic clear, do all the boundaries update at the end of the while loop.

        Note that when processing the last row and the first column, need to check for duplicates.
        '''
        if not matrix or not matrix[0]:
            return []
        
        ans = []
        rowStart, rowEnd = 0, len(matrix)
        colStart, colEnd = 0, len(matrix[0])
        while rowStart < rowEnd and colStart < colEnd:
            # top row
            for col in range(colStart, colEnd):
                ans.append(matrix[rowStart][col])
            # right col
            for row in range(rowStart+1, rowEnd):
                ans.append(matrix[row][colEnd-1])
            # bottom row if not overlapped with top row
            if rowStart != rowEnd - 1:
                for col in reversed(range(colStart, colEnd-1)):
                    ans.append(matrix[rowEnd-1][col])
            # left col if not overlapped with right col
            if colStart != colEnd - 1:
                for row in reversed(range(rowStart+1, rowEnd-1)):
                    ans.append(matrix[row][colStart])
            
            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1
            
        return ans