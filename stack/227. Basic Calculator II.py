class Solution:
    def calculate(self, s: str) -> int:
        '''
        Save the last sign, and iterate through s. Use a stack to store intermediate results, and sum them.
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
                    # to handle cases like -3//2 == -2, we use floating division and convert to integer
                    stack.append(int(stack.pop() / num))
                lastSign = c
        
        return sum(n for n in stack)