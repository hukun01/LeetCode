# 28. Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        1/2 Rabin Karp, or rolling hash algorithm.
        Pseudo code of naive implementation:
            function RabinKarp(string s[1..n], string pattern[1..m])
                hpattern := hash(pattern[1..m]);
                for i from 1 to n-m+1
                    hs := hash(s[i..i+m-1])
                    if hs = hpattern
                        if s[i..i+m-1] = pattern[1..m]
                            return i
                return not found

        The key is to optimize this line "hs := hash(s[i..i+m-1])", as we don't
        need to spend O(m) time everytime, with rolling hash technique.
        Rolling hash formula at a high level.
        s[i+1..i+m] is built on s[i..i+m-1] and s[i] and s[i+m].

        Here we treat each char and their index as if they are at integers,
        where the alphabet size is the base. For example, in string 'abcd',
        hash for 'abc' will be ('a' * R^2 + 'b' * R + 'c') % mod, where R is
        the alphabet size, mod is a random large prime number.
        As we roll to the right, we need to add 'd' to the hash and shift
        existing factors by one step left, namely,
        ('a' * R^3 + 'b' * R^2 + 'c' * R + 'd') % mod, then we also discard
        'a', so the new hash is ('b' * R^2 + 'c' * R + 'd') % mod.

        Time: O(m + n) where m is len(needle), n is len(haystack)
        Space: O(1)
        '''
        m = len(needle)
        if m == 0:
            return 0
        R = 128 # radix
        mod = 10 ** 9 + 7
        RM = 1 # (R ^ M) % mod
        for _ in range(m):
            RM = (RM * R) % mod

        pattern_hash = 0
        for c in needle:
            pattern_hash = (pattern_hash * R + ord(c)) % mod

        txt_hash = 0
        for i in range(len(haystack)):
            txt_hash = (txt_hash * R + ord(haystack[i])) % mod

            if i < m - 1:
                continue
            
            if i >= m:
                txt_hash = (txt_hash + mod - RM * ord(haystack[i-m]) % mod) % mod

            offset = i - m + 1
            if pattern_hash == txt_hash and needle == haystack[offset:i + 1]:
                return offset

        return -1