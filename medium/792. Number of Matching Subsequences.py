# 792. Number of Matching Subsequences
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''
        1/2 State machines.

        Keep the mapping of current char -> iterator for each word, and as
        we go through s, we update the iterators whose keys match the current
        char.

        At the end, the number of exhausted iterators is the number of matched
        words.

        Time: O(T) where T is the total lengths of words.
        Space: O(W) where W is the number of words.

        Same as 524. Longest Word in Dictionary through Deleting
        '''
        states = defaultdict(list)
        for it in map(iter, words):
            states[next(it)].append(it)
        for c in s:
            for it in states.pop(c, ()):
                states[next(it, None)].append(it)

        return len(states[None])
        '''
        2/2 Collect the s indexes and do binary search for each word.

        Time: O(S + T*log(S)) where S is len(s)
        Space: O(S)
        '''
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        ans = 0
        for w in words:
            found = True
            prev = 0
            for i, c in enumerate(w):
                idx = bisect_left(pos[c], prev)
                if idx == len(pos[c]):
                    found = False
                    break
                prev = pos[c][idx] + 1
            if found:
                ans += 1

        return ans