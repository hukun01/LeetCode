class Solution:
    def calculate(self, s: str) -> int:
        '''
        When we see +-, we push the number with symbol to stack.
        When we see */, we must process the num at stack peek and current num, immediately.
        '''
        stack = []
        lastSign = '+'
        numStr = ""
        for i, c in enumerate(s):
            if c.isdigit():
                numStr += c
            if c in '+-*/' or i == len(s) - 1:
                num = int(numStr)
                numStr = ""
                if lastSign == '+':
                    stack.append(num)
                if lastSign == '-':
                    stack.append(-num)
                if lastSign == '*':
                    stack.append(stack.pop() * num)
                if lastSign == '/':
                    stack.append(int(stack.pop() / num))
                lastSign = c
        
        return sum(n for n in stack)