# 1415. The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        '''
        Similar to 60. Permutation Sequence
        Except that we can reuse the letters if they don't conflict.
        Also, the first letter comes from "abc", while the rest comes
        from any other two letters.
        '''
        abc = "abc"
        abc_len = len(abc)
        block_size = (abc_len - 1) ** (n - 1)
        if k > abc_len * block_size:
            return ""
        k -= 1
        first = abc[k // block_size]
        ans = [first]
        rest = { c: [c2 for c2 in abc if c2 != c] for c in abc }
        for _ in range(1, n):
            k %= block_size
            block_size //= (abc_len - 1)
            ans.append(rest[ans[-1]][k // block_size])
        return ''.join(ans)