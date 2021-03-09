# 1737. Change Minimum Characters to Satisfy One of Three Conditions
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        '''
        Finding the splitting letter.

        Leverage the conditions of 'strictly less'. The key is to notice that
        this is all about lowercase letters, and if string 'a' is less than
        'b', then there must a letter, say x, that satisfies 'a' <= x < 'b'
        for every character. Hence x must be in ['a', 'z'), excluding 'z'.

        For condition 3, we just find the most common char, and change the rest
        of the chars. And we can start from here since it's simple.

        For condition 1 and 2, we try each letter, and see which one gives the
        min operations. E.g., for condition 1, at char x, assuming the count of
        letters less than or equal to x in string 'a' is c1[x], then we have
        1. len(a) - c1[x] is the chars strictly greater than x, and is also
           the count we need to change in 'a' so all chars in 'a' are less than
           or equal to x;
        2. c2[x] is the count we need to change in 'b', so all chars in 'b' are
           strictly greater than x.

        The optimization is to reuse the Counters to collect the total count
        of letters at each index that's less than the index letter. E.g.,
        c1[x + 1] += c1[x] means c1[x + 1] tracks the count of letters that's
        less than or equal to chr(ord('a') + x + 1), which is the sum of char
        at [x + 1] and all chars less than or equal to char at [x], aka c1[x].

        Time: O(len(a) + len(b))
        Space: O(1)
        '''
        c1 = Counter(ord(c) - ord('a') for c in a)
        c2 = Counter(ord(c) - ord('a') for c in b)
        ans = len(a) + len(b) - max((c1 + c2).values())
        for x in range(25):
            c1[x + 1] += c1[x]
            c2[x + 1] += c2[x]
            ans = min(ans, len(a) - c1[x] + c2[x])
            ans = min(ans, len(b) - c2[x] + c1[x])

        return ans