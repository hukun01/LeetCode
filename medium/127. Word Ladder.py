# 127. Word Ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Use 2-end BFS.
        Need to check whether endWord is in the wordList.
        '''
        words = set(wordList)
        if endWord not in words:
            return 0
        begins = set([beginWord])
        ends = set([endWord])
        steps = 1
        letters = { chr(ord('a') + i) for i in range(26) }
        while begins and ends:
            if len(begins) > len(ends):
                begins, ends = ends, begins

            next_level = set()
            for w in begins:
                for i in range(len(w)):
                    for l in letters:
                        new_w = w[:i] + l + w[i+1:]
                        if new_w in ends:
                            return steps + 1
                        if new_w in words:
                            words.remove(new_w)
                            next_level.add(new_w)
            steps += 1
            begins = next_level
        return 0