class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        State machine.
        To solve it in-place, we need to make use of each element itself to
        store the next state.

        Have a set of intermediate states as below.
        let 1 continue to be the current and future living cell
        let 2 be the current live and future dead
        let 3 be the current dead and future living

        Then traverse the board twice. First time we update to the
        intermediate states.
        In the second traversal, we update 2 to dead, and 3 to live.

        Time: O(RC)
        Space: O(1)
        '''
        R, C = len(board), len(board[0])
        def count(r, c):
            ans = 0
            for r0 in range(r-1, r+2):
                for c0 in range(c-1, c+2):
                    if (r0, c0) == (r, c):
                        continue
                    if not 0 <= r0 < R or not 0 <= c0 < C:
                        continue
                    if board[r0][c0] in {1, 2}:
                        ans += 1

            return ans
        
        for r in range(R):
            for c in range(C):
                x = count(r, c)
                if x not in {2, 3}:
                    if board[r][c] == 1:
                        board[r][c] = 2
                else:
                    if x == 3 and board[r][c] == 0:
                        board[r][c] = 3

        for r in range(R):
            for c in range(C):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1