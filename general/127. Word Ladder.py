class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Use 2-end BFS.
        Need to check whether endWord is in the wordList.
        '''
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        begins = set([beginWord])
        ends = set([endWord])
        steps = 1
        letters = "abcdefghijklmnopqrstuvwxyz"
        while len(begins) > 0 and len(ends) > 0:
            if len(begins) > len(ends):
                begins, ends = ends, begins
            
            nextSet = set()
            for word in begins:
                for i in range(len(word)):
                    for letter in letters:
                        nextWord = word[:i] + letter + word[i+1:]
                        if nextWord in ends:
                            return steps + 1
                        if nextWord in wordSet:
                            nextSet.add(nextWord)
                            wordSet.remove(nextWord)
            begins = nextSet
            steps += 1
        return 0