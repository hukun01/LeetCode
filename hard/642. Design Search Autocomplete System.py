Trie = lambda: defaultdict(Trie)

class AutocompleteSystem:
    '''
    Use trie tree to record all sentences and times.
    Use DFS to find all applicable sentences; use heap to find the top
    sentences.
    '''
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = Trie()
        for s, t in zip(sentences, times):
            node = self.root
            for c in s:
                node = node[c]
            if '#' not in node:
                node['#'] = 0
            node['#'] += t
        self._reset()

    def input(self, c: str) -> List[str]:
        if c == '#':
            if '#' not in self.curr:
                self.curr['#'] = 0
            self.curr['#'] += 1
            self._reset()
            return []
        self.prefix.append(c)
        self.curr = self.curr[c]
        return self._find()
        
    def _dfs(self, node, suffix, results):
        if not node:
            return
        if '#' in node:
            times = node['#']
            results.append((-times, suffix[:]))
        for char, next_node in node.items():
            if char != '#':
                suffix.append(char)
                self._dfs(next_node, suffix, results)
                suffix.pop()
    
    def _find(self):
        results = []
        self._dfs(self.curr, [], results)
        results = nsmallest(3, results)
        return [''.join(self.prefix + suffix) for _, suffix in results]
        
    def _reset(self):
        self.curr = self.root
        self.prefix = []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)