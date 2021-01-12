# 1717. Maximum Score From Removing Substrings
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = 'a'
        b = 'b'
        if x < y:
            a, b = b, a
            x, y = y, x

        seen = Counter()
        ans = 0
        for c in s + 'x':
            if c in 'ab':
                if c == b and seen[a] > 0:
                    seen[a] -= 1
                    ans += x
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()
        return ans