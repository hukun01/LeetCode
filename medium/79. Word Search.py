# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Regular DFS. The key here is to stop early by comparing the last character.
        Also, comparing the char-count in word char-count in the board to check the
        existence helps a lot with performance.
        '''
        if collections.Counter(word) - collections.Counter(ch for row in board for ch in row):
            return False
        def dfs(r, c, wIdx):
            if wIdx == len(word):
                return True
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
                return False
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if board[r][c] != word[wIdx]:
                    continue
                board[r][c] = '#'
                if dfs(r + dr, c + dc, wIdx + 1):
                    return True
                board[r][c] = word[wIdx]
            return False
        return any(dfs(r, c, 0) for r in range(len(board)) for c in range(len(board[0])))