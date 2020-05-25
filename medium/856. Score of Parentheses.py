# 856. Score of Parentheses
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        '''
        1/3 Stack. When seeing '(', just push into stack;
        when seeing ')', find the last seen '(', and add the score*2
        to the stack, or 1 if no intermediate scores found.
        '''
        stack = []
        for c in S:
            if c == '(':
                stack.append(c)
            else:
                total = 0
                while stack and stack[-1] != '(':
                    total += stack.pop()
                stack.pop()
                total = max(total * 2, 1)
                stack.append(total)
        return sum(stack)
        '''
        2/3 Stack (Better). Start the stack with [0], when seeing
        '(', push a 0; when seeing ')', find the last score, and double it,
        or use a 1, and push it back to the stack.
        '''
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(last * 2, 1)
        return stack.pop()
        '''
        3/3 Count the number of '()' (Best).
        Note that the final answer would be a sum of powers of 2.
        Each time we see a '(xxxx)', we double the score of 'xxxx';
        if we see a '((xx))', we add to answer "xx * 4", or "xx << 2",
        in which 2 is the balance of the total parentheses.
        '''
        ans = bal = 0
        for i, c in enumerate(S):
            if c == '(':
                bal += 1
            else:
                bal -= 1
                if S[i - 1] == '(':
                    ans += 1 << bal
        return ans