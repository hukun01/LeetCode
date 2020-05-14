# 208. Implement Trie (Prefix Tree)
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.isWord = False
    
class Trie:
    '''
    Straightforward idea with one handy template below:

    Node = lambda: defaultdict(Node)
    trie = Node()
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True
        
    def find(self, part: str) -> Node:
        node = self.root
        for c in part:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node.isWord if node else False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.find(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)