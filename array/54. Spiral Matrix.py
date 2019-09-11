class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        Note that when processing the last row and the first column, need to check for duplicates.
        '''
        if not matrix or not matrix[0]:
            return []
        
        ans = []
        rowStart, rowEnd = 0, len(matrix)
        colStart, colEnd = 0, len(matrix[0])
        while rowStart < rowEnd and colStart < colEnd:
            # first row
            for col in range(colStart, colEnd):
                ans.append(matrix[rowStart][col])
            # last col
            for row in range(rowStart+1, rowEnd):
                ans.append(matrix[row][colEnd-1])
            # last row
            if rowStart != rowEnd - 1:
                for col in reversed(range(colStart, colEnd-1)):
                    ans.append(matrix[rowEnd-1][col])
            # first col
            if colStart != colEnd - 1:
                for row in reversed(range(rowStart+1, rowEnd-1)):
                    ans.append(matrix[row][colStart])
            
            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1
            
        return ans