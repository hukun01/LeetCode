class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Find the prerequisite pairs by iterating every 2 words, and do topological sorting
        on the pair list.
        To make code concise, use list comprehension as much as possible.
        '''
        prevs = { c: set() for word in words for c in word }
        for pair in zip(words, words[1:]):
            w1, w2 = pair[0], pair[1]
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    prevs[c2].add(c1)
                    break
        ans = []
        while True:
            removed = [p for p, prev in prevs.items() if len(prev) == 0]
            if len(removed) == 0:
                break
            ans += removed
            nextChars = set(removed)
            prevs = { char: prevSet - nextChars for char, prevSet in prevs.items() if len(prevSet) > 0 }
        return ''.join(ans) if len(prevs) == 0 else ""