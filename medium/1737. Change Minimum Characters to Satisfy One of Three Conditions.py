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

        Time: O(len(a) + len(b))
        Space: O(1)
        '''
        f1 = Counter(a)
        f2 = Counter(b)
        f3 = f1 + f2
        ans = len(a) + len(b) - max(f3.values()) # cond 3
        for c in range(25):
            char = chr(ord('a') + c)
            # cond 1
            s1 = sum(count for key, count in f1.items() if key > char)
            s2 = sum(count for key, count in f2.items() if key <= char)
            ans = min(ans, s1 + s2)
            # cond 2
            s1 = sum(count for key, count in f1.items() if key <= char)
            s2 = sum(count for key, count in f2.items() if key > char)
            ans = min(ans, s1 + s2)

        return ans