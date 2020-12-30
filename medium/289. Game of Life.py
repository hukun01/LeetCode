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
        Let 2 be the state for 'dying' from 'live' to die.
        Let 3 be the state for 'living' from 'live' to live.
        Let 4 be the state for 'reproducing' from 'dead' to live.

        Then traverse the board twice. First time we update to the
        intermediate states. In this traversal, treat 2 and 3 as live, and 4
        as dead. In the second traversal, we update 2 to dead, and 3,4 to live.

        Time: O(RC)
        Space: O(1)
        '''
        R, C = len(board), len(board[0])
        def count_neighbors(r, c):
            lives = 0
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < R or not 0 <= nc < C:
                        continue
                    if (nr, nc) == (r, c):
                        continue
                    
                    if board[nr][nc] in {1, 2, 3}:
                        lives += 1
            return lives

        for r in range(R):
            for c in range(C):
                lives = count_neighbors(r, c)
                if board[r][c] == 1:
                    if 2 <= lives <= 3:
                        board[r][c] = 3
                    else:
                        board[r][c] = 2
                else:
                    if lives == 3:
                        board[r][c] = 4
        for r in range(R):
            for c in range(C):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] in {3, 4}:
                    board[r][c] = 1