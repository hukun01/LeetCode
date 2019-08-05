class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        If current char is smaller than the last char in stack, and the last char
        appears later in the string again, the last char can be removed and added 
        later. E.g., stack = "bc", and remaining string is "abc" then 'a' can 
        pop 'b' and then 'c'.
        We use a stack because we are only interested in the most recent chars. 
        We are interested in the most recent chars because we want to keep the relative order.
        
        Use a counter to tell whether a char appears later in the string again.
        
        Use a set to tell whether we already added the char to the answer.
        '''
        remainingLetters = collections.Counter(s)
        visited = set()
        stack = []
        for c in s:
            remainingLetters[c] -= 1
            if c in visited:
                continue
            while stack and c < stack[-1] and remainingLetters[stack[-1]] > 0:
                lastChar = stack.pop()
                visited.remove(lastChar)
            stack.append(c)
            visited.add(c)
        return ''.join(stack)