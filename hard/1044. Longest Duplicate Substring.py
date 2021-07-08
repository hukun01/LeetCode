# 1044. Longest Duplicate Substring
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        '''
        Binary search + Rabin Karp rolling hash.
        Binary search the possible length of the substring, and check the
        length using rolling hash.

        Time: O(n log(n)) where n is len(s)
        Space: O(n)

        Similar to 718. Maximum Length of Repeated Subarray
        '''
        A = [ord(c) - ord('a') for c in s]
        mod = 2**63 - 1

        def check(L):
            base = 26
            p = pow(base, L, mod)
            cur = 0
            for i in range(L):
                cur = (cur * base + A[i]) % mod

            seen = {cur}
            for i in range(L, len(s)):
                cur = (cur * base + A[i] - A[i - L] * p % mod) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)
            return 0

        ans, l, h = 0, 0, len(s)
        while l < h:
            m = (l + h + 1) // 2
            pos = check(m)
            if pos:
                l = m
                ans = pos
            else:
                h = m - 1
        return s[ans: ans + l]