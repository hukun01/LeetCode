# 1190. Reverse Substrings Between Each Pair of Parentheses
class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        1/2 Stack.
        Use a stack to start collecting substrings that need to be
        reversed when seeing left paren, and add the reversed substring
        back when seeing right paren.

        Time: O(N^2)
        '''
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                x = stack.pop()
                stack[-1].extend(x[::-1])
            else:
                stack[-1].append(c)
        return ''.join(itertools.chain(*stack))
        '''
        2/2 Warmhole.
        Record all the left and right parens positions and pair them.
        Iterate through s, when seeing a paren, jump to its counterpart,
        and iterate to the reverse direction. When seeing a char, collect
        it in the final result.

        Time O(N).
        '''
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)