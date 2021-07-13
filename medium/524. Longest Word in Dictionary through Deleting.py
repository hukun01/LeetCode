# 524. Longest Word in Dictionary through Deleting
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        '''
        State machines.

        Keep the mapping of current char -> iterator for each word, and as
        we go through s, we update the iterators whose keys match the current
        char.

        At the end, the number of exhausted iterators is the number of matched
        words. From the matched words, we find the one with the longest length
        and smallest alphabetically among the strings with the same length.

        Time: O(S + T) where S is the len(s), T is the total lengths of words.
        Space: O(W) where W is the number of words.
        '''
        iterators = defaultdict(list)
        for i, w in enumerate(dictionary):
            it = iter(w)
            iterators[next(it)].append((it, i))

        for c in s:
            if c not in iterators:
                continue

            for it, i in iterators.pop(c):
                iterators[next(it, None)].append((it, i))

        return min(
            (dictionary[idx] for _, idx in iterators[None]),
            key=lambda x: (-len(x), x),
            default="")