# 212. Word Search II    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        Trie + DFS. A few tricks:
        
        1. To de-dup, erase the word on the trie node after adding it to the result.
        2. Mark the board[r][c] = '#' as visited, to avoid having an extra set for visited.
        3. No need to store the char on the trie node, we just need the children dict.
        '''
        # another template for: Node = lambda: defaultdict(Node); trie = Node();
        root = Node()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = w
        ans = []
        def dfs(r, c, node):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return
            char = board[r][c]
            if char not in node.children:
                return
            curr = node.children[char]
            if curr.word:
                ans.append(curr.word)
                curr.word = None
            board[r][c] = '#'
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                dfs(dr + r, dc + c, curr)
            board[r][c] = char
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, root)
        return ans

class Node:
    def __init__(self):
        self.children = {}
        self.word = None