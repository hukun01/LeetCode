# 1062. Longest Repeating Substring
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        def ok(window_size):
            seen = set()
            for i in range(0, n - window_size + 1):
                substr = s[i: i + window_size]
                if substr in seen:
                    return True
                seen.add(substr)
            return False

        l = 1
        h = n
        while l <= h:
            m = (l + h) // 2
            if ok(m):
                l = m + 1
            else:
                h = m - 1
        return l - 1