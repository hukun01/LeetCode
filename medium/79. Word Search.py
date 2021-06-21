# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Regular DFS. The key here is to stop early by comparing the last
        character.
        
        Also, comparing the char-count in word char-count in the board to check
        the existence helps a lot with performance.
        Counter1 - Counter2 is empty only if Counter2 has at least the same
        data as Counter1.

        Another key is to backtrack, if one path doesn't find the word, reclaim
        the char and try another path.
        '''
        if Counter(word) - Counter(ch for row in board for ch in row):
            return False
        R, C = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, w_idx):
            if w_idx == len(word):
                return True
            if not 0 <= r < R or not 0 <= c < C:
                return False
            if board[r][c] != word[w_idx]:
                return False
            board[r][c] = '#'
            if any(dfs(r + dr, c + dc, w_idx + 1) for dr, dc in dirs):
                return True
            board[r][c] = word[w_idx]
            return False

        return any(dfs(r, c, 0) for r in range(R) for c in range(C))