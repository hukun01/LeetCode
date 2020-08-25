# 1032. Stream of Characters
Trie = lambda: defaultdict(Trie)
class StreamChecker:
    '''
    Trie + record each word reversely.
    The key takeaway is to use a special char as stopper in Trie node to
    indicate a certain node is a word.
    '''

    def __init__(self, words: List[str]):
        self.tree = Trie()
        self.size = 0
        for w in words:
            node = self.tree
            self.size = max(self.size, len(w))
            for c in reversed(w):
                node = node[c]
            node['$'] = ''
        self.chars = deque()

    def query(self, letter: str) -> bool:
        self.chars.append(letter)
        if len(self.chars) > self.size:
            self.chars.popleft()
        node = self.tree
        for c in reversed(self.chars):
            if c in node:
                node = node[c]
                if '$' in node:
                    return True
            else:
                break
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)