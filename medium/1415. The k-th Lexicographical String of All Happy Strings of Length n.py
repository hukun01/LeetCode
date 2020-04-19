# 1415. The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        '''
        Similar to 60. Permutation Sequence
        Except that we can reuse the letters if they don't conflict.
        '''
        fact = 1 << (n - 1)
        if k > 3 * fact:
            return ""
        k -= 1
        abc = "abc"
        ans = []
        ans.append(abc[k // fact])
        k %= fact
        rest = { 'a': 'bc', 'b': 'ac', 'c': 'ab' }
        for i in range(1, n):
            fact //= 2
            ans.append(rest[ans[-1]][k // fact])
            k %= fact
        return ''.join(ans)