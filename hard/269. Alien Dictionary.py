class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        Find the prerequisite pairs by iterating every 2 words, and do topological sorting
        on the pair list.
        To make code concise, use list comprehension as much as possible.

        Don't use defaultdict here because we actually need to explicitly keep all chars in the dict.
        '''
        prevs = { c: set() for c in itertools.chain(*words) }
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    prevs[c2].add(c1)
                    break
        ans = []
        while True:
            removed = { c for c, prev in prevs.items() if len(prev) == 0 }
            if len(removed) == 0:
                break
            ans += removed
            prevs = { c: prevSet - removed for c, prevSet in prevs.items() if len(prevSet) > 0 }
        return ''.join(ans) if len(prevs) == 0 else ""