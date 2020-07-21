# 527. Word Abbreviation
class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        '''
        Trie.
        Group words by length, first char, last char.
        For each group, use a trie to count the frequencies of chars
        which starts from the second char (the first char always match in
        a group).
        On this trie, for each word, keep going deeper in the trie,
        until the number of shared prefixes with this word becomes one,
        which means the current word's prefix is unique, and we can
        potentially use it in the abbreviation.
        Now check whether the abbreviation saving length, if it's greater
        than 1, then use abbreviation, otherwise don't.

        The key is to leverage the trie to find the length of the
        unique prefix for each word in each group.
        '''
        groups = defaultdict(list)
        for i, w in enumerate(words):
            groups[(len(w), w[0], w[-1])].append((w, i))

        ans = [None] * len(words)
        Trie = lambda: defaultdict(Trie)
        COUNT = "count"
        for group in groups.values():
            trie = Trie()

            for w, _ in group:
                cur = trie
                for c in w[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[c]
            
            for w, w_index in group:
                cur = trie
                for i, c in enumerate(w[1:]):
                    if cur[COUNT] == 1:
                        break
                    cur = cur[c]
                if (save := len(w) - i - 2) > 1:
                    ans[w_index] = w[:i + 1] + str(save) + w[-1]
                else:
                    ans[w_index] = w
        return ans