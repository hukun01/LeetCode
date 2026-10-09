class Solution:
    def robotWithString(self, s: str) -> str:
        '''
        We need to understand the chars distribution globally when iterating through s.
        At every char in s, we need to know whether it's the smallest compared to the
        remaining chars after it.
        When the current char is the smallest, we move it to ans, and we keep comparing
        t[-1] with the remaining chars, and move t[-1] to ans if it's the smallest;
        Otherwise, we push the current char to t.
        
        In implementation, we always start with pushing char to t, and pop it out in the
        same round in a while loop.
        '''
        remaining, t, ans = Counter(s), [], []
        for char in s:
            t.append(char)
            if remaining[char] == 1:
                del remaining[char]
            else:
                remaining[char] -= 1
            while t and (not remaining or t[-1] <= min(remaining)):
                ans.append(t.pop())

        return ''.join(ans)
