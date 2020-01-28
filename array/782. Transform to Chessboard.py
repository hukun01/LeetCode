# 782. Transform to Chessboard
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        '''
        Make two checks and if both pass, we are sure that this board can transform.
        
        1. A good starting board has exactly two kinds of rows, and these two rows must
        negate each other. Same applies column wise. This means that the 4 corners of
        any rectangle in the board must be 4 ones, or 4 zeros, or 2 ones and 2 zeros,
        otherwise this board can't transform to chessboard.
        2. After the first check we know there are exactly two kinds of rows and one row
        is the inversed version of another. Now we just need to check the first row, or
        any row that: if the number of ones in this row is not N / 2 or (N + 1) / 2, then
        the column swaps would never lead to chessboard. Same applies column wise.
        
        Now we know that we definitely can transform to chessboard, we then count the total
        number X of misplaced rows and columns, and the number of swaps needed will be X / 2.
        '''
        b = board
        N = len(b)
        if any(b[0][0] ^ b[i][0] ^ b[0][j] ^ b[i][j] for i in range(N) for j in range(N)):
            return -1
        if not N // 2 <= sum(b[0]) <= (N + 1) // 2:
            return -1
        if not N // 2 <= sum(b[i][0] for i in range(N)) <= (N + 1) // 2:
            return -1
        rowSum = sum(b[0][i] == i % 2 for i in range(N))
        colSum = sum(b[i][0] == i % 2 for i in range(N))
        
        if N % 2 == 1:
            if rowSum % 2 == 1:
                rowSum = N - rowSum
            if colSum % 2 == 1:
                colSum = N - colSum
        else:
            rowSum = min(N - rowSum, rowSum)
            colSum = min(N - colSum, colSum)
        return (colSum + rowSum) // 2