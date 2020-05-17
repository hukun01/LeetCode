# 1209. Remove All Adjacent Duplicates in String II
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        Linear scan with stack.
        Every time we see a different char than the last char, we add
        a new counter to the stack; when the counter reaches k, we erase
        the entry.
        '''
        stack = []
        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(char * count for char, count in stack)