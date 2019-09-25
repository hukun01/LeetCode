class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Regular DFS. The key here is to stop early by comparing the last character.
        '''
        compass = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(board), len(board[0])

        def dfs(row, col, curr, visited):
            if len(curr) == len(word):
                return curr == word

            if curr[-1] != word[len(curr)-1]:
                return False

            for dirs in compass:
                newRow = row + dirs[0]
                newCol = col + dirs[1]
                if 0 <= newRow < rows and 0 <= newCol < cols and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    newWord = curr + board[newRow][newCol]
                    if dfs(newRow, newCol, newWord, visited):
                        return True
                    visited.remove((newRow, newCol))
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, board[r][c], { (r, c) }):
                    return True
        return False