# 1737. Change Minimum Characters to Satisfy One of Three Conditions
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        '''
        Brute force with optimization.
        The key is to notice that this is all about lowercase letters, and if
        'a' is less than 'b', then there must a letter, say x, that satisfies
        'a' <= x < 'b' for every character. Hence x must be in ['a', 'z'),
        excluding 'z'.

        For condition 1 and 2, we try each letter, and see which one gives the
        min operations.
        For condition 3, we just find the most common char, and change the rest
        of the chars. And we can start from here since it's simple.

        The optimization is to reuse the Counters to collect the total count
        of letters at each index that's less than the index letter. E.g.,
        c1[i + 1] += c1[i] means c1[i + 1] tracks the count of letters that's
        less than or equal to chr(ord('a') + i + 1), which is the sum of char
        at [i + 1] and all chars less than or equal to char at [i], aka c1[i].

        Time: O(len(a) + len(b))
        Space: O(1)
        '''
        c1 = Counter(ord(c) - ord('a') for c in a)
        c2 = Counter(ord(c) - ord('a') for c in b)
        ans = len(a) + len(b) - max((c1 + c2).values())
        for i in range(25):
            c1[i + 1] += c1[i]
            c2[i + 1] += c2[i]
            ans = min(ans, len(a) - c1[i] + c2[i])
            ans = min(ans, len(b) - c2[i] + c1[i])

        return ans