class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        The key here is to write short, concise, readable code.
        Use f"cell in row x" and f"cell in col y", and f"cell in block x-y" to 
        help easily find duplicates.
        '''
        seen = set()
        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                rowRecord = f"{cell} in row {row}"
                if rowRecord in seen:
                    return False
                seen.add(rowRecord)
                colRecord = f"{cell} in col {col}"
                if colRecord in seen:
                    return False
                seen.add(colRecord)
                blockRecord = f"{cell} in block {row // 3}-{col // 3}"
                if blockRecord in seen:
                    return False
                seen.add(blockRecord)
        return True