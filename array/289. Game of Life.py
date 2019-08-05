class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        To solve it in-place, we need to make use of each element itself to
        store the next state.
        We can add 2 to each cell whenever they should be live in the next round;
        When counting neighbors, we check whether the cell >= 2, if so, that 
        means we added 2 to it, so we subtract 2 from it, and use the result as
        the neighbor.
        2 means it was 0, now it's 1.
        3 means it was 1, now it's still 1.
        Note that for cell that dies in the next round, we do NOT want to set it to 0 during the process!

        At the end, we need to go through the board and set every cell to 1 if it's >= 2,
        and set the cell to 0 otherwise.
        """
        rows = len(board)
        cols = len(board[0])
        def countNeighbors(r, c):
            total = 0
            for i in range(max(0, r-1), min(rows, r+2)):
                for j in range(max(c-1, 0), min(cols, c+2)):
                    if board[i][j] > 1:
                        neighbor = board[i][j] - 2
                    else:
                        neighbor = board[i][j]
                    total += neighbor
            return total - board[r][c]
        
        for r in range(rows):
            for c in range(cols):
                liveNeighbors = countNeighbors(r, c)
                if liveNeighbors == 3 or (liveNeighbors == 2 and board[r][c] == 1):
                    board[r][c] += 2
                # Note that we can't set board[r][c] to 0 in the else branch yet
        for r in range(rows):
            for c in range(cols):
                if board[r][c] > 1:
                    board[r][c] = 1
                else:
                    board[r][c] = 0