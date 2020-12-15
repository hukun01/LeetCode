# 132. Palindrome Partitioning II
class Solution:
    def minCut(self, s: str) -> int:
        '''
        1/2 DP.
        Let f[l, r] be the answer for s[l:r], we have 2 cases (can be combined)
        1. f[l, r] = 0 if s[l:r] is palindrome, or
        2. f[l, r] = min(f[l, k] + 1 for k in [l+1, r) where s[k:r] is palin)

        Time: O(n^2) where n is len(s), based on below process.
              check all k in [l, r]: # O(n)
                check all s[k:r] # O(n) after caching all is_palin info.
        Space: O(n^2)
        '''
        n = len(s)
        is_palin = [[False] * (n + 1) for _ in range(n + 1)]
        for l in range(n+1):
            for r in range(l, n+1):
                is_palin[l][r] = s[l:r] == s[l:r][::-1]

        @cache
        def dfs(l, r):
            if r - l <= 1:
                return 0
            ans = inf
            for k in range(l, r):
                if is_palin[k][r]:
                    ans = min(ans, (k > l) + dfs(l, k))
            return ans

        return dfs(0, len(s))
        '''
        2/2 DP another style with reduced space.
        Let cuts[i] be the min cuts for s[:i], we have two transitions
        1. cuts[i+j+1] = min(cuts[i-j] + 1 for all j
            where 0 <= i-j and i+j < n and s[i-j] == s[i+j])
        2. cuts[i+j+2] = min(cuts[i-j+2] + 1 for all j
            where 0 <= i-j and i+j+1 < n and s[i-j] == s[i+j+1])
        #1 is to find the odd-length longest palindrome with i as the center.
        #2 is to find the even-length one.

        Time: O(n^2)
        Space: O(n)
        Similar to 5. Longest Palindromic Substring
        '''
        n = len(s)
        cuts = [i-1 for i in range(n+1)]
        for i in range(n):
            j = 0
            while 0 <= i-j and i+j < n and s[i-j] == s[i+j]:
                cuts[i+j+1] = min(cuts[i+j+1], cuts[i-j] + 1)
                j += 1
            j = 0
            while 0 <= i-j and i+j+1 < n and s[i-j] == s[i+j+1]:
                cuts[i+j+2] = min(cuts[i+j+2], cuts[i-j] + 1)
                j += 1
        return cuts[-1]