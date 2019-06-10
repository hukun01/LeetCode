class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        If current char is smaller than the last char in stack, and the last char
        appears later in the string again, the last char can be removed and added 
        later. E.g., stack = "bc", and remaining string is "abc" then 'a' can 
        pop 'b' and then 'c'.
        
        Use a counter to tell whether a char appears later in the string again.
        '''
        counter = collections.Counter(s)
        visited = set()
        stack = []
        for c in s:
            counter[c] -= 1
            if c in visited:
                continue
            while stack and stack[-1] > c and counter[stack[-1]] > 0:
                lastChar = stack.pop()
                visited.remove(lastChar)
            stack.append(c)
            visited.add(c)
        return ''.join(stack)