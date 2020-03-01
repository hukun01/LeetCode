class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        The key here is to write short, concise, readable code.
        Use f"cell in row x" and f"cell in col y", and f"cell in block x-y" to 
        help easily find duplicates.
        '''
        visited = set()
        def addMessage(msg):
            if msg in visited:
                return False
            visited.add(msg)
            return True
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                digit = board[r][c]
                if not addMessage(f"{digit} in row {r}"):
                    return False
                if not addMessage(f"{digit} in col {c}"):
                    return False
                if not addMessage(f"{digit} in cell {r//3}-{c//3}"):
                    return False
        return True