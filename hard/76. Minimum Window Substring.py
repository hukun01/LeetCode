# 76. Minimum Window Substring
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Sliding window.
        High level flow:
        1. Use two pointers: 'start' and 'end' to represent a window.
        2. Move 'end' to find a valid window.
        3. When a valid window is found, advance 'start' to find a smaller window.

        The current window is s[start:end+1] and the result window is
        s[final_start:final_end].
        Let need[c] store how many times I need character c (can be negative),
        and missing tells how many characters are still missing. 
        In the loop, first add the new character to the window. 
        Then, if nothing is missing, remove as much as possible 
        from the current window and then update the result.

        Sliding window part is similar to 30. Substring with Concatenation
        of All Words.
        '''
        need = Counter(t)
        missing = len(t)
        final_start = final_end = 0
        start = 0
        for end, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while start < end and need[s[start]] < 0:
                    need[s[start]] += 1
                    start += 1
                if final_end == 0 or end - start < final_end - final_start:
                    final_start, final_end = start, end+1

        return s[final_start: final_end]