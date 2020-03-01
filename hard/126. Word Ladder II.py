class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        Use 2-end BFS to find the layers where we could get the paths, and
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