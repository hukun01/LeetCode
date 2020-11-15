# 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        String.
        With operation 1, the order of the string doesn't really matter.
        With operation 2, we need to ensure 2 things to make two strs match.
            1. two strs have the same set of chars, as the transform only
            happen within the same str;
            2. the char frequencies patterns match, so one str can transform
            the same size of group chars into another.

        Note that the dict.keys() returns dict_keys type which works like a set,
        so dict_keys([1, 2]) == dict_keys([2, 1]). However, dict.values() must
        be sorted before comparison.

        Time: O(1) as there's at most 26 letters.
        Space: O(1)

        Similar to 205. Isomorphic Strings
        '''
        c1, c2 = Counter(word1), Counter(word2)
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())