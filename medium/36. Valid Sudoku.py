# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        The key here is to write short, concise, readable code.
        Use f"cell in row x" and f"cell in col y", and f"cell in block x-y" to
        help easily find duplicates.

        Time: O(1)
        Space: O(1)
        '''
        seen = set()
        for r in range(9):
            for c in range(9):
                if (v := board[r][c]) == '.':
                    continue
                row_state = f'r {r}: {v}'
                col_state = f'c {c}: {v}'
                block_state = f'{r // 3}, {c // 3}: {v}'
                for state in [row_state, col_state, block_state]:
                    if state in seen:
                        #print(f'state {state}, seen {seen}')
                        return False
                    seen.add(state)
        return True