# 425. Word Squares
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        '''
        Trie + DFS.
        The key is to eliminate most of the irrelevant words by prefix matching.
        '''
        Trie = lambda: defaultdict(Trie)
        tree = Trie()
        for w in words:
            node = tree
            for c in w:
                node = node[c]
            node['$'] = w
        
        def dfs2(node, results):
            #print(f"node {node}")
            if '$' in node:
                results.append(node['$'])
                return
            for char in node:
                dfs2(node[char], results)
        
        def find_relevant(path):
            if not path:
                return words
            size = len(path)
            node = tree
            for i in range(size):
                c = path[i][size]
                if not c in node:
                    return []
                node = node[c]
            my_words = []
            dfs2(node, my_words)
            return my_words
        
        n = len(words[0])
        # must be a n*n square
            
        ans = []
        def dfs(path):
            if len(path) == n:
                ans.append(path[:])
                return
            for w in find_relevant(path):
                path.append(w)
                dfs(path)
                path.pop()
        dfs([])
        return ans