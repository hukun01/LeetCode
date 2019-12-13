class Node:
    def __init__(self):
        self.children = {}
        self.word = None
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        Trie + DFS. A few tricks:
        
        1. To de-dup, erase the word on the trie node after adding it to the result.
        2. Mark the board[r][c] = '#' as visited, to avoid having an extra set for visited.
        3. No need to store the char on the trie node, we just need the children dict.
        '''
        def growTrie(node, word):
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = word
            
        root = Node()
        for w in words:
            growTrie(root, w)
            
        def dfs(r, c, node):
            char = board[r][c]
            if char == '#' or char not in node.children:
                return
            node = node.children[char]
            if node.word:
                ans.append(node.word)
                node.word = None

            board[r][c] = '#'
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                newR = r + d[0]
                newC = c + d[1]
                if newR < 0 or newR >= len(board) or newC < 0 or newC >= len(board[0]):
                    continue
                dfs(newR, newC, node)
            board[r][c] = char
        
        ans = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)
        return ans