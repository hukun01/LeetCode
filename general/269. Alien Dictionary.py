class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Find the prerequisite pairs by iterating every 2 words, and do topological sorting
        on the pair list.
        To make code concise, use list comprehension as much as possible.
        '''
        if not words:
            return ''
        # build the prerequisite mapping
        prevWord = words[0]
        allChars = { char: set() for word in words for char in word }
        for word in words[1:]:
            for a, b in zip(prevWord, word):
                if a != b:
                    allChars[b].add(a)
                    break
            prevWord = word
            
        # topological sort
        ans = []
        while True:
            # get all chars without previous chars
            nextChars = [ char for char, preSet in allChars.items() if len(preSet) == 0 ]
            allChars = { char: preSet for char, preSet in allChars.items() if len(preSet) > 0 }
            if len(nextChars) == 0:
                break
            ans += nextChars
            for preSet in allChars.values():
                for char in nextChars:
                    if char in preSet:
                        preSet.remove(char)
            
        if len(allChars) > 0:
            return ''
        return ''.join(ans)