class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        1/2 BFS.
        Let layer[word] be the list of paths that ends at word.
        newlayer[new_w] = [p + [new_w] for p in layer[word]] for all 'new_w'
        that's one char away from 'word'.

        Also remember to eliminate the used words in new layer from words, to
        reduce repetitive search.

        Time: O(V + E * p * w) where V is len(wordList), E is the number of
              edges, aka, number of 1-char away word pairs. p is the length
              of path, w is the length of a word.
        Space: O(p^2 * w)
        '''
        words = set(wordList)
        layer = {}
        layer[beginWord] = [[beginWord]]
        letters = "abcdefghijklmnopqrstuvwxyz"

        while layer:
            newlayer = defaultdict(list)
            for w, paths_to_w in layer.items():
                if w == endWord: 
                    return paths_to_w

                for i in range(len(w)):
                    for c in letters:
                        new_w = w[:i] + c + w[i+1:]
                        if new_w in words:
                            newlayer[new_w] += [p + [new_w] for p in paths_to_w]

            words -= set(newlayer.keys()) # this is critical for time
            layer = newlayer

        return []
        '''
        2/2 Use 2-end BFS to find the layers where we could get the paths, and
        use DFS to find the paths.
        '''
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        letters = "abcdefghijklmnopqrstuvwxyz"
        begins = [set([beginWord])]
        ends = [set([endWord])]
        def bfsFindLayers():
            nonlocal begins, ends
            while len(begins[-1]) > 0 and len(ends[-1]) > 0:
                if len(begins[-1]) > len(ends[-1]):
                    begins, ends = ends, begins

                nextSet = set()
                for word in begins[-1]:
                    for i in range(len(word)):
                        for letter in letters:
                            nextWord = word[:i] + letter + word[i+1:]
                            if nextWord in ends[-1]:
                                return
                            if nextWord in wordSet:
                                nextSet.add(nextWord)
                                wordSet.remove(nextWord) # this is critical for time
                begins.append(nextSet)
        bfsFindLayers()
        ans = []

        # remember to swap two sets to ensure they are ordered
        if beginWord not in begins[0]:
            begins, ends = ends, begins
        allLayers = begins + ends[::-1]
        def dfsFindPaths(path, idx):
            if len(path) == len(allLayers):
                ans.append(path[:])
                return
            last = path[-1]
            for i in range(len(last)):
                for l in letters:
                    node = last[:i] + l + last[i+1:]
                    if node in allLayers[idx]:
                        path.append(node)
                        dfsFindPaths(path, idx + 1)
                        path.pop()
        dfsFindPaths([beginWord], 1)
        return ans