class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        High level flow:
        1. Use two pointers: 'start' and 'end' to represent a window.
        2. Move 'end' to find a valid window.
        3. When a valid window is found, move 'start' to find a smaller window.

        The current window is s[i:j] and the result window is s[start:end].
        In need[c] I store how many times I need character c (can be negative),
        and missing tells how many characters are still missing. 
        In the loop, first add the new character to the window. 
        Then, if nothing is missing, remove as much as possible 
        from the current window and then update the result.
        '''
        need = collections.Counter(t)
        missing = len(t)
        i = start = end = 0
        size = float('inf')
        # j is base-1 index so that s[i:j] is valid
        for j, c in enumerate(s, 1):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j
            
        return s[start: end]