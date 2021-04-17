# 425. Word Squares
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        Trie + DFS backtracking.
        Build the word square row by row, when filling (r, c), also advance
        its vertical corresponding element (c, r).
        Note that we don't want to advance a node twice when (r, c) == (c, r).
        Also note that when starting filling the next row, we don't start from
        the 0th column, but from the row-th column.

        Time: O(N W) where N is the len(words), W is the length of a word,
              note that O(26^W) is correct but too loose.
        Space: O(N W).
        '''
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        for w in words:
            node = root
            for c in w:
                node = node[c]
            node['#'] = w

        self.ans = []
        n = len(words[0])
        def dfs(path, r, c):
            if  r == n:
                self.ans.append([node['#'] for node in path])
                return

            if c == n:
                dfs(path, r + 1, r + 1)
            else:
                for next_char in path[r]:
                    if next_char not in path[c]:
                        continue
                    new_path = path[:]
                    new_path[c] = new_path[c][next_char]
                    if r != c:
                        new_path[r] = new_path[r][next_char]

                    dfs(new_path, r, c + 1)

        dfs([root] * n, 0, 0)
        return self.ans