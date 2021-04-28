# 472. Concatenated Words
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        '''
        Trie + DFS + prune.

        Longer words must be built by shorter ones. Sort words by lengths.
        Add words to a Trie, when seeing a word, check whether existing words
        in Trie can form it, by doing a pruned DFS on the Trie.

        The DFS works this way: we track the word's index, and starts from
        Trie root, whenever the Trie node has a word, we try restarting DFS
        from the root again, and also try to continue on the current search.

        During DFS, we use visited to cache the word index that we went down
        and found infeasible, so we can prune the search. Without this pruning,
        we get TLE for cases like [a, aa, aaa, aaaa, ...] in which words share
        the same prefix.

        Time: O(n) where n is the total lengths of all the words. This is
              because we traverse each word at most 3 times. First and second
              times during DFS, third time at adding to the Trie.
        Space: O(n)
        '''
        Trie = lambda: defaultdict(Trie)
        root = Trie()
        words.sort(key=len)

        def dfs(word, idx, visited):
            if idx == len(word):
                return True

            if idx in visited:
                return False

            node = root
            for i in range(idx, len(word)):
                if word[i] in node:
                    node = node[word[i]]
                    if '$' in node and dfs(word, i + 1, visited):
                        return True
                else:
                    break

            visited.add(idx)
            return False

        ans = []
        for w in words:
            if not w:
                continue
            if dfs(w, 0, set()):
                ans.append(w)

            node = root
            for c in w:
                node = node[c]
            node['$'] = w

        return ans