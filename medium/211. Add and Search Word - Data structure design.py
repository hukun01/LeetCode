# 211. Add and Search Word - Data structure design
class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie_root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie_root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_word = True
    
    def _dfs(self, node: Node, idx: int, word: str) -> bool:
        if idx == len(word):
            return node and node.is_word
        if (char := word[idx]) in node.children:
            return self._dfs(node.children[char], idx + 1, word)
        if char == '.':
            return any(self._dfs(node.children[c], idx + 1, word) for c in node.children)
        return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._dfs(self.trie_root, 0, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)